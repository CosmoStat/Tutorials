---
title: TreeCorr-style profiles over physical 1/r profiles
status: closed
kind: decision
priority: 2
depends-on:
    - gv-correlation-tutorial-scripts-58528f9c
created-at: 2026-01-28T22:47:06.820552+01:00
closed-at: 2026-01-28T22:47:06.820556+01:00
close-reason: 'Chose γ ∝ exp(-r²/2r₀²)(x+iy)²/r₀² over γ ∝ exp(-r²/2r₀²)(x+iy)²/r². TreeCorr test profiles have clean analytical Fourier transforms — correlation integrals work out nicely. Physical 1/r and 1/r² profiles require harder Hankel transform integrals. Trade-off: lose nice dipole/quadrupole visualization patterns, gain matching theory curves. For tutorial, having theory match is more valuable than visualization aesthetics.'
---
