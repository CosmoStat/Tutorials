"""Generate mock shear+velocity catalog from a point mass field.

Physical model: Point mass at origin creates gravitational potential Φ = -Φ0/r, giving:
- Velocity: v = -∇Φ → radial inflow, v_r = -Φ0/r²
- Shear: γ ∝ ∂²Φ → tangential, γ_t ∝ Φ0/r³

Galaxies are distributed uniformly in an annulus (avoiding r~0 singularity).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from astropy.table import Table
from pathlib import Path

# Physical parameters - softened gravitational potential (Plummer-like)
# Φ = -Φ0 / sqrt(r² + rs²) avoids singularity at r=0
PHI0 = 1000.0   # potential amplitude
RS = 5.0        # softening/scale radius
R_MAX = 100.0   # outer radius for catalog
N_GAL = 2000    # number of galaxies for catalog

# Random seed for reproducibility
RNG_SEED = 42


def generate_positions_in_disk(n, r_max, rng):
    """Generate n random positions uniformly in a disk."""
    r = np.sqrt(rng.uniform(0, r_max**2, n))
    theta = rng.uniform(0, 2 * np.pi, n)
    return r * np.cos(theta), r * np.sin(theta), r, theta


def compute_potential(r, phi0, rs):
    """Softened gravitational potential: Φ = -Φ0 / sqrt(r² + rs²)."""
    return -phi0 / np.sqrt(r**2 + rs**2)


def compute_velocity(r, theta, phi0, rs):
    """Velocity from potential gradient: v = -∇Φ.

    For Φ = -Φ0/sqrt(r² + rs²): v_r = -Φ0 * r / (r² + rs²)^(3/2) (inward).
    """
    v_r = -phi0 * r / (r**2 + rs**2)**1.5
    v1 = v_r * np.cos(theta)
    v2 = v_r * np.sin(theta)
    return v1, v2


def compute_shear(r, theta, phi0, rs):
    """Shear from potential second derivatives.

    For softened potential: γ_t = 3Φ0 * r² / (2 * (r² + rs²)^(5/2))
    Convention: tangential shear → γ = -γ_t * exp(2iθ).
    """
    gamma_t = 1.5 * phi0 * r**2 / (r**2 + rs**2)**2.5
    g1 = -gamma_t * np.cos(2 * theta)
    g2 = -gamma_t * np.sin(2 * theta)
    return g1, g2


def plot_fields(phi0, rs, r_max, output_path, sample_x=None, sample_y=None):
    """Plot potential, velocity, and shear fields.

    Top row: Φ (scalar), velocity vectors (radial), shear sticks (tangential)
    Bottom row: v1, v2, g1, g2 showing spin-1/spin-2 structure
    """
    sns.set_theme(style='white')

    # Zoom to inner region for better visibility of amplitude variation
    plot_max = r_max * 0.5

    # Create grid for field evaluation (zoomed)
    grid = np.linspace(-plot_max, plot_max, 200)
    X, Y = np.meshgrid(grid, grid)
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    # Compute fields on grid (no masking needed - softened potential is finite everywhere)
    Phi = compute_potential(R, phi0, rs)
    V1, V2 = compute_velocity(R, Theta, phi0, rs)
    G1, G2 = compute_shear(R, Theta, phi0, rs)

    # Coarse grid for vectors/sticks
    sparse = np.linspace(-plot_max * 0.9, plot_max * 0.9, 11)
    Xs, Ys = np.meshgrid(sparse, sparse)
    Rs = np.sqrt(Xs**2 + Ys**2)
    Ts = np.arctan2(Ys, Xs)

    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 12, figure=fig, height_ratios=[1, 1], hspace=0.25, wspace=0.3,
                  left=0.02, right=0.98, top=0.92, bottom=0.05)

    # === Top row: Physical intuition (3 equal panels) ===

    # (a) Potential - non-diverging colormap with sampled positions
    ax = fig.add_subplot(gs[0, 0:4])
    ax.pcolormesh(X, Y, Phi, cmap='mako_r', shading='auto')
    if sample_x is not None and sample_y is not None:
        # Show subset of sampled positions within plot range
        mask = (np.abs(sample_x) < plot_max) & (np.abs(sample_y) < plot_max)
        ax.scatter(sample_x[mask][::5], sample_y[mask][::5], c='white', s=3, alpha=0.6,
                   label='sampled positions')
        ax.legend(loc='upper right', fontsize=8, framealpha=0.8)
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'(a) Potential $\Phi$', fontsize=12)

    # (b) Velocity vectors - radial inflow (sqrt-scaled length for visibility)
    ax = fig.add_subplot(gs[0, 4:8])
    v1s, v2s = compute_velocity(Rs, Ts, phi0, rs)
    v_mag = np.sqrt(v1s**2 + v2s**2)
    # Sqrt scaling: middle ground between linear (too steep) and log (too flat)
    v_mag_safe = np.where(v_mag > 0, v_mag, 1e-10)
    v_scale = np.sqrt(v_mag / np.nanmax(v_mag))
    v1_plot = v1s / v_mag_safe * v_scale
    v2_plot = v2s / v_mag_safe * v_scale
    ax.quiver(Xs, Ys, v1_plot, v2_plot, scale=10, width=0.008, color='C0', alpha=0.8)
    ax.scatter(0, 0, c='black', s=80, marker='x', zorder=10)
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'(b) Velocity $\mathbf{v}$ (radial)', fontsize=12)

    # (c) Shear sticks - tangential pattern (sqrt-scaled length for visibility)
    ax = fig.add_subplot(gs[0, 8:12])
    g1s, g2s = compute_shear(Rs, Ts, phi0, rs)
    g_mag = np.sqrt(g1s**2 + g2s**2)
    phi_g = 0.5 * np.arctan2(g2s, g1s)
    # Sqrt scaling: middle ground between linear (too steep) and log (too flat)
    g_scale = np.sqrt(g_mag / np.nanmax(g_mag))
    stick_base = 3.5
    for i in range(Xs.shape[0]):
        for j in range(Xs.shape[1]):
            stick_len = stick_base * g_scale[i, j]
            dx = stick_len * np.cos(phi_g[i, j])
            dy = stick_len * np.sin(phi_g[i, j])
            ax.plot([Xs[i,j] - dx, Xs[i,j] + dx],
                    [Ys[i,j] - dy, Ys[i,j] + dy],
                    color='C1', lw=1.5, alpha=0.8)
    ax.scatter(0, 0, c='black', s=80, marker='x', zorder=10)
    ax.set_xlim(-plot_max, plot_max)
    ax.set_ylim(-plot_max, plot_max)
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'(c) Shear $\gamma$ (tangential)', fontsize=12)

    # === Bottom row: Spin structure ===
    field_data = [
        (V1, r'$v_1$ (spin-1)'),
        (V2, r'$v_2$ (spin-1)'),
        (G1, r'$\gamma_1$ (spin-2)'),
        (G2, r'$\gamma_2$ (spin-2)'),
    ]

    for i, (field, title) in enumerate(field_data):
        ax = fig.add_subplot(gs[1, i*3:(i+1)*3])
        vmax = np.nanpercentile(np.abs(field), 99)
        ax.pcolormesh(X, Y, field, cmap='RdBu_r', shading='auto', vmin=-vmax, vmax=vmax)
        ax.set_aspect('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y') if i == 0 else None
        ax.set_title(title, fontsize=12)

    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved field visualization to {output_path}")
    plt.close()


def main():
    rng = np.random.default_rng(RNG_SEED)

    # Generate positions in full disk (no singularity with softened potential)
    x, y, r, theta = generate_positions_in_disk(N_GAL, R_MAX, rng)

    # Compute physical fields (no noise for clean signal)
    v1, v2 = compute_velocity(r, theta, PHI0, RS)
    g1, g2 = compute_shear(r, theta, PHI0, RS)

    # Add noise for realistic catalog
    noise_g = 0.01 * np.max(np.abs(g1))  # ~1% of max shear
    noise_v = 0.05 * np.max(np.abs(v1))  # ~5% of max velocity
    g1_noisy = g1 + rng.normal(0, noise_g, N_GAL)
    g2_noisy = g2 + rng.normal(0, noise_g, N_GAL)
    v1_noisy = v1 + rng.normal(0, noise_v, N_GAL)
    v2_noisy = v2 + rng.normal(0, noise_v, N_GAL)

    # Plot fields (output to same directory as script)
    output_dir = Path(__file__).parent
    plot_fields(PHI0, RS, R_MAX, output_dir / 'gv_mock_fields.png', sample_x=x, sample_y=y)

    # Save catalog (with noise)
    t = Table({
        'x': x, 'y': y,
        'g1': g1_noisy, 'g2': g2_noisy,
        'v1': v1_noisy, 'v2': v2_noisy
    })
    catalog_path = output_dir / 'gv_mock_catalog.fits'
    t.write(catalog_path, overwrite=True)

    print(f"Wrote {len(t)} galaxies to {catalog_path}")
    print(f"  r range: [{r.min():.1f}, {r.max():.1f}]")
    print(f"  |γ| range: [{np.sqrt(g1**2+g2**2).min():.2e}, {np.sqrt(g1**2+g2**2).max():.2e}]")
    print(f"  |v| range: [{np.sqrt(v1**2+v2**2).min():.2f}, {np.sqrt(v1**2+v2**2).max():.2f}]")


if __name__ == '__main__':
    main()
