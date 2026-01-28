---
title: Field amplitudes are arbitrary - need physical normalization
status: closed
kind: task
tags:
    - '[spin-fields]'
priority: 2
depends-on:
    - fix-shear-generation-formula-in-38b67282
created-at: 2026-01-27T10:17:33.544414+01:00
closed-at: 2026-01-27T21:05:00.458994+01:00
close-reason: 'Accepted: tutorial uses arbitrary A=1, n=-5 power law. Physical normalization (e.g., from CAMB) is out of scope.'
---

Current fields have:
- γ std ~ 10^11 (arbitrary units)
- θ × ξ ~ 10^16

Real weak lensing has:
- γ std ~ 0.02-0.03
- θ × ξ ~ 10^-4 at 10'

Fix: Normalize fields to physical units
```python
sigma_target = 0.02  # typical cosmic shear
gamma1 *= sigma_target / sigma_measured
gamma2 *= sigma_target / sigma_measured
```

Or fix upstream in CAMB/power spectrum amplitude.
