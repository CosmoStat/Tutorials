---
title: Multi-halo GV correlation test
status: closed
kind: task
priority: 2
depends-on:
    - gv-correlation-tutorial-scripts-58528f9c
created-at: 2026-01-28T19:44:05.129129+01:00
closed-at: 2026-01-28T19:49:30.664272+01:00
close-reason: 'Implemented generate_gv_halos.py following test_kv pattern: 1000 lenses, 50000 sources, Gaussian profiles. NG/NV match theory (γ0=v0=0.05, r0=10). GV shows non-trivial ξ+/ξ- signal. Field visualization shows velocity vectors, shear sticks, spin-1/2 components.'
---

## Goal
Implement test_kv-style multi-halo approach for GV correlation.

## Design
- Scatter N_HALO (~100-1000) halos randomly in box
- Each halo contributes:
  - Tangential shear: γ_t = γ₀ exp(-r²/2r₀²)
  - Radial velocity: v_r = v₀ exp(-r²/2r₀²)
- Sum contributions at each source position
- Measure GV correlation (stacks around all halos)

## Deliverables
1. generate_gv_halos.py script
2. Field visualization (like point mass case):
   - Net velocity vectors
   - Net shear sticks
   - v1, v2, g1, g2 components
   - Halo positions marked
3. Correlation plot (GG, VV, GV)

## Key difference from single-center
- Many random centers → statistically meaningful ξ(r)
- Stacking like real galaxy-galaxy lensing measurements
- r is separation from ANY halo, averaged over all halos
