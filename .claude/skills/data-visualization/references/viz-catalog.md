# Visualization Catalog

A directory of visualization forms organized by **what you're trying to show** (Wilke's approach), with cosmology-specific variants nested under each category.

## Table of Contents

1. [Visualizing Amounts](#visualizing-amounts)
2. [Visualizing Distributions](#visualizing-distributions)
3. [Visualizing X-Y Relationships](#visualizing-x-y-relationships)
4. [Visualizing Uncertainty](#visualizing-uncertainty)
5. [Visualizing Correlations](#visualizing-correlations)
6. [Visualizing Spatial/Map Data](#visualizing-spatialmap-data)
7. [Visualizing Proportions](#visualizing-proportions)
8. [Multi-Panel Strategies](#multi-panel-strategies)

---

## Visualizing Amounts

Values across categories.

### Standard Forms

**Dot Plot (Cleveland)**
- Preferred over bar chart for amounts
- Position encoding (rank 1) vs length encoding (rank 3)
- Sort by value, not alphabetically
- Excellent for: parameter constraints, model comparisons

```
Use: Categories with single values
Avoid: When zero baseline is conceptually important
```

**Bar Chart**
- Must start at zero (length encoding requires it)
- Horizontal bars when labels are long
- Sort by value unless category order is meaningful

```
Use: When zero is meaningful baseline
Avoid: When values are all similar magnitude (use dot plot)
```

**Heatmap**
- Amounts in a 2D matrix
- Sequential colormap for positive values
- Include colorbar for value lookup

```
Use: Two categorical dimensions, one quantitative value
Avoid: Sparse matrices (most cells empty)
```

### Cosmology Applications

**Parameter Constraint Dot Plots**
- Show constraints from multiple experiments
- Sort by constraining power or publication date
- Add reference line for fiducial value
- Error bars on dots (hybrid with uncertainty viz)

**Detection Significance Table as Heatmap**
- Rows: frequency bands or redshift bins
- Columns: analysis variants or systematics tests
- Color: σ significance or χ²

---

## Visualizing Distributions

The spread and shape of values.

### Standard Forms

**Histogram**
- Bin counts on y-axis
- Choose bin width carefully (too few: loss of detail, too many: noise)
- Consider density normalization for comparison

```
Use: Single distribution, want to see binned counts
Avoid: Comparing many distributions (use ridgelines)
```

**Kernel Density Estimate (KDE)**
- Smoothed continuous estimate
- Bandwidth selection matters (too smooth hides features)
- Better than histogram for comparing 2-3 distributions

```
Use: Smooth underlying distribution, comparison across groups
Avoid: When sample size is small (KDE can mislead)
```

**Violin Plot**
- KDE mirrored vertically + optional boxplot overlay
- Good for comparing distributions across categories
- Shows both shape and summary stats

```
Use: Distributions across 3-10 categories
Avoid: Very few data points (shows spurious shape)
```

**Ridgeline Plot (Joy Plot)**
- Stacked KDEs, slightly overlapping
- Excellent for many distributions
- Natural for ordered categories (time, redshift bins)

```
Use: Many distributions to compare (5-30+)
Avoid: When precise density values matter (overlapping obscures)
```

**Boxplot**
- Median, quartiles, whiskers, outliers
- Compact summary, loses shape information
- Traditional but often inferior to violin

```
Use: Quick summary, limited space
Avoid: When distribution shape matters (bimodality hidden)
```

**Strip/Jitter Plot**
- Individual points with random horizontal displacement
- Shows actual data, not summary
- Good for small N (shows every point)

```
Use: Small sample sizes (N < 100 per group)
Avoid: Large N (overplotting even with jitter)
```

### Cosmology Applications

**Posterior Distributions**
- Ridgeline across parameters
- Mark prior range, posterior mode, credible intervals
- Consistent x-axis range if comparing same parameter

**Residual Distributions**
- Histogram of (data - model)/σ
- Overlay Gaussian N(0,1) for reference
- Check for non-Gaussianity, outliers

**Chain Diagnostics**
- Trace plots: parameter value vs step number
- Autocorrelation plots
- Ridgeline of chains for convergence assessment

---

## Visualizing X-Y Relationships

Continuous variables against each other.

### Standard Forms

**Scatter Plot**
- Position on both axes (rank 1 encoding)
- Add trend line (loess, linear fit) if relationship exists
- Handle overplotting: alpha transparency, hexbin, contours

```
Use: Exploring relationships, showing correlation
Avoid: Connected sequential data (use line plot)
```

**Line Plot**
- Points connected, implies sequence/continuity
- Use when x is ordered (time, frequency, multipole)
- Bank to 45° when slope comparison matters

```
Use: Time series, spectra, functional relationships
Avoid: Unordered x values (scatter instead)
```

**Loess/Smoothed Line**
- Non-parametric smooth trend
- Useful for showing general pattern in noisy data
- Bandwidth controls smoothness

```
Use: Noisy data where trend is the message
Avoid: When precise functional form matters
```

**Connected Scatter**
- Points connected with arrows showing direction
- For paired before/after or trajectory data

```
Use: Trajectories, paired comparisons
Avoid: When sequence is already in x-axis
```

### Cosmology Applications

**Power Spectrum (Cℓ or P(k))**
- **Flatten before plotting** to reveal percent-level features:
  - Angular: $\ell^n C_\ell$ (commonly $D_\ell$, but factor varies by context)
  - Matter: $k^3 P(k)$ or $\Delta^2(k)$
  - Correlation functions: $\theta \xi(\theta)$
- **Log-linear preferred**: log x-axis, linear y-axis after flattening
  - Log-log hides small differences in steep compression
  - Use log-log only when dynamic range itself is the message
- Confidence band for uncertainty (see uncertainty section)
- Residual panel below: (data - model)/σ or data/model
- Multiple spectra: limit to 3-4 overlaid, then facet

**Bandpowers**
- Discrete points with error bars
- Horizontal bars showing ℓ-bin width
- Theory curve as continuous line underneath

**Hubble Diagram**
- Distance modulus vs redshift
- Log scale on redshift axis
- Residuals from fiducial cosmology

**Residual Plots**
- Always show residuals for model fits
- (data - model) for additive, data/model for multiplicative
- Include reference line at 0 (or 1)
- Check for systematic patterns

---

## Visualizing Uncertainty

The gap in Tufte/McCandless that Wilke fills.

### Standard Forms

**Error Bars**
- Discrete points with symmetric or asymmetric bars
- Cap vs no cap: mostly aesthetic (no cap is cleaner)
- Position is primary signal, error bar is secondary

```
Use: Discrete measurements, sparse data
Avoid: Dense continuous data (use bands)
```

**Confidence Band**
- Shaded region around central estimate
- Works for continuous functions (regression, spectra)
- Can show multiple confidence levels (1σ, 2σ)

```
Use: Continuous uncertainty, dense data
Avoid: Discrete measurements (use error bars)
```

**Gradient Ribbon**
- Opacity fades from high probability (center) to low (edges)
- More informative than hard-edged bands
- Shows distribution shape, not just interval

```
Use: When distribution shape matters, not just interval
Avoid: When hard boundaries are conceptually correct
```

**Point Range / Interval Plot**
- Point + line showing interval
- Multiple intervals can show different confidence levels
- Good for comparing constraints across many items

```
Use: Many constraints to compare
Avoid: When continuous uncertainty matters
```

**Half-Eye / Eye Plot**
- Interval + density visualization
- Shows both summary and distribution shape
- Hybrid of violin and point range

```
Use: Full posterior visualization for key parameters
Avoid: Space-constrained plots
```

### Cosmology Applications

**Spectral Uncertainty Bands**
- 1σ band: darker/more opaque
- 2σ band: lighter/more transparent
- Can use hatching for print-safety

**MCMC Contours**
- In 2D: filled contours at 68%, 95%
- Consider: gradient fill vs hard boundaries
- Ensure contour levels are explicitly labeled

**Asymmetric Errors**
- Common in cosmology (log-normal distributions)
- Visual asymmetry must be obvious
- Consider: showing full posterior instead

**Upper/Lower Limits**
- Arrows indicating bound direction
- Clear visual distinction from detections
- Standard: arrow pointing toward allowed region

---

## Visualizing Correlations

Relationships between many variables.

### Standard Forms

**Correlation Matrix Heatmap**
- Diagonal is 1 (correlation) or maximum (covariance)
- Diverging colormap: red-white-blue
- White at zero/center value
- Consider: upper triangle only (symmetric)

```
Use: Overview of all pairwise relationships
Avoid: When precise values matter (use table or add numbers)
```

**Scatter Matrix (Pairs Plot)**
- All pairwise scatterplots in grid
- Diagonal: histograms or KDEs of each variable
- Good for exploring multivariate structure

```
Use: Exploratory analysis, looking for relationships
Avoid: Many variables (>8-10, becomes overwhelming)
```

**Triangle/Corner Plot**
- Scatter matrix + contours for posterior samples
- 1D posteriors on diagonal
- 2D joint posteriors off-diagonal
- Standard in cosmology parameter estimation

```
Use: MCMC results, parameter constraints
Avoid: Non-MCMC data (use scatter matrix or correlation matrix)
```

### Cosmology Applications

**Covariance Matrix**
- Diverging colormap, white at zero
- Consider log scale for large dynamic range
- Add grid lines at meaningful boundaries (frequency bands, bins)
- Label: frequency/multipole on both axes

**Correlation Matrix**
- Normalized version of covariance
- Diagonal is 1
- Often cleaner for understanding structure

**Triangle Plots for Cosmological Parameters**
- Standard layout from `corner`, `getdist`, `chainconsumer`
- Contour levels: 68%, 95% (1σ, 2σ)
- Include 1D marginalized posteriors
- Mark fiducial/input values if known
- Consistent parameter ranges across comparisons

---

## Visualizing Spatial/Map Data

Geographic or sky-based data.

### Standard Forms

**Choropleth**
- Regions colored by value
- Sequential colormap for magnitude
- Diverging colormap for deviation from reference

```
Use: Data aggregated by region
Avoid: When point locations matter (use symbol map)
```

**Symbol Map**
- Points at geographic locations
- Size/color encodes value
- Better than choropleth for point data

```
Use: Discrete location data
Avoid: Continuously varying fields (use raster)
```

### Cosmology Applications

**Mollweide Projection**
- Full-sky maps
- Standard in CMB, large-scale structure
- Graticule: RA/Dec or Galactic l/b

**Healpix Maps**
- Pixelization for full-sky
- Use `healpy` for plotting
- Consider: showing only observed regions

**Orthographic Projection**
- Hemisphere view for partial sky
- Good for showing specific regions

**RA/Dec Scatter**
- For discrete source catalogs
- Consider density binning for many sources
- Add survey footprint as reference

**Map Residuals**
- Diverging colormap centered on zero
- Check for systematic spatial patterns
- Include mask showing excluded regions

---

## Visualizing Proportions

Parts of a whole.

### Standard Forms

**Stacked Bar**
- Parts stacked to show total
- Bottom category easiest to compare
- Order categories thoughtfully

```
Use: Few categories (3-5), totals matter
Avoid: Many categories, precise comparison needed
```

**Side-by-Side Bars**
- Each category separate bar
- Better for comparison than stacked
- Loses sense of total

```
Use: Comparing parts across groups
Avoid: When total is the message
```

**Pie Chart**
- Controversial: angle encoding is poor
- Use sparingly, only for ~2-4 categories
- Tufte and Cleveland recommend against

```
Use: Almost never in scientific contexts
Avoid: Precise comparisons, >4 categories
```

### Cosmology Applications

**Component Spectra**
- Stacked area showing CMB + foregrounds
- Order: largest component at bottom
- Use when showing total is key

**Error Budget**
- Dot plot of variance contributions
- Sorted by magnitude
- Shows which systematics dominate

---

## Multi-Panel Strategies

When single plots aren't enough.

### Small Multiples (Trellis/Faceting)

Same plot structure, different data subsets:
- All panels share axes for comparison
- Better than overlaying >4 groups
- Order panels meaningfully (time, redshift, etc.)

**When to facet vs overlay**:
- Overlay: 2-4 groups, when interaction/crossing matters
- Facet: 5+ groups, when individual patterns matter

### Layered Complexity (Tufte)

Build dense plots with visual separation:
- Signal layer: bold, saturated
- Context layer: gray, transparent
- Use alpha to separate "1000 points" from "key result"

### Main + Residual

Standard for model-data comparison:
- Top panel: data and model
- Bottom panel: residuals
- Shared x-axis, linked zooming
- Height ratio: ~3:1 (main:residual)

### Inset Panels

Zoom into region of interest:
- Show context in main panel
- Detail in inset
- Clear visual link between them

### Multi-Axis Alternatives

Instead of dual y-axes (avoid!):
- Stacked panels with shared x-axis
- Side-by-side panels
- Index both series to common baseline
