---
title: 'Simplify theory: smooth numerical Hankel for ξ_± comparison'
status: closed
kind: spec
tags:
    - '[ralph]'
priority: 2
created-at: 2026-01-27T23:13:09.771047+01:00
closed-at: 2026-01-28T02:00:34.005406+01:00
close-reason: |-
    Implemented broken power law P_Φ(ℓ) = A ℓ^n / (1 + (ℓ₀/ℓ)²). Changes:
    - power_spectrum.py: All functions now accept ell_0 parameter (default 10)
    - generate_fields_lib.py: Uses broken power law for field generation
    - theory_correlations.py: Removed box_size_deg, added ell_0; ell_min→0.5 since IR converges naturally
    - run_tutorial.py: Uses ELL_0=10 instead of box_size coupling
    - fit_power_law.py: All fit functions accept ell_0 (fixed, not fitted)

    VV ξ+ now shows physical θ-dependence instead of artificial constant. All Hankel integrals converge naturally.
---

# Goal

Clean theory correlation functions via numerical Hankel transforms, with proper
handling of IR divergence through a broken power law spectrum.

# Current State (as of 2026-01-28)

## What's done

1. **`theory_correlations.py`** has clean `hankel_xi()` function using direct
   trapezoid integration over dense linear-spaced ℓ
2. **`get_theory_correlations()`** computes all 6 correlation functions (GG±, VV±, GV±)
3. **`box_size_deg`** parameter added to set IR cutoff ℓ_min = 2π/L
4. **`run_tutorial.py`** updated: 4096² pixels, 50° box, θ = 1'-50'

## IR divergence issue discovered

For power-law C_ℓ ∝ ℓ^α, convergence requires α + n + 2 > 0 (n = Bessel order).

| Correlation | α | n | α+n+2 | Status |
|-------------|---|---|-------|--------|
| GG ξ± | -1 | 0,4 | +1,+5 | ✓ converges, ξ ∝ 1/θ |
| VV ξ+ | -3 | 0 | **-1** | **✗ IR diverges** |
| VV ξ- | -3 | 2 | +1 | ✓ converges, ξ ∝ θ |
| GV ξ± | -2 | 1,3 | +1,+3 | ✓ converges, ξ = const |

VV ξ+ diverges at ℓ→0. Currently regularized by ℓ_min cutoff, but this:
- Couples theory to box_size parameter (ugly)
- Makes VV ξ+ artificially constant instead of physical behavior

## main.tex correction

The GV analytical result was wrong. For C_ℓ ∝ ℓ^{-2}:
- **Incorrect**: ξ(θ) ∝ 1/θ
- **Correct**: ξ(θ) = const (θ-independent)

The substitution in eq. 79-81 had an error. main.tex has been updated.

# Next Steps: Broken Power Law

## Design

Replace pure power law with broken form that flattens at low ℓ:

```python
P_Φ(ℓ) = A * ℓ^n / (1 + (ℓ_0/ℓ)^2)
```

Behavior:
- ℓ >> ℓ_0: P_Φ → A ℓ^n (unchanged high-ℓ)
- ℓ << ℓ_0: P_Φ → A ℓ_0^{-2} ℓ^{n+2} (2 powers shallower)

For n=-5: low-ℓ becomes ℓ^{-3}, making VV ξ+ (α=-3+2=-1, n=0) → α+n+2 = +1 > 0 ✓

## Changes needed

1. **power_spectrum.py**: Add `ell_0` parameter (default ~10)
   ```python
   def potential_power_spectrum(ell, amplitude, index, ell_0=10):
       return amplitude * ell**index / (1 + (ell_0/ell)**2)
   ```
   Update all derived spectra (shear, velocity, convergence, cross).

2. **generate_fields_lib.py**: Use broken power law in field generation
   for consistency between simulation and theory.

3. **theory_correlations.py**:
   - Remove `box_size_deg` parameter
   - Set `ell_min` to small value (~0.1) since integrals now converge
   - Pass `ell_0` through to power spectrum functions

4. **run_tutorial.py**:
   - Remove `box_size_deg` from theory calls
   - Add `ell_0` to config (fixed, not fitted)

5. **fit_power_law.py**: Fit (A, n) with fixed ell_0, or optionally fit ell_0 too.

## Sign conventions (still to verify)

Code has empirical sign flips for VV ξ- and GV ξ-. These may be:
- TreeCorr phase conventions
- Or actual physics

Need to compare raw Hankel output to TreeCorr measurements to determine.
For now, keep the flips with documentation.

# Completion criteria

1. All Hankel integrals converge naturally (no ℓ_min hack)
2. `get_theory_correlations()` has no box_size parameter
3. VV ξ+ shows physical θ-dependence (not artificially constant)
4. Theory matches TreeCorr within cosmic variance
5. Tutorial runs end-to-end with sensible MCMC fits

# Context files

- calum_spin_fields/power_spectrum.py
- calum_spin_fields/theory_correlations.py
- calum_spin_fields/generate_fields_lib.py
- calum_spin_fields/run_tutorial.py
- calum_spin_fields/fit_power_law.py
- calum_spin_fields/main.tex
