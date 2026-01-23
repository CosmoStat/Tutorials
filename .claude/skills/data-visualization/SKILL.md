---
name: data-visualization
description: >
  Create data visualizations, design figures, and plot analysis results.
  Specialized for observational cosmology (spectra, covariances, posteriors, sky maps)
  but capable of creative/expressive output for outreach.
  Use when: plotting data, designing figures for papers/talks, visualizing uncertainty,
  creating publication-quality graphics, or any task involving matplotlib/seaborn/plotly.
---

# Data Visualization

A decision framework for translating data into effective visual form. Synthesizes Bertin, Cleveland, Tufte, Cairo, Wilke, and Knaflic—optimized for scientific work with cosmology-specific conventions.

## The Intake Protocol

Before plotting, establish two dimensions:

### 1. Data Structure Analysis

Identify what you're visualizing:

| Data Type | Description | Likely Forms |
|-----------|-------------|--------------|
| **Amounts** | Values across categories | Bar, dot plot, heatmap |
| **Distributions** | Spread/shape of values | Histogram, KDE, violin, ridgeline |
| **X-Y Relationships** | Continuous variables | Scatter, line, confidence bands |
| **Uncertainty** | Error on measurements | Error bars, bands, gradient ribbons |
| **Proportions** | Parts of whole | Stacked bar, pie (rarely) |
| **Spatial/Maps** | Geographic or sky data | Mollweide, healpix, choropleth |
| **Correlations** | Variable relationships | Covariance matrix, triangle plot |

### 2. Communication Mode

Determine the venue—this switches the entire rule set:

**Mode A: Analytical/Paper**
- Audience: Expert peers, reviewers
- Optimize for: Precision, black/white printing, convention
- Philosophy: Tufte/Cleveland/Wilke—density is permitted, accuracy is paramount
- Color: Restrained, colorblind-safe, grayscale-compatible
- Default: This mode unless otherwise specified

**Mode B: Presentation/Outreach**
- Audience: Mixed expertise, attention-competitive
- Optimize for: Impact, engagement, narrative clarity
- Philosophy: Cairo/McCandless/Knaflic—preattentive pop, visual hierarchy
- Color: Bold accent colors, clear entry points
- Use when: Talks, posters, press releases, social media

## The Decision Framework

Route from data to visualization form:

### Step 1: Analyze Variables (Bertin)

For each variable, classify:
- **Quantitative**: Continuous numeric (position, intensity, redshift)
- **Ordered**: Categorical with sequence (low/med/high, redshift bins)
- **Categorical**: Nominal groups (experiments, instruments, sky regions)

Check for uncertainty: Is there error on mean (discrete bars) or intrinsic spread (continuous band)?

### Step 2: Select Encoding (Cleveland)

Match importance to perceptual accuracy:

| Rank | Encoding | Use For |
|------|----------|---------|
| 1 | Position on common scale | Primary comparisons, precise values |
| 2 | Position on non-aligned scales | Secondary comparisons |
| 3 | Length | Bar charts (amounts only) |
| 4 | Angle/Slope | Avoid for precise reading |
| 5 | Area | Gestalt impressions, bubble charts |
| 6 | Color saturation | Tertiary encoding, density |

**Rule**: If precise comparison is needed, use position. If gestalt impression is needed, use color/area.

### Step 3: Select Form (Wilke)

Consult [viz-catalog.md](references/viz-catalog.md) for the specific form. Key mappings:

| You Have | Consider |
|----------|----------|
| Spectrum (continuous x, continuous y, uncertainty) | Line + confidence band, residual subplot |
| Correlation/covariance matrix | Heatmap, diverging colormap, white at zero |
| Parameter posteriors | Triangle plot, ridgeline, violin |
| Comparison across groups | Small multiples > overlay when groups > 4 |
| Time series | Line, banking to 45° |
| Amounts across categories | Dot plot (Cleveland) > bar chart |

### Step 4: Apply Mode-Specific Rules

**If Mode A (Paper)**:
- Enforce strict linear/log scaling
- No bubble charts for precise quantities
- No dual y-axes
- Redundant encoding (shape + color) for colorblind safety
- Direct labeling over legends when ≤4 series
- Light grid lines, subordinate to data

**If Mode B (Outreach)**:
- Establish visual hierarchy—most important data most salient
- One clear entry point (where does eye go first?)
- Bolder colors, but maintain accuracy
- Annotations that guide reading
- Title states the takeaway, not the topic

## Cosmology-Specific Overrides

These conventions override general principles for domain consistency:

### Power Spectra
- **Flatten steeply falling spectra**: Multiply by x-axis factor to reveal percent-level features
  - Angular: Plot $\ell^n C_\ell$ (commonly $D_\ell = \ell(\ell+1)C_\ell/2\pi$, but factor varies)
  - Matter: Plot $k^3 P(k)$ or $\Delta^2(k)$ to flatten
  - Correlation functions: Plot $\theta \xi(\theta)$ or similar
- **Log-linear preferred**: Log scale on x (multipole/k), linear on y after flattening
  - Reveals small differences hidden by log-log compression
  - Reserve log-log only when dynamic range is the message
- **Label x-axis with actual values** (10, 100, 1000), not exponents
- **Residual panel**: Show (data - model)/σ or data/model below main panel
- **Uncertainty**: Confidence bands if dense sampling, error bars if sparse

### Covariance Matrices
- **Diverging colormap required** (RdBu, coolwarm)
- **White/neutral at zero** (or at 1 for correlation matrices)
- **Explicit colorbar** with position-based lookup for precise values
- **Consider**: Showing only upper/lower triangle for symmetry

### Triangle/Corner Plots
- **Standard layout**: 1D posteriors on diagonal, 2D contours off-diagonal
- **Contour levels**: 68%, 95% (1σ, 2σ)
- **Consistent axis ranges** across all panels showing same parameter
- **Direct parameter labels** on axes, not legend

### Sky Maps (Healpix/Mollweide)
- **Projection matters**: Mollweide for full-sky, orthographic for regions
- **Graticule**: RA/Dec grid, labeled at edges
- **Sequential colormap** for intensity, diverging for residuals

### Error Representation
- **Asymmetric errors**: Make asymmetry visually obvious
- **Bands vs bars**: Use bands for continuous functions, bars for discrete points
- **Multiple σ levels**: Gradient opacity (dark = 1σ, light = 2σ)

## Encoding Principles

Brief rules from perceptual science:

### Preattentive Attributes (Cairo)
These "pop out" in <250ms—use for key distinctions:
- Color (hue)
- Size
- Position
- Orientation

If your main finding should be visible at a glance, encode it preattentively.

### Working Memory Limits
Humans hold ~4 chunks in working memory:
- Legends with >4 items require constant back-and-forth
- Direct labeling dramatically reduces cognitive load
- Group by meaningful categories to chunk (8 items → 2 groups of 4)

### Redundant Encoding (Wilke)
Never rely on color alone:
- Shape + color for categories
- Position + color for emphasis
- Ensures colorblind safety and bad projector survival

## The Refinement Loop

After generating the plot, inspect against:

### The Squint Test (Knaflic)
Squint at the figure. What stands out? If it's not your main finding, you have:
- Clutter competing with signal
- Wrong visual hierarchy
- Preattentive attributes on wrong elements

### Data-Ink Ratio (Tufte)
For each element, ask: "Does this earn its ink?"
- Remove chart frames if not essential
- Lighten or remove gridlines
- Replace legends with direct labels
- Remove redundant axis lines

### The 1+1=3 Principle (Tufte)
Two elements create emergent visual artifacts (the space between). Check:
- Dense grids creating moiré
- Grouped bars creating unintended rhythms
- Close parallel lines creating "third" shapes

### Colorblind Check
Verify with simulation (viridis is designed for CVD safety).
Test: Would the message survive grayscale printing?

## Reference Files

**Consult as needed**:
- [viz-catalog.md](references/viz-catalog.md) — Form directory organized by visualization function
- [color-palettes.md](references/color-palettes.md) — Colormaps, categorical palettes, Porch Morning theme
- [design-system.md](references/design-system.md) — Typography, decluttering checklist, styling

**Library preference**: Use seaborn over raw matplotlib when possible. Seaborn provides cleaner defaults and better statistical visualization primitives.

## Quick Reference: Common Mistakes

| Mistake | Fix |
|---------|-----|
| Jet/rainbow colormap | Use `forestdawn` (diverging) or `mako`/`rocket` (sequential) |
| >5 colors in legend | Small multiples or direct labeling |
| Dual y-axes | Two separate plots or faceting |
| 3D effects | Never. Use 2D with color/facets |
| Pie charts for comparison | Dot plot or bar chart |
| Bar chart not starting at zero | Start at zero (length encoding) or use dot plot |
| Truncated axis exaggerating effect | Show full range or use log scale |
| Heavy matplotlib defaults | Apply decluttering checklist |
