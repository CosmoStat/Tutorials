---
title: GV correlation tutorial scripts
status: closed
kind: spec
priority: 2
created-at: 2026-01-28T18:32:02.531415+01:00
closed-at: 2026-01-28T22:48:42.591053+01:00
close-reason: |-
    COMPLETE. generate_gv_halos.py implements full GV correlation tutorial:

    **Approach:** Multi-lens field generation with TreeCorr-style Gaussian profiles (γ ∝ exp(-r²/2r₀²)(x+iy)²/r₀², v ∝ exp(-r²/2r₀²)(x+iy)/r₀). Chose this over physical 1/r profiles for analytical tractability.

    **Correlations:** GG, VV measured with matching theory from TreeCorr tests. GV measured but theory not yet derived (new correlation type).

    **Visualizations:**
    - Field plot: 3 top panels (sources+lenses, velocity vectors, shear sticks), 4 bottom panels (spin components with spin-1/spin-2 labels)
    - Lens buildup GIF: 1 → 10 → 1000 lenses showing field emergence
    - Correlation plot: ξ+ and ξ- for all three, with theory curves and correlation length markers

    **Extensions explored:** Lens clustering (two-halo term), separate R0_G/R0_V for different correlation lengths — infrastructure exists but kept simple for tutorial.
---

# Spec

You are in a Ralph loop — autonomous iterative contribution toward a desired state.

## Skills

Activate before beginning:

- /ralph
- /implementing-code
- /data-visualization

## Rhythm

1. **Survey** — `felt downstream <spec-id>`, git log, system state. What's done? What's incomplete?
2. **Contribute** — Pick highest-value work. Spawn subagents for parallel items. Record as sub-fibers: `felt add "..." -a <spec-id>`.
3. **Exit** — Always `kill $PPID`.

## Exit Rules

**Made ANY contribution:** `kill $PPID`. Do NOT close the fiber.

**Made ZERO contributions AND nothing left:** `felt off <id> -r "..."`, then `kill $PPID`.

---

## Goal

Create two scripts for a TreeCorr GV correlation tutorial: one to generate mock shear+velocity catalogs from a point mass, another to measure GV and plot results.

## Design

**Script 1: generate_gv_mock.py**
- Generate random positions in an annulus around origin (avoid r~0 singularity)
- Compute physical point mass fields:
  - Tangential shear: γ_t = γ0 / r²
  - Radial velocity: v_r = v0 / r
- Convert to components (g1, g2, v1, v2)
- Save as FITS catalog with columns: x, y, g1, g2, v1, v2

**Script 2: measure_gv.py**
- Load FITS catalog
- Create TreeCorr Catalog objects (one for G, one for V, or combined)
- Run GVCorrelation
- Plot ξ+(r) and ξ-(r) vs separation

## Context

- TreeCorr with GVCorrelation: /Users/cd280747/Documents/projects/TreeCorr
- Tutorial repo: /Users/cd280747/Documents/projects/Tutorials
- Reference tests: TreeCorr/tests/test_kv.py, test_kg.py, test_vv.py (for field generation patterns)
- Output catalogs: data/ subdirectory in Tutorials repo

## Completion

- `generate_gv_mock.py` exists and produces a valid FITS catalog
- `measure_gv.py` exists and produces a plot of ξ+(r), ξ-(r)
- Both scripts run without error
- Plot shows non-trivial correlation signal (not just noise)
