# Building the Codelab

## Install claat

The `claat` (Codelabs as a Thing) tool converts markdown to the Codelabs HTML format.

```bash
# With Go installed:
go install github.com/googlecodelabs/tools/claat@latest

# Or download binary from:
# https://github.com/googlecodelabs/tools/releases
```

## Build

```bash
claat export agent-loops.md
```

This creates an `agent-loops/` directory with `index.html`.

## Serve locally

```bash
# Option 1: Python
python -m http.server 8000
# Then open http://localhost:8000/agent-loops/

# Option 2: claat serve (auto-rebuilds on changes)
claat serve
# Opens http://localhost:9090
```

## Publish

The generated `agent-loops/` directory is static HTML. Host it anywhere:
- GitHub Pages
- Netlify
- Any static file server

For the full Google Codelabs site experience with search and categories, see:
https://github.com/googlecodelabs/tools/tree/main/site
