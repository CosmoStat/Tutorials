---
title: 'Debug GG theory: spin-2 rotation formula'
status: closed
kind: task
priority: 2
depends-on:
    - real-space-correlated-field-50b252b1
created-at: 2026-01-28T14:12:16.814986+01:00
closed-at: 2026-01-28T14:25:44.905078+01:00
close-reason: "SOLVED: Issue was anisotropic field generation, NOT spin-2 rotation theory.\n\nRoot cause: Circulant embedding noise wasn't Hermitian-symmetric → anisotropic φ field → γ₁/γ₂ ratio of 25:1 instead of 1:1.\n\nFix: Replaced circulant embedding with direct FFT method using proper Hermitian noise:\n- Generate complex Gaussian noise\n- Enforce φ̃[-k] = φ̃[k]* symmetry explicitly  \n- Scale by sqrt(P(k)) and IFFT\n\nResult: Both VV and GG now match theory perfectly with no normalization factor. The existing xi_shear_plus() theory was correct all along — it's the standard ⟨γ₁γ₁'⟩ + ⟨γ₂γ₂'⟩ = ξ₊ for spin-2 fields."
---

TreeCorr GG ξ₊ doesn't match theory because of spin-2 rotation.

## Problem
- Direct ⟨γ₁γ₁'⟩ + ⟨γ₂γ₂'⟩ matches theory (oscillates, goes negative)
- TreeCorr ξ₊ (with tangential/cross rotation) stays positive
- My derived formula for rotated ξ₊ still shows oscillation

## Key equations
γ_t = -γ₁ cos(2φ) - γ₂ sin(2φ)
γ_× = +γ₁ sin(2φ) - γ₂ cos(2φ)

ξ₊ = ⟨γ_t γ_t'⟩ + ⟨γ_× γ_×'⟩ averaged over pair angles φ

## What to investigate
1. Verify the rotation formula is correct
2. Check how correlations transform under rotation
3. Compare with standard weak lensing ξ₊ derivations (Schneider et al.)
4. Possibly: the finite-difference shear has different properties than continuous

## Files
- derive_gg_theory.py: symbolic derivation attempt
- data/gg_rotation_comparison.png: shows discrepancy
