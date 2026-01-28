---
title: TreeCorr GG correlation works correctly with proper shear
status: closed
kind: decision
tags:
    - '[spin-fields]'
priority: 2
created-at: 2026-01-27T10:17:23.255002+01:00
closed-at: 2026-01-27T21:04:59.384516+01:00
close-reason: 'Confirmed: TreeCorr GG matches theory when using discrete 2D sum. Offset was cosmic variance.'
---

Verified TreeCorr GGCorrelation is not the problem.

Test with synthetic tangential shear pattern (known E-mode):
- ξ+/ξ- ~ 13 at small θ ✓
- 100% positive ✓

Test with correctly generated shear from Φ (with taper):
- ξ+/ξ- ~ 1.7 at smallest θ ✓
- Mostly positive ✓

The ξ+/ξ- << 1 behavior was entirely due to the wrong shear formula,
not TreeCorr or the power spectrum.
