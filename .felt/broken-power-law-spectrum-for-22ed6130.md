---
title: Broken power law spectrum for IR convergence
status: closed
kind: spec
priority: 2
created-at: 2026-01-28T01:22:59.584644+01:00
closed-at: 2026-01-28T01:24:13.183489+01:00
close-reason: Merged into simplify-theory fiber
---

# Goal

Replace pure power-law P_Φ(ℓ) = A ℓ^n with a broken power law that flattens at low ℓ,
eliminating IR divergence in Hankel transforms and removing the need for box_size_deg
in theory predictions.

# Background

For steep power laws (n=-5), some Hankel integrals diverge at ℓ→0:
- VV ξ+ (J_0): α=-3, n=0 → α+n+2 = -1 < 0 → **diverges**
- All others converge

Currently we regularize by setting ℓ_min = 2π/box_size, but this:
- Couples theory to simulation parameters
- Makes VV ξ+ artificially constant instead of showing physical behavior
- Requires passing box_size_deg to get_theory_correlations()

# Design

## Broken power law form

```python
P_Φ(ℓ) = A * ℓ^n / (1 + (ℓ_0/ℓ)^2)
```

Behavior:
- ℓ >> ℓ_0: P_Φ → A ℓ^n (unchanged)
- ℓ << ℓ_0: P_Φ → A ℓ_0^{-2} ℓ^{n+2} (flattened, 2 powers shallower)

For n=-5: low-ℓ behavior becomes ℓ^{-3} instead of ℓ^{-5}

The transition scale ℓ_0 becomes a physical parameter (could be related to
horizon scale, or just set to ~10 for numerical convenience).

## Changes needed

1. **power_spectrum.py**: Add `ell_0` parameter to all spectrum functions
   ```python
   def potential_power_spectrum(ell, amplitude, index, ell_0=10):
       return amplitude * ell**index / (1 + (ell_0/ell)**2)
   ```

2. **theory_correlations.py**: 
   - Remove `box_size_deg` parameter
   - Set `ell_min` to small value (e.g., 0.1) since integrals now converge
   - Update docstring

3. **run_tutorial.py**: Remove `box_size_deg=BOX_SIZE_DEG` from theory calls

4. **generate_fields_lib.py**: Use broken power law in field generation too
   (for consistency between simulation and theory)

## Fitting implications

The fitter would fit for (A, n) as before. ℓ_0 could be:
- Fixed (simplest)
- A third fit parameter (if data constrains it)

For the tutorial, fix ℓ_0 = 10 (or similar).

# Verification

1. All Hankel integrals converge with ell_min → 0
2. VV ξ+ now shows physical θ-dependence (not artificially constant)
3. GG, GV still show expected scaling at θ << 1/ℓ_0
4. Theory matches TreeCorr measurements without box_size tuning
5. Tutorial runs and produces sensible fits

# Context files

- calum_spin_fields/power_spectrum.py
- calum_spin_fields/theory_correlations.py
- calum_spin_fields/generate_fields_lib.py
- calum_spin_fields/run_tutorial.py
