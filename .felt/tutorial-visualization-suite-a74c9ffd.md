---
title: Tutorial visualization suite
status: active
kind: spec
priority: 2
created-at: 2026-01-27T20:07:35.461263+01:00
---

# Goal

Create polished publication-quality figures for the spin fields tutorial.

## Figures to Create

### 1. `fields.png` — Field visualization (4 panels)
- Panel 1: φ (gravitational potential) — colormap
- Panel 2: α (velocity) — quiver or colormap of |α|
- Panel 3: κ (convergence) — colormap
- Panel 4: γ (shear) — whisker plot or colormap of |γ|

### 2. `phi_with_velocity.png` — Potential with velocity vectors
- Background: φ field colormap
- Overlay: α (velocity) as quiver/arrow field
- Rebin velocity field (average over NxN blocks) for cleaner arrows, not just subsample

### 3. `correlation_functions.png` — All correlations (3×2 grid)
```
         ξ₊           ξ₋
   ┌──────────┬──────────┐
GG │ measured │ measured │
   │ + theory │ + theory │
   ├──────────┼──────────┤
VV │ measured │ measured │
   │ + theory │ + theory │
   ├──────────┼──────────┤
GV │ ξ_t      │ ξ_x      │
   │ + theory │ + theory │
   └──────────┴──────────┘
```
- Error bars on measured points
- Theory as solid line
- Log scale on θ axis

### 4. `mcmc_fit.png` — Best-fit comparison
- Joint fit to all three data vectors: GG, VV, GV
- Show data with error bars for each correlation
- Overplot best-fit theory curves
- Include residuals panel below each
- 3×2 layout matching correlation_functions.png

### 5. `mcmc_corner.png` — Parameter posteriors
- Corner plot of MCMC chains
- Parameters: amplitude A, index n
- Show 1σ/2σ contours
- Mark true values if known

## Design Guidelines

- Use seaborn style
- Consistent colormap (mako for sequential)
- Font sizes readable at paper width
- Save at 150 DPI minimum
- No emojis

## Output

All figures to `output_tutorial/`

## Context

- Field generation: `generate_fields_lib.py`
- Correlation measurement: `measure_correlations.py`  
- Theory: `theory_correlations.py` (uses discrete 2D sum)
- MCMC fitting: needs to be written or exists in `fit_correlations.py`

## Completion

All 5 figures generated and saved. Visually inspect each.

## Comments
**2026-01-29 01:25** — Session progress: Created 3 diagrams via nano-banana - chatbot vs agent, model harness (text boxes + car), workflow (warm colors with loop). All added to codelab and committed.

