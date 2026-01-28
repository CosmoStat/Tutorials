---
title: GV correlation tutorial complete
status: closed
kind: task
priority: 2
depends-on:
    - gv-correlation-tutorial-scripts-58528f9c
created-at: 2026-01-28T22:48:09.920738+01:00
closed-at: 2026-01-28T22:48:09.920742+01:00
close-reason: |-
    generate_gv_halos.py produces:
    - Multi-lens shear+velocity fields (TreeCorr-style Gaussian profiles)
    - GG, VV, GV correlation measurements with TreeCorr
    - Theory curves matching GG and VV (GV theory not yet derived)
    - Field visualization: 3 panels top (sources+lenses, velocity vectors, shear sticks), 4 panels bottom (v1, v2, γ1, γ2 with spin-1/spin-2 labels)
    - Lens buildup GIF: 1 → 10 → 1000 lenses
    - Correlation length markers on plots
    - Black dot markers for lenses throughout

    All completion criteria met. Scripts run without error, plots show non-trivial signal.
---
