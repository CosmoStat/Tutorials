"""Generate multi-lens shear+velocity fields for GV correlation tutorial.

Following the TreeCorr test_kv/test_kg pattern:
- N lenses in a box (uniform or sampled from Gaussian density field)
- Each lens contributes Gaussian-profile fields:
  - Velocity: v = -v0 exp(-r²/2r0²) (x+iy)/r (infall toward lens, spin-1)
  - Shear: γ = -γ0 exp(-r²/2r0²) (x+iy)²/r² (tangential, spin-2)
- Fields are summed over all lenses at each source position
- Correlations measure the stacked signal around lenses

With clustered lenses (CLUSTERED_LENSES=True):
- Lenses trace an underlying Gaussian density field
- One-halo term: signal from individual lens profiles
- Two-halo term: extra correlation from lens-lens clustering

This mimics real galaxy-galaxy lensing + kinematic measurements.
"""
import numpy as np
import treecorr
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from astropy.table import Table

# Field parameters (following TreeCorr test conventions)
GAMMA0 = 0.05   # shear amplitude
V0 = 0.05       # velocity amplitude
R0_G = 10.0     # shear scale radius
R0_V = 10.0     # velocity scale radius
R0 = R0_G       # reference scale for box size
L = 100.0 * R0  # box size
N_LENS = 1500   # number of lenses
N_SOURCE = 50000  # number of galaxies (sources)

# Lens clustering parameters
CLUSTERED_LENSES = False  # if True, sample lenses from Gaussian density field
XI_LENS = 5.0 * R0        # lens-lens correlation length (larger = more large-scale structure)
DELTA_RMS = 3.0           # RMS of density fluctuations (controls clustering strength)

RNG_SEED = 8675309


def generate_gaussian_field(ngrid, box_size, xi, rng):
    """Generate a Gaussian random field with Gaussian correlation function.

    ξ(r) = exp(-r²/2ξ²) → P(k) ∝ exp(-k²ξ²/2)
    """
    # Fourier grid
    kx = np.fft.fftfreq(ngrid, d=box_size/ngrid) * 2 * np.pi
    ky = np.fft.fftfreq(ngrid, d=box_size/ngrid) * 2 * np.pi
    KX, KY = np.meshgrid(kx, ky)
    K2 = KX**2 + KY**2

    # Gaussian power spectrum: P(k) ∝ exp(-k²ξ²/2)
    Pk = np.exp(-0.5 * K2 * xi**2)
    Pk[0, 0] = 0  # zero mean

    # Generate Gaussian field in Fourier space
    noise_real = rng.standard_normal((ngrid, ngrid))
    noise_imag = rng.standard_normal((ngrid, ngrid))
    delta_k = (noise_real + 1j * noise_imag) * np.sqrt(Pk)

    # Transform to real space
    delta = np.fft.ifft2(delta_k).real
    delta = delta / delta.std()  # normalize to unit variance
    return delta


def sample_lenses_from_field(n_lens, box_size, xi, delta_rms, rng):
    """Sample lens positions from a Gaussian density field via Poisson sampling."""
    ngrid = 256
    delta = generate_gaussian_field(ngrid, box_size, xi, rng)
    delta *= delta_rms  # scale to desired RMS

    # Density field: ρ ∝ (1 + δ), clipped to avoid negative densities
    density = np.maximum(1 + delta, 0.01)

    # Normalize to get probability distribution
    prob = density / density.sum()

    # Sample grid cells according to probability
    flat_prob = prob.ravel()
    indices = rng.choice(len(flat_prob), size=n_lens, p=flat_prob)

    # Convert to positions with sub-cell jitter
    iy, ix = np.unravel_index(indices, (ngrid, ngrid))
    cell_size = box_size / ngrid
    xl = (ix + rng.uniform(0, 1, n_lens)) * cell_size - box_size/2
    yl = (iy + rng.uniform(0, 1, n_lens)) * cell_size - box_size/2

    return xl, yl, delta


def make_gv_fields(rng):
    """Generate multi-lens shear and velocity fields.

    Returns lens positions, source positions, source fields (g1, g2, v1, v2),
    and the density field (if clustered) or None.
    """
    # Lens positions (uniform or clustered)
    if CLUSTERED_LENSES:
        xl, yl, delta = sample_lenses_from_field(N_LENS, L, XI_LENS, DELTA_RMS, rng)
    else:
        xl = (rng.random(N_LENS) - 0.5) * L
        yl = (rng.random(N_LENS) - 0.5) * L
        delta = None

    # Source positions (always uniform)
    xs = (rng.random(N_SOURCE) - 0.5) * L
    ys = (rng.random(N_SOURCE) - 0.5) * L

    # Initialize fields
    g1 = np.zeros(N_SOURCE)
    g2 = np.zeros(N_SOURCE)
    v1 = np.zeros(N_SOURCE)
    v2 = np.zeros(N_SOURCE)

    # Sum contributions from all halos
    for x, y in zip(xl, yl):
        dx = xs - x
        dy = ys - y
        r2 = dx**2 + dy**2
        r = np.sqrt(r2)
        r_safe = np.where(r > 0, r, 1e-10)

        # Gaussian envelope
        envelope = np.exp(-0.5 * r2 / R0**2)

        # Velocity (spin-1): v = -v0 exp(-r²/2r0_v²) (dx+idy)/r0_v (infall toward lens)
        envelope_v = np.exp(-0.5 * r2 / R0_V**2)
        v1 += -V0 * envelope_v * dx / R0_V
        v2 += -V0 * envelope_v * dy / R0_V

        # Shear (spin-2): γ = -γ0 exp(-r²/2r0_g²) (dx+idy)²/r0_g²
        envelope_g = np.exp(-0.5 * r2 / R0_G**2)
        g1 += -GAMMA0 * envelope_g * (dx**2 - dy**2) / R0_G**2
        g2 += -GAMMA0 * envelope_g * (2 * dx * dy) / R0_G**2

    return xl, yl, xs, ys, g1, g2, v1, v2, delta


def measure_correlations(xl, yl, xs, ys, g1, g2, v1, v2):
    """Measure GG, VV, and GV correlations (source-source)."""
    # Separate catalogs for G and V (GV needs two catalogs)
    cat_g = treecorr.Catalog(x=xs, y=ys, g1=g1, g2=g2,
                              x_units='arcmin', y_units='arcmin')
    cat_v = treecorr.Catalog(x=xs, y=ys, v1=v1, v2=v2,
                              x_units='arcmin', y_units='arcmin')

    corr_params = dict(min_sep=1, max_sep=200, nbins=25, sep_units='arcmin')

    # GG: shear-shear correlation
    gg = treecorr.GGCorrelation(**corr_params)
    gg.process(cat_g)

    # VV: velocity-velocity correlation
    vv = treecorr.VVCorrelation(**corr_params)
    vv.process(cat_v)

    # GV: shear-velocity correlation
    gv = treecorr.VGCorrelation(**corr_params)
    gv.process(cat_v, cat_g)

    return gg, vv, gv


def compute_fields_on_grid(xl, yl, plot_max, ngrid=100):
    """Compute shear and velocity fields on a grid for given lens positions."""
    grid = np.linspace(-plot_max, plot_max, ngrid)
    X, Y = np.meshgrid(grid, grid)
    Xf, Yf = X.ravel(), Y.ravel()

    G1 = np.zeros_like(Xf)
    G2 = np.zeros_like(Xf)
    V1 = np.zeros_like(Xf)
    V2 = np.zeros_like(Xf)

    for x, y in zip(xl, yl):
        dx = Xf - x
        dy = Yf - y
        r2 = dx**2 + dy**2

        envelope_v = np.exp(-0.5 * r2 / R0_V**2)
        V1 += -V0 * envelope_v * dx / R0_V
        V2 += -V0 * envelope_v * dy / R0_V

        envelope_g = np.exp(-0.5 * r2 / R0_G**2)
        G1 += -GAMMA0 * envelope_g * (dx**2 - dy**2) / R0_G**2
        G2 += -GAMMA0 * envelope_g * (2 * dx * dy) / R0_G**2

    return X, Y, V1.reshape(X.shape), V2.reshape(X.shape), G1.reshape(X.shape), G2.reshape(X.shape)


def compute_fields_sparse(xl, yl, plot_max, ngrid=15):
    """Compute fields on sparse grid for vector/stick visualization."""
    sparse = np.linspace(-plot_max * 0.9, plot_max * 0.9, ngrid)
    Xs, Ys = np.meshgrid(sparse, sparse)
    Xsf, Ysf = Xs.ravel(), Ys.ravel()

    v1s = np.zeros_like(Xsf)
    v2s = np.zeros_like(Xsf)
    g1s = np.zeros_like(Xsf)
    g2s = np.zeros_like(Xsf)

    for x, y in zip(xl, yl):
        dx = Xsf - x
        dy = Ysf - y
        r2 = dx**2 + dy**2

        envelope_v = np.exp(-0.5 * r2 / R0_V**2)
        v1s += -V0 * envelope_v * dx / R0_V
        v2s += -V0 * envelope_v * dy / R0_V

        envelope_g = np.exp(-0.5 * r2 / R0_G**2)
        g1s += -GAMMA0 * envelope_g * (dx**2 - dy**2) / R0_G**2
        g2s += -GAMMA0 * envelope_g * (2 * dx * dy) / R0_G**2

    return Xs, Ys, v1s.reshape(Xs.shape), v2s.reshape(Xs.shape), g1s.reshape(Xs.shape), g2s.reshape(Xs.shape)


def plot_fields(xl, yl, xs, ys, g1, g2, v1, v2, output_path, delta=None):
    """Plot multi-lens shear and velocity fields.

    Top row (3 panels): sources+lenses, net velocity, net shear
    Bottom row (4 panels): v1, v2, γ1, γ2 components
    """
    sns.set_theme(style='white')

    plot_max = L * 0.1
    X, Y, V1, V2, G1, G2 = compute_fields_on_grid(xl, yl, plot_max)
    Xs, Ys, v1s, v2s, g1s, g2s = compute_fields_sparse(xl, yl, plot_max)

    # Use GridSpec: top row has 3 centered panels, bottom row has 4
    fig = plt.figure(figsize=(14, 8))
    gs_top = fig.add_gridspec(1, 3, left=0.08, right=0.92, top=0.95, bottom=0.55, wspace=0.3)
    gs_bot = fig.add_gridspec(1, 4, left=0.05, right=0.95, top=0.45, bottom=0.08, wspace=0.3)

    lens_mask = (np.abs(xl) < plot_max) & (np.abs(yl) < plot_max)

    # === Top row: 3 centered panels ===

    # (a) Source positions + lenses (zoom)
    ax = fig.add_subplot(gs_top[0, 0])
    src_mask = (np.abs(xs) < plot_max) & (np.abs(ys) < plot_max)
    ax.scatter(xs[src_mask][::3], ys[src_mask][::3], s=1, alpha=0.4, c='C0', label='sources')
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.8, label='lenses')
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(f'(a) Sources + lenses')
    ax.legend(fontsize=8, loc='upper right')

    # (b) Velocity vectors
    ax = fig.add_subplot(gs_top[0, 1])
    v_mag = np.sqrt(v1s**2 + v2s**2)
    v_mag_safe = np.where(v_mag > 0, v_mag, 1e-10)
    v_scale = np.sqrt(v_mag / np.nanmax(v_mag))
    ax.quiver(Xs, Ys, v1s/v_mag_safe*v_scale, v2s/v_mag_safe*v_scale,
              scale=15, width=0.006, color='C0', alpha=0.7)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.8)
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(b) Net velocity $\mathbf{v}$')

    # (c) Shear sticks
    ax = fig.add_subplot(gs_top[0, 2])
    g_mag = np.sqrt(g1s**2 + g2s**2)
    phi_g = 0.5 * np.arctan2(g2s, g1s)
    g_scale = np.sqrt(g_mag / np.nanmax(g_mag))
    stick_base = plot_max * 0.03
    for i in range(Xs.shape[0]):
        for j in range(Xs.shape[1]):
            stick_len = stick_base * g_scale[i, j]
            dx = stick_len * np.cos(phi_g[i, j])
            dy = stick_len * np.sin(phi_g[i, j])
            ax.plot([Xs[i,j] - dx, Xs[i,j] + dx],
                    [Ys[i,j] - dy, Ys[i,j] + dy],
                    color='C1', lw=1.2, alpha=0.7)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.8)
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(c) Net shear $\gamma$')

    # === Bottom row: 4 spin component panels ===

    # (d) v1 component
    ax = fig.add_subplot(gs_bot[0, 0])
    vmax_v = np.nanpercentile(np.abs(V1), 99)
    ax.pcolormesh(X, Y, V1, cmap='RdBu_r', shading='auto', vmin=-vmax_v, vmax=vmax_v)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(d) $v_1$ — spin-1')

    # (e) v2 component
    ax = fig.add_subplot(gs_bot[0, 1])
    ax.pcolormesh(X, Y, V2, cmap='RdBu_r', shading='auto', vmin=-vmax_v, vmax=vmax_v)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(e) $v_2$ — spin-1')

    # (f) g1 component
    ax = fig.add_subplot(gs_bot[0, 2])
    vmax_g = np.nanpercentile(np.abs(G1), 99)
    ax.pcolormesh(X, Y, G1, cmap='RdBu_r', shading='auto', vmin=-vmax_g, vmax=vmax_g)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(f) $\gamma_1$ — spin-2')

    # (g) g2 component
    ax = fig.add_subplot(gs_bot[0, 3])
    ax.pcolormesh(X, Y, G2, cmap='RdBu_r', shading='auto', vmin=-vmax_g, vmax=vmax_g)
    ax.scatter(xl[lens_mask], yl[lens_mask], c='black', s=30, marker='.', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('x [arcmin]')
    ax.set_ylabel('y [arcmin]')
    ax.set_title(r'(g) $\gamma_2$ — spin-2')

    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved fields plot to {output_path}")
    plt.close()


def create_lens_buildup_gif(xl, yl, output_path):
    """Create GIF showing field buildup: 1 lens → 10 lenses → all lenses."""
    import imageio.v2 as imageio
    from pathlib import Path

    plot_max = L * 0.1
    frames = []
    temp_dir = Path(output_path).parent

    # Select lenses that are in the zoomed region (for clearer visualization)
    in_region = (np.abs(xl) < plot_max * 0.8) & (np.abs(yl) < plot_max * 0.8)
    xl_visible = xl[in_region]
    yl_visible = yl[in_region]

    # Use visible lenses for buildup, then all lenses for final frame
    n_visible = len(xl_visible)
    n_stages = [1, min(10, n_visible), n_visible]

    # Compute fields for all lenses to get consistent color scale
    _, _, V1_all, V2_all, G1_all, G2_all = compute_fields_on_grid(xl, yl, plot_max)
    vmax_v = np.nanmax(np.abs(V1_all))
    vmax_g = np.nanmax(np.abs(G1_all))

    for idx, n in enumerate(n_stages):
        # For stages 1 and 2, use visible lenses; for stage 3, use all
        if idx < 2:
            xl_sub = xl_visible[:n]
            yl_sub = yl_visible[:n]
            title_n = n
        else:
            xl_sub = xl
            yl_sub = yl
            title_n = len(xl)

        X, Y, V1, V2, G1, G2 = compute_fields_on_grid(xl_sub, yl_sub, plot_max)
        Xs, Ys, v1s, v2s, g1s, g2s = compute_fields_sparse(xl_sub, yl_sub, plot_max)

        fig = plt.figure(figsize=(14, 8))
        gs = fig.add_gridspec(2, 4, height_ratios=[1, 1], hspace=0.25, wspace=0.3)

        lens_mask = (np.abs(xl_sub) < plot_max) & (np.abs(yl_sub) < plot_max)

        # Top row: 3 panels (shared y-axis)
        # (a) Lenses
        ax0 = fig.add_subplot(gs[0, 0])
        ax0.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.8)
        ax0.set_xlim(-plot_max, plot_max)
        ax0.set_ylim(-plot_max, plot_max)
        ax0.set_aspect('equal')
        ax0.set_xlabel('x [arcmin]')
        ax0.set_ylabel('y [arcmin]')
        ax0.set_title(f'(a) Lenses (N={title_n})')

        # (b) Velocity vectors
        ax = fig.add_subplot(gs[0, 1], sharey=ax0)
        if np.any(v1s != 0):
            v_mag = np.sqrt(v1s**2 + v2s**2)
            v_mag_safe = np.where(v_mag > 0, v_mag, 1e-10)
            v_scale = np.sqrt(v_mag / np.nanmax(v_mag)) if np.nanmax(v_mag) > 0 else np.ones_like(v_mag)
            ax.quiver(Xs, Ys, v1s/v_mag_safe*v_scale, v2s/v_mag_safe*v_scale,
                      scale=15, width=0.006, color='C0', alpha=0.7)
        ax.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.8)
        ax.set_xlim(-plot_max, plot_max)
        ax.set_aspect('equal')
        ax.set_xlabel('x [arcmin]')
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title(r'(b) Net velocity $\mathbf{v}$')

        # (c) Shear sticks
        ax = fig.add_subplot(gs[0, 2], sharey=ax0)
        if np.any(g1s != 0):
            g_mag = np.sqrt(g1s**2 + g2s**2)
            phi_g = 0.5 * np.arctan2(g2s, g1s)
            g_scale = np.sqrt(g_mag / np.nanmax(g_mag)) if np.nanmax(g_mag) > 0 else np.ones_like(g_mag)
            stick_base = plot_max * 0.03
            for i in range(Xs.shape[0]):
                for j in range(Xs.shape[1]):
                    stick_len = stick_base * g_scale[i, j]
                    dx = stick_len * np.cos(phi_g[i, j])
                    dy = stick_len * np.sin(phi_g[i, j])
                    ax.plot([Xs[i,j] - dx, Xs[i,j] + dx],
                            [Ys[i,j] - dy, Ys[i,j] + dy],
                            color='C1', lw=1.2, alpha=0.7)
        ax.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.8)
        ax.set_xlim(-plot_max, plot_max)
        ax.set_aspect('equal')
        ax.set_xlabel('x [arcmin]')
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title(r'(c) Net shear $\gamma$')

        ax = fig.add_subplot(gs[0, 3])
        ax.axis('off')

        # Bottom row: 4 components (shared y-axis, consistent color scale)
        ax1 = fig.add_subplot(gs[1, 0])
        ax1.pcolormesh(X, Y, V1, cmap='RdBu_r', shading='auto', vmin=-vmax_v, vmax=vmax_v, rasterized=True)
        ax1.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.5)
        ax1.set_aspect('equal')
        ax1.set_xlabel('x [arcmin]')
        ax1.set_ylabel('y [arcmin]')
        ax1.set_title(r'(d) $v_1$ — spin-1')

        ax = fig.add_subplot(gs[1, 1], sharey=ax1)
        ax.pcolormesh(X, Y, V2, cmap='RdBu_r', shading='auto', vmin=-vmax_v, vmax=vmax_v, rasterized=True)
        ax.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.5)
        ax.set_aspect('equal')
        ax.set_xlabel('x [arcmin]')
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title(r'(e) $v_2$ — spin-1')

        ax = fig.add_subplot(gs[1, 2], sharey=ax1)
        ax.pcolormesh(X, Y, G1, cmap='RdBu_r', shading='auto', vmin=-vmax_g, vmax=vmax_g, rasterized=True)
        ax.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.5)
        ax.set_aspect('equal')
        ax.set_xlabel('x [arcmin]')
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title(r'(f) $\gamma_1$ — spin-2')

        ax = fig.add_subplot(gs[1, 3], sharey=ax1)
        ax.pcolormesh(X, Y, G2, cmap='RdBu_r', shading='auto', vmin=-vmax_g, vmax=vmax_g, rasterized=True)
        ax.scatter(xl_sub[lens_mask], yl_sub[lens_mask], c='black', s=30, marker='.', alpha=0.5)
        ax.set_aspect('equal')
        ax.set_xlabel('x [arcmin]')
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title(r'(g) $\gamma_2$ — spin-2')

        fig.suptitle(f'Field buildup: {title_n} lens{"es" if title_n > 1 else ""}', fontsize=14, y=0.98)

        # Save frame
        frame_path = temp_dir / f'_frame_{n}.png'
        plt.savefig(frame_path, dpi=100, bbox_inches='tight')
        plt.close()
        frames.append(imageio.imread(frame_path))
        frame_path.unlink()

    # Create GIF (1.5 seconds per frame)
    imageio.mimsave(output_path, frames, duration=1500, loop=0)
    print(f"Saved lens buildup GIF to {output_path}")


def plot_correlations(ng, nv, gv, output_path):
    """Plot lens-source and source-source correlations."""
    sns.set_theme(style='whitegrid')
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    r = ng.meanr

    # NG: tangential shear profile
    ax = axes[0]
    # Theory: γ_t(r) = γ0 exp(-r²/2r0²)
    true_gt = GAMMA0 * np.exp(-0.5 * r**2 / R0**2)
    ax.errorbar(r, ng.xi, yerr=np.sqrt(ng.varxi), fmt='o', capsize=3, label='measured')
    ax.plot(r, true_gt, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\gamma_t(r)$')
    ax.set_xscale('log')
    ax.set_title('NG: lens-shear (tangential)')
    ax.legend()

    # NV: radial velocity profile
    ax = axes[1]
    # Theory: v_r(r) = -v0 exp(-r²/2r0²) (infall toward lens)
    true_vr = -V0 * np.exp(-0.5 * r**2 / R0**2)
    ax.errorbar(r, nv.xi, yerr=np.sqrt(nv.varxi), fmt='o', capsize=3, label='measured')
    ax.plot(r, true_vr, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$v_r(r)$')
    ax.set_xscale('log')
    ax.set_title('NV: lens-velocity (radial)')
    ax.legend()

    # GV: shear-velocity correlation
    ax = axes[2]
    ax.errorbar(gv.meanr, gv.xip, yerr=np.sqrt(gv.varxip), fmt='o', capsize=3,
                label=r'$\xi_+$ (spin-1)')
    ax.errorbar(gv.meanr, gv.xim, yerr=np.sqrt(gv.varxim), fmt='s', capsize=3,
                label=r'$\xi_-$ (spin-3)')
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi(r)$')
    ax.set_xscale('log')
    ax.set_title('GV: shear-velocity')
    ax.legend()

    fig.suptitle(f'Multi-lens correlations (N_lens={N_LENS}, N_source={N_SOURCE})', y=1.02)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved correlation plot to {output_path}")
    plt.close()


def run_single(rng, clustered, output_dir):
    """Run simulation with given clustering setting, return correlations."""
    global CLUSTERED_LENSES
    CLUSTERED_LENSES = clustered

    clustering_str = f"clustered (ξ={XI_LENS:.0f})" if clustered else "uniform"
    print(f"\n=== {clustering_str.upper()} LENSES ===")
    print(f"Generating {N_LENS} lenses and {N_SOURCE} sources...")

    xl, yl, xs, ys, g1, g2, v1, v2, delta = make_gv_fields(rng)

    # Add noise (same level for fair comparison)
    noise_rng = np.random.default_rng(42)  # fixed seed for noise
    g1 += noise_rng.normal(0, 0.01, N_SOURCE)
    g2 += noise_rng.normal(0, 0.01, N_SOURCE)
    v1 += noise_rng.normal(0, 0.01, N_SOURCE)
    v2 += noise_rng.normal(0, 0.01, N_SOURCE)

    print(f"  |γ| max: {np.sqrt(g1**2 + g2**2).max():.4f}")
    print(f"  |v| max: {np.sqrt(v1**2 + v2**2).max():.4f}")

    suffix = "clustered" if clustered else "uniform"
    plot_fields(xl, yl, xs, ys, g1, g2, v1, v2,
                output_dir / f'gv_halo_fields_{suffix}.png', delta=delta)

    print("Measuring correlations...")
    gg, vv, gv = measure_correlations(xl, yl, xs, ys, g1, g2, v1, v2)

    print(f"  GG ξ+ max: {np.abs(gg.xip).max():.2e}")
    print(f"  VV ξ+ max: {np.abs(vv.xip).max():.2e}")
    print(f"  GV ξ+ max: {np.abs(gv.xip).max():.2e}")

    return gg, vv, gv


def compute_theory_correlations(r):
    """Compute theoretical GG, VV correlations for TreeCorr-style profiles.

    From TreeCorr tests (test_gg.py, test_vv.py):
    - γ = -γ0 exp(-r²/2r0_g²) (x+iy)²/r0_g²
    - v = v0 exp(-r²/2r0_v²) (x+iy)/r0_v

    Using separate scale radii: R0_G for shear, R0_V for velocity.
    """
    # GG theory (spin-2) with R0_G
    gauss_g = np.exp(-0.25 * r**2 / R0_G**2)
    temp_gg = np.pi/16 * GAMMA0**2 * (R0_G/L)**2 * gauss_g * N_LENS
    gg_theory = temp_gg * (r**4 - 16*r**2*R0_G**2 + 32*R0_G**4) / R0_G**4

    # VV theory (spin-1) with R0_V
    gauss_v = np.exp(-0.25 * r**2 / R0_V**2)
    temp_vv = np.pi/4 * V0**2 * (R0_V/L)**2 * gauss_v * N_LENS
    vv_theory = temp_vv * (4*R0_V**2 - r**2) / R0_V**2

    # GV theory: not yet derived
    gv_theory = None

    return gg_theory, vv_theory, gv_theory


def plot_correlations(gg, vv, gv, output_path):
    """Plot GG, VV, GV correlations with theory predictions."""
    sns.set_theme(style='whitegrid')
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))

    r = gg.meanr
    gg_th, vv_th, gv_th = compute_theory_correlations(r)

    # Correlation lengths from actual profile scales
    r_corr_g = R0_G
    r_corr_v = R0_V

    # GG ξ+
    ax = axes[0, 0]
    ax.errorbar(r, gg.xip, yerr=np.sqrt(gg.varxip), fmt='o', capsize=2,
                label=r'$\xi_+$ measured', alpha=0.8, ms=5)
    ax.plot(r, gg_th, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.axvline(r_corr_g, color='C3', ls='--', alpha=0.6, label=rf'$r_\gamma={r_corr_g:.0f}$')
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_+(r)$')
    ax.set_xscale('log')
    ax.set_title(r'GG: $\xi_+$')
    ax.legend(fontsize=8)

    # VV ξ+
    ax = axes[0, 1]
    ax.errorbar(r, vv.xip, yerr=np.sqrt(vv.varxip), fmt='o', capsize=2,
                label=r'$\xi_+$ measured', alpha=0.8, ms=5)
    ax.plot(r, vv_th, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.axvline(r_corr_v, color='C3', ls='--', alpha=0.6, label=rf'$r_v={r_corr_v:.0f}$')
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_+(r)$')
    ax.set_xscale('log')
    ax.set_title(r'VV: $\xi_+$')
    ax.legend(fontsize=8)

    # GV ξ+ (no theory, no marker)
    ax = axes[0, 2]
    ax.errorbar(r, gv.xip, yerr=np.sqrt(gv.varxip), fmt='o', capsize=2,
                label=r'$\xi_+$ measured', alpha=0.8, ms=5)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_+(r)$')
    ax.set_xscale('log')
    ax.set_title(r'GV: $\xi_+$')
    ax.legend(fontsize=8)

    # GG ξ-
    ax = axes[1, 0]
    ax.errorbar(r, gg.xim, yerr=np.sqrt(gg.varxim), fmt='s', capsize=2,
                label=r'$\xi_-$ measured', alpha=0.8, ms=5, color='C1')
    # ξ- theory with R0_G
    gg_xim_th = np.pi/16 * GAMMA0**2 * (R0_G/L)**2 * np.exp(-0.25*r**2/R0_G**2) * N_LENS * r**4/R0_G**4
    ax.plot(r, gg_xim_th, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.axvline(r_corr_g, color='C3', ls='--', alpha=0.6, label=rf'$r_\gamma={r_corr_g:.0f}$')
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_-(r)$')
    ax.set_xscale('log')
    ax.set_title(r'GG: $\xi_-$')
    ax.legend(fontsize=8)

    # VV ξ-
    ax = axes[1, 1]
    ax.errorbar(r, vv.xim, yerr=np.sqrt(vv.varxim), fmt='s', capsize=2,
                label=r'$\xi_-$ measured', alpha=0.8, ms=5, color='C1')
    # ξ- theory with R0_V
    vv_xim_th = -np.pi/4 * V0**2 * (R0_V/L)**2 * np.exp(-0.25*r**2/R0_V**2) * N_LENS * r**2/R0_V**2
    ax.plot(r, vv_xim_th, 'k--', label='theory', alpha=0.7)
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.axvline(r_corr_v, color='C3', ls='--', alpha=0.6, label=rf'$r_v={r_corr_v:.0f}$')
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_-(r)$')
    ax.set_xscale('log')
    ax.set_title(r'VV: $\xi_-$')
    ax.legend(fontsize=8)

    # GV ξ- (no theory, no marker)
    ax = axes[1, 2]
    ax.errorbar(r, gv.xim, yerr=np.sqrt(gv.varxim), fmt='s', capsize=2,
                label=r'$\xi_-$ measured', alpha=0.8, ms=5, color='C1')
    ax.axhline(0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Separation r [arcmin]')
    ax.set_ylabel(r'$\xi_-(r)$')
    ax.set_xscale('log')
    ax.set_title(r'GV: $\xi_-$')
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved correlation plot to {output_path}")
    plt.close()


def main():
    rng = np.random.default_rng(RNG_SEED)
    output_dir = Path(__file__).parent

    print(f"Generating {N_LENS} lenses and {N_SOURCE} sources...")
    xl, yl, xs, ys, g1, g2, v1, v2, delta = make_gv_fields(rng)

    # Add noise
    g1 += rng.normal(0, 0.01, N_SOURCE)
    g2 += rng.normal(0, 0.01, N_SOURCE)
    v1 += rng.normal(0, 0.01, N_SOURCE)
    v2 += rng.normal(0, 0.01, N_SOURCE)

    print(f"  |γ| max: {np.sqrt(g1**2 + g2**2).max():.4f}")
    print(f"  |v| max: {np.sqrt(v1**2 + v2**2).max():.4f}")

    plot_fields(xl, yl, xs, ys, g1, g2, v1, v2,
                output_dir / 'gv_halo_fields.png', delta=delta)

    # Create lens buildup GIF
    create_lens_buildup_gif(xl, yl, output_dir / 'gv_halo_buildup.gif')

    print("\nMeasuring correlations...")
    gg, vv, gv = measure_correlations(xl, yl, xs, ys, g1, g2, v1, v2)

    print(f"  GG ξ+ max: {np.abs(gg.xip).max():.2e}")
    print(f"  VV ξ+ max: {np.abs(vv.xip).max():.2e}")
    print(f"  GV ξ+ max: {np.abs(gv.xip).max():.2e}")

    plot_correlations(gg, vv, gv, output_dir / 'gv_halo_correlation.png')

    # Save source catalog
    catalog = Table({
        'x': xs, 'y': ys,
        'g1': g1, 'g2': g2,
        'v1': v1, 'v2': v2
    })
    catalog_path = output_dir / 'gv_mock_catalog.fits'
    catalog.write(catalog_path, overwrite=True)
    print(f"Saved catalog ({len(catalog)} sources) to {catalog_path}")


if __name__ == '__main__':
    main()
