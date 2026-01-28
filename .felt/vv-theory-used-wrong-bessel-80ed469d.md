---
title: VV theory used wrong Bessel function formula
status: closed
kind: decision
priority: 2
created-at: 2026-01-27T16:16:10.734559+01:00
closed-at: 2026-01-27T16:16:10.734562+01:00
close-reason: Fixed xi_velocity_theory in theory_correlations.py. Was using (J0+J2)/2 for ξ₊ and (J0-J2)/2 for ξ₋, but TreeCorr VVCorrelation computes ξ₊ = ⟨v v*⟩ (spin-0, uses J₀ directly) and ξ₋ = ⟨v v⟩ (spin-2, uses J₂ directly). The factor of 2 error explained half the original 2.6× discrepancy.
---
