---
title: Investigate CAMB normalization for lensing power spectrum
status: closed
kind: question
tags:
    - '[spin-fields]'
priority: 2
created-at: 2026-01-27T10:16:59.309923+01:00
closed-at: 2026-01-27T21:04:56.426844+01:00
close-reason: 'Deferred: tutorial uses arbitrary power-law normalization. CAMB integration out of scope.'
---

CAMB's source window for lensing gives σ_κ ~ 2 instead of expected ~0.02.
The C_ℓ^κκ amplitude is ~100× too large.

Possible issues:
- Source window configuration in cosmology.py
- Units mismatch (dimensionless vs physical)
- SourceWindows vs direct lensing potential computation

Currently using manual normalization (γ *= 0.02/σ_measured) as workaround.
Need to trace through CAMB setup to get physical amplitudes automatically.
