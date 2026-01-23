# Design System

Polish layer for data visualizations: color, typography, decluttering. Apply after selecting visualization form.

## Table of Contents

1. [Color](#color)
2. [Typography](#typography)
3. [Decluttering Checklist](#decluttering-checklist)
4. [Matplotlib Styling](#matplotlib-styling)
5. [Mode-Specific Styling](#mode-specific-styling)

---

## Color

### Color Scale Types

Match scale type to data type:

**Sequential** — Low to high, single direction
- For: Intensity, magnitude, counts, positive-only values
- Recommended: `viridis`, `plasma`, `inferno`, `cividis`
- Avoid: `jet`, `rainbow` (perceptually non-uniform, colorblind-unsafe)

**Diverging** — Two directions from meaningful center
- For: Residuals, correlations, deviations from reference
- Recommended: `RdBu`, `coolwarm`, `PiYG`
- Center: White or neutral gray at zero/reference value
- Ensure: Symmetric around center if data is symmetric

**Qualitative** — Distinct categories, no ordering
- For: Different experiments, instruments, analysis variants
- Recommended: ColorBrewer qualitative palettes, `tab10`
- Maximum: 5-8 distinct colors before confusion
- Beyond 8: Use faceting or shape+color encoding

### Colorblind Safety

~8% of men have color vision deficiency:

**Safe palettes**:
- `viridis`, `cividis` — Designed for CVD safety
- `RdBu` — Distinguishable red-blue for most CVD types
- Blue-orange combinations

**Avoid**:
- Red-green as sole distinction
- Rainbow/jet (red-green spans)
- Subtle hue differences without luminance change

**Redundant encoding**: Always pair color with another channel:
- Color + shape for scatter points
- Color + linestyle for lines
- Color + direct label for clarity

### Print and Grayscale

For papers that may be printed in B&W:

- **Luminance must vary**: Sequential colormaps work; pure hue rotation fails
- **Test**: Convert to grayscale and check discriminability
- **Fallback**: Add linestyle variation (solid, dashed, dotted)
- **Hatching**: For filled regions, consider pattern fills

### Color Guidelines by Mode

**Mode A (Paper)**:
- Restrained palette: 1-3 main colors + gray
- High contrast with white background
- Test in grayscale
- Avoid: bright saturated colors competing for attention

**Mode B (Outreach)**:
- Bold accent colors for key findings
- Visual hierarchy through saturation
- Dark backgrounds acceptable
- One entry point color that draws the eye

### Specific Recommendations

| Data Type | Colormap | Notes |
|-----------|----------|-------|
| Intensity/magnitude | `viridis` | Default sequential, CVD-safe |
| Residuals | `RdBu` | Diverging, white at zero |
| Covariance | `RdBu` or `coolwarm` | White at zero for covariance, white at 1 for correlation |
| CMB maps | `planck` (custom) or `RdBu` | Convention-dependent |
| Sky masks | Binary grayscale | Observed (white) vs masked (gray) |
| Categories ≤5 | `tab10` subset | Distinct hues |
| Categories >5 | Facet instead | Too many colors confuse |

---

## Typography

### Hierarchy

Visual importance through text styling:

1. **Title** — Largest, can be bold
   - Paper mode: Descriptive ("Power Spectrum of Field A")
   - Outreach mode: Takeaway ("Field A Shows Unexpected Excess")

2. **Axis Labels** — Clear, medium size
   - Include units: "Multipole ℓ" or "ℓ"
   - Include units in parentheses: "Power (μK²)"

3. **Tick Labels** — Smaller, readable
   - Actual values, not scientific notation for log scales: 0.01, 0.1, 1, 10
   - Avoid crowding: fewer ticks is better

4. **Annotations** — Context-dependent
   - Direct labels on data when possible
   - Legends when direct labeling is impractical

5. **Captions** — Not on the figure itself
   - For papers: detailed caption in LaTeX
   - For presentations: verbal explanation

### Font Guidelines

**For papers** (matplotlib defaults are usually fine):
- Serif or sans-serif matching document
- Size: readable at expected print/screen size
- Consistency across all figures

**For presentations**:
- Larger text (axis labels visible from back of room)
- Sans-serif preferred for screen
- High contrast (dark text on light background or vice versa)

### Direct Labeling vs Legends

**Prefer direct labeling when**:
- ≤4 series
- Lines/points have clear space nearby
- Identity is primary message

**Use legend when**:
- >4 series (but consider faceting first)
- Direct labels would overlap
- Space is constrained

**Legend placement**:
- Inside plot area if there's empty space
- Outside if plot is dense
- Never obscuring data

### Numbers and Units

**Format consistency**:
- Decimal places: match measurement precision
- Scientific notation: only when necessary, prefer actual values on log scales
- Units: always include, either in axis label or parentheses

**Examples**:
- Good: "Frequency (GHz)" with ticks at 30, 100, 300
- Bad: "ν [1e9 Hz]" with ticks at 3e10, 1e11, 3e11

---

## Decluttering Checklist

Systematic approach to removing visual noise (Knaflic/Tufte).

### The Process

After generating a plot, go through each item:

1. **Chart frame/box**
   - Try removing the full box
   - Often only left + bottom axes needed
   - Spines can be shortened to data range

2. **Gridlines**
   - Remove or make very light (gray, thin)
   - Horizontal grids often more useful than vertical
   - Grid should never compete with data

3. **Axis lines**
   - Can be removed if gridlines provide reference
   - If kept, subordinate (thin, gray)

4. **Tick marks**
   - Fewer is better (5-7 major ticks)
   - Minor ticks: only if precision needed
   - Direction: outward or removed, not inward competing with data

5. **Background color**
   - White is almost always best
   - Remove gray backgrounds (seaborn default)

6. **Legend**
   - Can it be replaced with direct labels?
   - Can title be removed (obvious from context)?
   - Position: not covering data

7. **Data markers**
   - Are markers necessary, or is the line enough?
   - If markers, are they too large/prominent?

8. **3D effects**
   - Remove. Always.
   - 3D bars, shadows, gradients: no.

### The Squint Test

After decluttering:
1. Step back or squint at the figure
2. What stands out?
3. If it's not your main finding, keep removing elements

### Before/After Mindset

Default matplotlib creates cluttered figures. Transform:

**Default problems**:
- Heavy black frame
- Dense tick marks pointing inward
- Gray background (some themes)
- Legend box with frame
- Gridlines competing with data

**After decluttering**:
- Clean axes or no frame
- Minimal ticks, pointing out or removed
- White background
- Legend without frame, or direct labels
- Light or no gridlines

---

## Matplotlib Styling

Concrete implementation for matplotlib.

### Basic Clean Style

```python
import matplotlib.pyplot as plt

# Apply at start of script/notebook
plt.rcParams.update({
    # Remove top and right spines
    'axes.spines.top': False,
    'axes.spines.right': False,

    # Clean tick direction
    'xtick.direction': 'out',
    'ytick.direction': 'out',

    # Subtle grid
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',

    # White background
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',

    # Reasonable font sizes
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
})
```

### Per-Figure Cleanup

```python
fig, ax = plt.subplots()
# ... plot data ...

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Light grid
ax.grid(True, alpha=0.3, linestyle='--')

# Remove legend frame
ax.legend(frameon=False)

# Tighter layout
fig.tight_layout()
```

### Log Scale Labels

```python
from matplotlib.ticker import ScalarFormatter

ax.set_xscale('log')
ax.set_yscale('log')

# Actual values instead of 10^n
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())
```

### Colorbar Styling

```python
cbar = fig.colorbar(im, ax=ax)
cbar.ax.tick_params(size=0)  # Remove tick marks
cbar.outline.set_visible(False)  # Remove frame
```

---

## Mode-Specific Styling

### Mode A: Paper Style

Optimize for precision, printing, convention:

```python
# Conservative, clean
plt.rcParams.update({
    'figure.figsize': (6, 4),
    'font.size': 9,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.0,
    'lines.markersize': 4,

    # Muted colors
    'axes.prop_cycle': plt.cycler(color=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'
    ]),
})
```

**Checklist**:
- [ ] Readable at journal column width (~3.5 inches)
- [ ] Survives grayscale printing
- [ ] Axis labels include units
- [ ] Caption provides context (in LaTeX, not on figure)

### Mode B: Presentation Style

Optimize for impact, screen display:

```python
# Bold, high contrast
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 14,
    'axes.linewidth': 1.5,
    'lines.linewidth': 2.5,
    'lines.markersize': 8,

    # Bolder colors
    'axes.prop_cycle': plt.cycler(color=[
        '#e41a1c', '#377eb8', '#4daf4a', '#984ea3'
    ]),
})
```

**Checklist**:
- [ ] Readable from back of room
- [ ] Title states the takeaway
- [ ] Visual hierarchy clear (main finding pops)
- [ ] Simplified: fewer data series, cleaner annotations

### Dark Mode (Outreach/Web)

For dark backgrounds:

```python
plt.style.use('dark_background')
plt.rcParams.update({
    'axes.facecolor': '#1a1a2e',
    'figure.facecolor': '#1a1a2e',
    'text.color': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
})
```

---

## Quick Reference

### Minimum Viable Cleanup

Apply these three changes to any matplotlib figure:

```python
# 1. Remove top/right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 2. Remove legend frame
if ax.get_legend():
    ax.get_legend().set_frame_on(False)

# 3. Lighten grid
ax.grid(True, alpha=0.3, linestyle='--')
```

### Font Size Guidelines

| Element | Paper (9pt base) | Presentation (14pt base) |
|---------|------------------|--------------------------|
| Title | 11-12pt | 18-20pt |
| Axis label | 10pt | 16pt |
| Tick label | 8-9pt | 12-14pt |
| Legend | 8-9pt | 12-14pt |
| Annotation | 8pt | 12pt |

---

## Color Palettes

For detailed definitions, see [color-palettes.md](color-palettes.md). Quick summary:

| Type | Preferred Aesthetic | Perceptually Uniform |
|------|---------------------|----------------------|
| Diverging | `forestdawn` | `vlag`, `icefire` |
| Sequential | Porch Morning blends | `mako`, `rocket` |
| Categorical | Porch Morning colors | seaborn `deep` |
