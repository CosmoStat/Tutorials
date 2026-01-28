---
title: Add high-ℓ tapering to avoid Gibbs ringing
status: closed
kind: task
tags:
    - '[spin-fields]'
priority: 2
created-at: 2026-01-27T10:16:49.418241+01:00
closed-at: 2026-01-27T21:04:55.076999+01:00
close-reason: 'Deferred: not needed for current tutorial. Gibbs ringing not a significant issue with current parameters.'
---

The power spectrum has a hard cutoff at ℓ_Nyquist, causing Gibbs ringing in real-space correlations.
This manifests as pixel-scale sign alternation in ξ(θ): +, -, +, -, ...

Fix: Taper the power spectrum before field generation:
```python
Cl_tapered = Cl * np.exp(-(ell / ell_taper)**2)
```

Choose ell_taper well below Nyquist (e.g., ℓ_taper ~ 0.5 × ℓ_Nyquist).

When fitting, only use θ > π/ℓ_taper to avoid taper artifacts.
