---
title: Shear-velocity correlation tutorial
status: closed
kind: spec
priority: 2
created-at: 2026-01-27T11:36:55.932218+01:00
closed-at: 2026-01-27T14:51:49.78506+01:00
close-reason: 'Tutorial complete. All 6 criteria met: (1) run_tutorial.py runs end-to-end, (2) measured ξ₊ matches theory, (3) B-mode ξ₋ suppressed vs ξ₊ (0.86 ratio), (4) MCMC recovers A,n within 0.3σ, (5) GV cross measured, (6) all plots saved to output_tutorial/. Power-law demo is pedagogically sound.'
---

# Spec: Shear-Velocity Correlation Tutorial

You are in a Ralph loop — autonomous iteration toward completion.

## Skills

Before beginning, activate the following skills:

- /ralph
- /implementing-code
- /data-visualization

## Rhythm

1. **Survey** — What's done? What's incomplete? Fresh judgment.
2. **Work** — Pick highest-value task. Delegate routine work if useful (2-3 agents max, different files).
3. **Exit** — Always end with `kill $PPID`. This continues the loop.

## Exit Rules (CRITICAL)

**If you made ANY changes this iteration:** `kill $PPID`. Do NOT close the fiber. The next iteration will verify your work with fresh eyes.

**If you made ZERO changes AND found nothing to contribute:** Close fiber with `felt off <id> -r "..."`, then `kill $PPID`.

---

## Goal

Build a clean pedagogical demo: generate shear (γ) and velocity (α̇) fields from a power-law potential spectrum, measure their correlation functions with TreeCorr, and fit the power-law parameters.

## Physics

Power-law potential spectrum:

P_Φ(ℓ) = A × ℓ^n

Derived fields in harmonic space (Calum's slides):

| Field | Spin | Definition | Power Spectrum |
|-------|------|------------|----------------|
| κ (convergence) | 0 | Bℓ²Φ̃(ℓ) | C^κκ = B²ℓ⁴ P_Φ |
| α̇ (velocity) | 1 | Cℓe^{iφ}Φ̃(ℓ) | C^α̇α̇ = C²ℓ² P_Φ |
| γ (shear) | 2 | Dℓ²e^{2iφ}Φ̃(ℓ) | C^γγ = D²ℓ⁴ P_Φ |

Cross-correlation: C^{α̇γ}_ℓ = CD ℓ³ P_Φ(ℓ)

For simplicity, set B = D = 0.5, C = 1.0 (matching existing code).

## Configuration

**Fixed:**
- Amplitude factors B, C, D = 0.5, 1.0, 0.5 (could also be fit, but keep simple)

**Blind (to fit):**
- A (amplitude) — nuisance parameter, any value works. Doesn't need to be physically realistic.
- n (spectral index) — the physics

Box size and grid are simulation details — they set ℓ_min and ℓ_max but don't affect the power law form.

**Simplicity principle:** Keep the demo pedagogical. Amplitude normalization is arbitrary — focus on recovering n correctly.

## Design

### 1. Power Spectrum

`calum_spin_fields/power_spectrum.py`:
- `power_law_spectrum(ell, amplitude, index)` → P_Φ(ℓ) = A × ℓ^n
- No tapering — theory and measurement use same ℓ range (up to Nyquist)

### 2. Field Generation

Use existing `calum_spin_fields/generate_fields_lib.py`:
- Already handles Hermitian symmetry correctly
- Already derives κ, α̇, γ from Φ with correct spin factors
- ℓ_max = π × N / θ_box (Nyquist) — same cutoff in theory integral

### 3. Theory Correlation Functions

`calum_spin_fields/theory_correlations.py`:
- Hankel transforms: ξ(θ) = ∫ (dℓ ℓ)/(2π) C_ℓ J_n(ℓθ)
- For spin-2 × spin-2: ξ₊ uses J_0, ξ₋ uses J_4
- For spin-1 × spin-2 (GV): uses J_1 and J_3
- Use scipy.integrate.quad or FFTLog

### 4. Measurement

`calum_spin_fields/measure_correlations.py`:
- Load fields from .npy files
- Create TreeCorr catalogs (full grid as objects)
- Compute:
  - `GGCorrelation` → ξ₊(θ), ξ₋(θ) for shear
  - `VVCorrelation` → velocity auto
  - `GVCorrelation` → shear-velocity cross
- Return theta bins and correlation values

### 5. Fitting

`calum_spin_fields/fit_power_law.py`:
- Theory prediction: C_ℓ^γγ(A, n) → ξ₊(θ; A, n) via Hankel
- Log-likelihood: χ² between measured and theory ξ₊(θ)
- Fit using scipy.optimize or emcee
- Recover (A, n)

### 6. Main Script

`calum_spin_fields/run_tutorial.py`:
- Generate fields with true (A, n)
- Measure correlation functions
- Fit and recover parameters
- Plot: theory vs measurement, residuals

## Context

Existing files:
- `calum_spin_fields/generate_fields_lib.py` — field generation (correct)
- `calum_spin_fields/power_spectrum.py` — power-law spectrum functions (created)
- `calum_spin_fields/theory_correlations.py` — Hankel transforms with scipy (no pyccl)
- `calum_spin_fields/fit_power_law.py` — fitting with scipy.optimize + emcee
- `calum_spin_fields/measure_correlations.py` — TreeCorr measurement
- `calum_spin_fields/run_tutorial.py` — main script

Cleaned up (removed):
- `cosmology_ccl.py`, `cosmology.py`, `fit_cosmology.py` — pyccl-based code, not needed for power-law demo

Felt fibers:
- `fix-shear-generation-formula-in-38b67282` — shear formula is correct in generate_fields_lib.py
- `treecorr-gg-correlation-works-d7b5a1d1` — TreeCorr validated

## Completion

The system is complete when:

1. `python run_tutorial.py` executes end-to-end without error
2. Measured ξ₊(θ) matches theory prediction (same A, n)
3. B-mode ξ₋ is suppressed relative to ξ₊ (pure E-mode check)
4. Fit recovers true (A, n) within uncertainty
5. GV cross-correlation is measured (may be noisy for single realization)
6. Plots exist: C_ℓ input, ξ(θ) theory vs measured, fit results
