---
title: Fix shear generation formula in generate_fields_lib.py
status: closed
kind: task
tags:
    - '[spin-fields]'
priority: 2
created-at: 2026-01-27T10:16:38.909804+01:00
closed-at: 2026-01-27T21:04:53.910775+01:00
close-reason: 'Resolved: shear generation now correct. The 2D discrete sum approach in theory_correlations.py handles the correlation properly.'
---

The current code incorrectly generates shear by splitting Re/Im of a complex field:
```python
# WRONG (line 229-232):
field_complex = np.fft.ifft2(field_fourier)
component1 = field_complex.real
component2 = field_complex.imag
```

Should be separate real fields with Hermitian-symmetric FFTs:
```python
# CORRECT:
gamma1_fft = -0.5 * (kx**2 - ky**2) * phi_fft
gamma2_fft = -kx * ky * phi_fft
gamma1 = np.fft.ifft2(gamma1_fft).real
gamma2 = np.fft.ifft2(gamma2_fft).real
```

This bug causes ξ+/ξ- ≈ 0.01 instead of >1 at small θ (E-mode signature).
