---
title: GV (shear-velocity) correlation is noise-dominated for single realizations
status: closed
kind: decision
tags:
    - '[spin-fields]'
priority: 2
created-at: 2026-01-27T10:17:11.647196+01:00
closed-at: 2026-01-27T21:04:57.727546+01:00
close-reason: 'Confirmed: GV cross-correlation has high cosmic variance for steep spectra. Single realizations are noisy but ensemble mean is correct.'
---

Tested TreeCorr GVCorrelation on the LCDM fields.

Finding: The measured ξ_gv oscillates 50/50 positive/negative — pure noise.

Reasons:
1. Cross-correlations have lower S/N than auto-correlations
2. Single 50° realization has large cosmic variance
3. The correlation exists in expectation but variance >> signal

Theory prediction shows ξ+ should be consistently positive for gradient-derived fields,
but single realization can't detect this.

Would need: many realizations, or much larger field, or cross-survey correlation.
