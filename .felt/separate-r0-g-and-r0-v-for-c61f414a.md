---
title: Separate R0_G and R0_V for different correlation lengths
status: closed
kind: spec
priority: 2
depends-on:
    - gv-correlation-tutorial-scripts-58528f9c
created-at: 2026-01-28T22:47:36.115155+01:00
closed-at: 2026-01-28T22:47:36.115163+01:00
close-reason: 'Can use different scale radii for shear vs velocity to mimic physical 1/r² vs 1/r behavior. R0_V > R0_G gives longer-range velocity correlations. With R0_G=10, R0_V=30: VV extends to ~3x larger scales than GG, with ~10x higher amplitude. Theory formulas just substitute the appropriate R0. Implemented but reverted to R0_G=R0_V=10 for cleaner tutorial visualization.'
---
