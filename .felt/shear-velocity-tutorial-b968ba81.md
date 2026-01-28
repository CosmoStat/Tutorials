---
title: Shear-velocity tutorial redesign spec
status: closed
kind: spec
tags:
    - '[tutorial]'
priority: 2
created-at: 2026-01-27T11:28:04.365089+01:00
closed-at: 2026-01-27T19:55:56.26295+01:00
close-reason: 'Root cause identified: Hankel integral fails for steep spectra due to discrete mode structure. Fixed by implementing discrete 2D sum: ξ(θ) = (1/L²) Σ_k C_ℓ(k) J_n(ℓθ). The ~8% offset for seed=42 is cosmic variance (mean across seeds = 1.04 ± 0.22). Updated theory_correlations.py with discrete_correlation_2d() and modified get_theory_correlations() to use it.'
---
