---
title: Align VG implementation with main.tex analytical approach
status: closed
kind: spec
tags:
    - '[ralph]'
priority: 2
created-at: 2026-01-27T22:59:30.098787+01:00
closed-at: 2026-01-27T23:07:53.91105+01:00
close-reason: 'Fixed shear sign to -ℓ₊² (main.tex convention). Added analytical closed-form for power-law n=-5: ξ₊=CDA/(2πr), ξ₋=CDA/(6πr). Simplified sign patches to match TreeCorr after shear fix. Verified ratio ξ₊/ξ₋ ≈ 3 matches theory.'
---

## Context
The calum_spin_fields tutorial has diverged from the clean analytical approach in main.tex.

## Key Divergences to Fix

### 1. Sign conventions
- Shear: code uses +ℓ²e^{2iφ} but main.tex uses -ℓ₊²
- GV vs VG ordering: code does gv.process(cat_g, cat_v) but main.tex defines ⟨v γ*⟩
- Empirical sign patches in theory_correlations.py:394 are symptoms

### 2. Overcomplicated theory computation
main.tex approach:
- Generate fields in Fourier space, IFFT to real space
- Sample catalog, run TreeCorr → measured ξ_+, ξ_-
- Theory: analytical Hankel transform of C_vγ(ℓ)

Code approach (overcomplicated):
- discrete_correlation_2d() with explicit 2D mode sums
- Romberg integration, fast Hankel, regular Hankel (3 implementations!)
- E/B decomposition machinery in measure_power_spectra.py

### 3. Simplification opportunity
For power-law P_Φ(ℓ) = A·ℓ^{-5}:
- P_vγ(ℓ) = ℓ³·P_Φ = A·ℓ^{-2}
- ξ_+(r) = (A/2π)·(1/r)
- ξ_-(r) = (A/6π)·(1/r)

These are **analytically closed form**. No numerical integration needed.

## Deliverables
1. Fix shear sign to match main.tex: γ̃ = -ℓ₊²Φ̃
2. Use VG ordering or derive correct phase for GV
3. Remove empirical sign patches - make theory derivation match TreeCorr naturally
4. Replace discrete_correlation_2d() with analytical formulas where possible
5. Single Hankel implementation for cases that need numerical integration
