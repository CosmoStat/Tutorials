# Shear-Velocity Correlation Tutorial Redesign

**Kind:** spec
**Status:** draft
**Tags:** [tutorial] [cosmology] [treecorr]

## Goal

Build a tutorial demonstrating shear-velocity (γ-v) correlations using TreeCorr, applied to mock catalogs representing:
- **Shear (γ):** Weak lensing shear from LSS
- **Velocity (v):** Apparent proper motion of quasars from evolving LSS (kinematic lensing / moving lens effect)

The tutorial should be pedagogically clear, physically realistic, and include theory vs measurement comparisons.

---

## Architecture

```
pyccl (cosmology + theory)
    ↓
┌───────────────────────────────────────────────────┐
│  Power Spectra                                    │
│  C_ℓ^κκ, C_ℓ^γγ, C_ℓ^vv, C_ℓ^κv, C_ℓ^γv         │
└───────────────────────────────────────────────────┘
    ↓                           ↓
Field Generation            Theory ξ(θ)
    ↓                           ↓
TreeCorr Measurement    ←→  Comparison
```

---

## Work Packages

### WP1: Cosmology Module (pyccl)

Replace CAMB with pyccl for cleaner normalization and theory predictions.

**Deliverables:**
- `cosmology_ccl.py` replacing `cosmology.py`
- Functions:
  - `get_cosmology(config)` → pyccl.Cosmology
  - `get_convergence_power(cosmo, ell, z_source)` → C_ℓ^κκ
  - `get_shear_power(cosmo, ell, z_source)` → C_ℓ^γγ (= C_ℓ^κκ for spin-2)
  - `get_velocity_power(cosmo, ell, z_lens)` → C_ℓ^vv (transverse velocity)
  - `get_shear_velocity_cross(cosmo, ell, z_source, z_lens)` → C_ℓ^γv

**Physics notes:**
- Velocity field: α̇ = ∂α/∂t where α is deflection angle
- For single lens plane: v ∝ ℓ × velocity × potential
- Cross-correlation exists when shear source and velocity lenses overlap in redshift

**Validation:**
- Compare C_ℓ^κκ against published values (e.g., Planck 2018)
- Check σ_κ ≈ 0.02 for typical source redshift

---

### WP2: Theory Correlation Functions

Compute theoretical ξ(θ) from C_ℓ for direct comparison with TreeCorr output.

**Deliverables:**
- `theory_correlations.py`
- Functions:
  - `xi_plus_minus(cl, ell, theta)` → ξ+(θ), ξ−(θ) for spin-2 × spin-2
  - `xi_gv(cl_gv, ell, theta)` → ξ_gv(θ) for spin-2 × spin-1
  - Hankel transforms using scipy or pyccl's FFTLog

**Key equations:**
```
ξ+(θ) = ∫ (dℓ ℓ)/(2π) C_ℓ^γγ J_0(ℓθ)
ξ−(θ) = ∫ (dℓ ℓ)/(2π) C_ℓ^γγ J_4(ℓθ)
ξ_gv(θ) = ∫ (dℓ ℓ)/(2π) C_ℓ^γv [J_1(ℓθ) or J_3(ℓθ)]
```

---

### WP3: Field Generation Refactor

Refactor field generation with proper pyccl-based normalization and high-ℓ tapering.

**Deliverables:**
- Update `generate_fields_lib.py`:
  - Accept C_ℓ from pyccl directly
  - Implement Gaussian taper: `C_ℓ → C_ℓ × exp(−(ℓ/ℓ_taper)²)` where ℓ_taper ~ 0.5 × ℓ_Nyquist
  - Ensure output fields have physical amplitudes (σ_γ ~ 0.3, σ_v ~ few μas/yr)

**Fields to generate:**
1. **Lensing potential ψ** — from C_ℓ^ψψ = 4 C_ℓ^κκ / ℓ⁴
2. **Convergence κ** — κ̃ = −ℓ²ψ̃/2
3. **Shear γ** — γ̃ = −ℓ²e^{2iφ}ψ̃/2
4. **Velocity v** — ṽ = iℓe^{iφ}ψ̃ × (velocity factor)

**Validation:**
- Verify σ_κ, σ_γ match pyccl predictions
- Check B-mode is consistent with zero

---

### WP4: Catalog Generation

Create TreeCorr-compatible catalogs from fields.

**Deliverables:**
- `catalog_utils.py`
- Functions:
  - `fields_to_shear_catalog(gamma1, gamma2, box_size, n_gal=None)` → treecorr.Catalog
  - `fields_to_velocity_catalog(vx, vy, box_size, n_qso=None)` → treecorr.Catalog
  - Support for:
    - Full grid (all pixels as objects)
    - Random sampling (realistic galaxy/quasar density)
    - Shape noise injection (for realism)

**Realistic densities:**
- Shear: ~30 gal/arcmin² (LSST-like)
- Velocity: ~100 QSO/deg² (Gaia-like)

---

### WP5: Correlation Measurement

Compute all auto- and cross-correlations with TreeCorr.

**Deliverables:**
- `measure_correlations.py`
- Correlators:
  - `GGCorrelation` → ξ+(θ), ξ−(θ) for shear
  - `VVCorrelation` → velocity auto-correlation
  - `GVCorrelation` → shear-velocity cross
  - `KKCorrelation` → convergence (for validation)
- Stacking over multiple realizations for S/N

**Configuration:**
- θ_min = 0.5 arcmin
- θ_max = 300 arcmin (up to box scale)
- n_bins = 20
- bin_slop = 0.1

---

### WP6: Visualization & Comparison

Plot theory vs measurement for all correlations.

**Deliverables:**
- `plot_correlations.py`
- Plots:
  - C_ℓ comparison (input vs measured)
  - ξ(θ) comparison (theory vs TreeCorr)
  - Residuals with error bars
  - Multi-realization scatter

**Style:**
- seaborn defaults
- HUSL palette for multiple curves
- Log scales for C_ℓ and θ

---

### WP7: Tutorial Notebook

Jupyter notebook walking through the full pipeline.

**Sections:**
1. **Introduction** — Physics of shear-velocity correlations
2. **Cosmology setup** — pyccl configuration
3. **Power spectra** — Theory C_ℓ
4. **Field generation** — From C_ℓ to fields
5. **Catalog creation** — Fields to TreeCorr catalogs
6. **Correlation measurement** — TreeCorr usage
7. **Theory comparison** — Validation
8. **Noise and systematics** — Shape noise, shot noise, cosmic variance

---

## Dependencies

**Python packages:**
- pyccl (cosmology, power spectra)
- treecorr (correlation functions)
- numpy, scipy
- matplotlib, seaborn
- healpy (optional, for full-sky extension)

**Remove:**
- camb (replaced by pyccl)
- namaster (not needed for flat-sky)

---

## Open Questions

1. **Velocity definition:** Is v = ∂α/∂t the right observable for kinematic lensing? Or is it the transverse velocity of lenses weighted by lensing kernel?

2. **Redshift configuration:** Should we use:
   - Single source plane (z_s = 1) + single lens plane (z_l = 0.5)?
   - Broad redshift distributions?
   - Limber approximation validity?

3. **Cross-correlation amplitude:** The γ-v correlation exists when:
   - Same underlying matter field
   - Overlapping kernels (shear sources behind velocity lenses)
   - What's the expected S/N for realistic surveys?

4. **Multiple realizations:** How many needed for 5σ detection of γ-v?

---

## Success Criteria

1. **Theory matches measurement** for γγ auto-correlation (within cosmic variance)
2. **Physical amplitudes** — σ_γ ~ 0.3, σ_κ ~ 0.02
3. **B-mode consistent with zero** — validates pure E-mode generation
4. **γv cross-correlation detectable** with sufficient realizations
5. **Tutorial is pedagogically clear** — can be followed by grad student

---

## Files to Create/Modify

**New:**
- `calum_spin_fields/cosmology_ccl.py`
- `calum_spin_fields/theory_correlations.py`
- `calum_spin_fields/catalog_utils.py`
- `calum_spin_fields/measure_correlations.py`
- `calum_spin_fields/plot_correlations.py`
- `notebooks/shear_velocity_tutorial.ipynb`

**Modify:**
- `calum_spin_fields/generate_fields_lib.py` — pyccl integration, tapering
- `calum_spin_fields/config_lcdm.yaml` — pyccl-compatible config

**Delete:**
- `calum_spin_fields/cosmology.py` (CAMB version)
- `compute_gv_correlation.py` (superseded)

---

## Parallelization Strategy

Independent work packages:
- WP1 (pyccl cosmology) — no dependencies
- WP2 (theory ξ) — depends on WP1
- WP3 (field generation) — depends on WP1
- WP4 (catalogs) — depends on WP3
- WP5 (measurement) — depends on WP3, WP4
- WP6 (plotting) — depends on WP2, WP5
- WP7 (notebook) — depends on all

**Phase 1:** WP1 (cosmology foundation)
**Phase 2:** WP2, WP3 in parallel
**Phase 3:** WP4, WP5
**Phase 4:** WP6, WP7
