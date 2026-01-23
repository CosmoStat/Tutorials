# Color Palettes

Python-focused color palette reference for scientific visualization. Assumes matplotlib and seaborn as primary plotting libraries.

**Library preference**: Use seaborn over raw matplotlib when possible.

---

## Quick Reference

| Type | Preferred Aesthetic | Perceptually Uniform |
|------|---------------------|----------------------|
| Diverging | `forestdawn` | `vlag`, `icefire` |
| Sequential | Porch Morning blends | `mako`, `rocket` |
| Categorical | Porch Morning colors | seaborn `deep` |

**Default**: Use preferred aesthetic unless precision is explicitly needed.

---

## Porch Morning Palette

Our preferred aesthetic palette. Use individual colors for categorical data, seaborn blends for sequential.

```python
porch_morning = {
    # Core colors (use for categorical data)
    'teal': '#6B9B9B',        # Weathered teal
    'sage': '#A4B095',        # Sagebrush green
    'tan': '#B39C86',         # Tumbleweed brown
    'ochre': '#C08B5C',       # Warm ochre
    'rust': '#A67C68',        # Rust & clay
    'purple': '#5B4B6B',      # Twilight purple

    # Additional qualitative colors
    'accent': '#5A7B7B',      # Cold creek water
    'green': '#6B8B6B',       # Hemlock bough
    'yellow': '#C4A86A',      # Morning light
    'red': '#A87070',         # Rust on tin roof
    'orange': '#B89060',      # Dried leaves
    'cyan': '#5A8B8B',        # Spring runoff

    # Text & backgrounds (for styling)
    'text': '#2E2A26',
    'text_secondary': '#4A4540',
    'text_muted': '#7A7368',
    'bg': '#EDE8E0',
    'paper': '#F8F5F0',
}
```

### Categorical: Pick Colors

```python
import seaborn as sns

# Ordinal (implied progression)
ordinal_6 = [
    porch_morning['teal'],
    porch_morning['sage'],
    porch_morning['tan'],
    porch_morning['ochre'],
    porch_morning['rust'],
    porch_morning['purple'],
]

# Qualitative (no ordering)
qualitative_5 = [
    porch_morning['accent'],
    porch_morning['orange'],
    porch_morning['green'],
    porch_morning['purple'],
    porch_morning['yellow'],
]

sns.set_palette(ordinal_6)  # or qualitative_5
```

### Sequential: Seaborn Blends

```python
import seaborn as sns

# Light palette from any Porch Morning color
teal_cmap = sns.light_palette(porch_morning['teal'], as_cmap=True)
rust_cmap = sns.light_palette(porch_morning['rust'], as_cmap=True)
purple_cmap = sns.light_palette(porch_morning['purple'], as_cmap=True)

# Dark palette
teal_dark = sns.dark_palette(porch_morning['teal'], as_cmap=True)

# Blend two colors
teal_to_rust = sns.blend_palette([porch_morning['teal'], porch_morning['rust']], as_cmap=True)
```

### Diverging: forestdawn

The `forestdawn` colormap from [suisai](https://github.com/yomori/suisai) fits the Porch Morning aesthetic. Teal-green → cream → rust-orange.

```python
# Install: pip install suisai

import suisai.cm as cmo
import seaborn as sns

# Basic usage
sns.heatmap(data, cmap=cmo.forestdawn, center=0)

# Reversed
sns.heatmap(data, cmap=cmo.forestdawn_r, center=0)
```

**Key waypoints:**
```python
forestdawn_waypoints = [
    '#436768',  # 0.00 - deep teal (negative)
    '#94BAB5',  # 0.50 - pale sage (center)
    '#A05638',  # 1.00 - rust (positive)
]
```

Full RGB: [forestdawn-rgb.txt](https://github.com/yomori/suisai/blob/main/suisai/rgb/forestdawn-rgb.txt)

---

## Perceptually Uniform Palettes

Use when quantitative precision matters.

### Sequential: mako, rocket

```python
import seaborn as sns

# mako: blue-green to pale yellow-green (cool)
sns.heatmap(data, cmap='mako')

# rocket: dark purple through red to pale yellow (warm)
sns.heatmap(data, cmap='rocket')
```

### Diverging: vlag, icefire

```python
# vlag: blue → white → red
sns.heatmap(data, cmap='vlag', center=0)

# icefire: cyan → dark → orange
sns.heatmap(data, cmap='icefire', center=0)
```

### Comparison

| Colormap | Type | Perceptually Uniform |
|----------|------|---------------------|
| `forestdawn` | Diverging | Good |
| `vlag` | Diverging | Excellent |
| `icefire` | Diverging | Excellent |
| `mako` | Sequential | Excellent |
| `rocket` | Sequential | Excellent |

---

## Styling

### Porch Morning Style

```python
import matplotlib.pyplot as plt
import seaborn as sns

def apply_porch_morning_style():
    """Apply Porch Morning styling to matplotlib and seaborn."""

    ordinal_6 = ['#6B9B9B', '#A4B095', '#B39C86', '#C08B5C', '#A67C68', '#5B4B6B']

    plt.rcParams.update({
        'figure.facecolor': '#EDE8E0',
        'axes.facecolor': '#F8F5F0',
        'text.color': '#2E2A26',
        'axes.labelcolor': '#2E2A26',
        'axes.edgecolor': '#7A7368',
        'xtick.color': '#4A4540',
        'ytick.color': '#4A4540',
        'grid.color': '#7A7368',
        'grid.alpha': 0.3,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.prop_cycle': plt.cycler(color=ordinal_6),
    })

    sns.set_palette(ordinal_6)
```

### Clean Style (Papers)

```python
def apply_clean_style():
    """Clean, conventional style for papers."""
    sns.set_theme(style='ticks', palette='deep')
    plt.rcParams.update({
        'axes.spines.top': False,
        'axes.spines.right': False,
        'grid.alpha': 0.3,
    })
```

---

## Decision Guide

| Context | Diverging | Sequential | Categorical |
|---------|-----------|------------|-------------|
| Exploratory / talks | `forestdawn` | Porch Morning blend | Porch Morning colors |
| Paper figures | `vlag` / `icefire` | `mako` / `rocket` | seaborn `deep` |
