---
title: GG/VV theory formulas from TreeCorr tests
status: closed
kind: spec
priority: 2
depends-on:
    - gv-correlation-tutorial-scripts-58528f9c
created-at: 2026-01-28T22:47:23.59414+01:00
closed-at: 2026-01-28T22:47:23.594144+01:00
close-reason: |-
    From test_gg.py and test_vv.py:

    GG ξ+(r) = (π/16) γ₀² (r₀/L)² exp(-r²/4r₀²) (r⁴ - 16r²r₀² + 32r₀⁴)/r₀⁴
    GG ξ-(r) = (π/16) γ₀² (r₀/L)² exp(-r²/4r₀²) r⁴/r₀⁴

    VV ξ+(r) = (π/4) v₀² (r₀/L)² exp(-r²/4r₀²) (4r₀² - r²)/r₀²
    VV ξ-(r) = -(π/4) v₀² (r₀/L)² exp(-r²/4r₀²) r²/r₀²

    Key insight: Different polynomial factors due to spin-2 vs spin-1 structure. GG has quartic polynomial with zero crossings at r≈1.5r₀ and r≈3.7r₀. VV has quadratic with zero crossing at r=2r₀. For N discrete halos, multiply by N.
---
