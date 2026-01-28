---
title: 'Fix GV cross-correlation: measured is zero'
status: closed
kind: task
priority: 2
created-at: 2026-01-27T14:55:12.598448+01:00
closed-at: 2026-01-27T15:20:15.659301+01:00
close-reason: 'Fixed GV cross-correlation. Root cause: velocity field missing factor of i in gradient definition (∇Φ = i·k·Φ̃). Added -1j multiplier in generate_vector_field(). Also fixed measure_gv_correlation() to use TreeCorr''s GVCorrelation with proper v1/v2 fields. Measured ξ_GV now matches theory at ~0.08.'
---

# Fix GV Cross-Correlation

You are in a Ralph loop — autonomous iteration toward completion.

## Skills

- /ralph
- /implementing-code

## Rhythm

1. **Survey** — What's done? What's incomplete? Fresh judgment.
2. **Work** — Pick highest-value task. Delegate routine work if useful (2-3 agents max, different files).
3. **Exit** — Always end with `kill $PPID`. This continues the loop.

## Exit Rules (CRITICAL)

**If you made ANY changes this iteration:** `kill $PPID`. Do NOT close the fiber. The next iteration will verify your work with fresh eyes.

**If you made ZERO changes AND found nothing to contribute:** Close fiber with `felt off <id> -r "..."`, then `kill $PPID`.

---

## Problem

The GV (shear × velocity) cross-correlation measurement is flat at zero with no scatter, while theory predicts ξ_GV ~ 0.07. This isn't noise — it's a bug.

If γ and α̇ are both derived from the same potential Φ, they must be correlated. Zero signal means something is broken.

## Hypotheses

1. **Fields not correlated**: γ and α̇ generated from different random seeds / independent Φ realizations
2. **TreeCorr GVCorrelation misuse**: Wrong catalog setup, wrong field assignments (v1/v2 vs g1/g2)
3. **Sign or phase error**: α̇ has wrong sign convention relative to γ
4. **Amplitude bug**: Fields have correct shape but wrong scale, making cross-correlation negligible
5. **Theory prediction wrong**: Hankel transform for GV uses wrong Bessel function order

## Diagnostic Steps

### Step 1: Verify fields are from same Φ

Check `generate_fields_lib.py` and `run_tutorial.py`:
- Is the same `phi_fourier` used for both γ and α̇?
- Are they generated in the same call, or separate calls with different RNG states?

### Step 2: Check TreeCorr catalog setup

In `measure_correlations.py`:
- Shear catalog: `g1=gamma1, g2=gamma2`
- Velocity catalog: `v1=vx, v2=vy`
- Are the sign conventions consistent?

TreeCorr GVCorrelation expects:
- g1, g2 for shear (spin-2)
- v1, v2 for velocity (spin-1)

### Step 3: Verify cross-correlation in Fourier space

Before TreeCorr, compute the cross-power spectrum directly:
```python
# If fields are correlated, this should be non-zero
cross_power = np.real(gamma_fft * np.conj(v_fft))
```

### Step 4: Check theory prediction

The GV correlation function involves J_1 and J_3 Bessel functions (spin-2 × spin-1 = spin-1 and spin-3 components). Verify `theory_correlations.py` uses correct formulas.

### Step 5: Simple sanity check

Create synthetic perfectly correlated fields:
- v = γ (same field, treated as both)
- Measure GV correlation — should be non-zero

## Files to Check

- `calum_spin_fields/generate_fields_lib.py` — field generation
- `calum_spin_fields/run_tutorial.py` — orchestration
- `calum_spin_fields/measure_correlations.py` — TreeCorr usage
- `calum_spin_fields/theory_correlations.py` — Hankel transforms

## Completion

The fix is complete when:

1. Root cause identified and documented
2. GV cross-correlation shows non-zero signal matching theory (within cosmic variance)
3. `run_tutorial.py` produces a GV plot where measured points follow the theory curve
