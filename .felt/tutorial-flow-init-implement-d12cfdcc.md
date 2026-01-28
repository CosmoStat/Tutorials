---
title: 'Tutorial flow: init → implement → validate'
status: closed
kind: spec
priority: 2
depends-on:
    - real-space-correlated-field-50b252b1
created-at: 2026-01-28T12:51:44.937308+01:00
closed-at: 2026-01-28T12:51:44.937314+01:00
close-reason: |-
    Meeting decision on tutorial structure:

    **Flow:**
    1. Clone TreeCorr, pip install (live, should work on IPCs)
    2. Run `claude init` — while it runs, explain TreeCorr + correlation functions
    3. Ask Claude to implement new GV correlation function
    4. Use plan mode (good practice, shows how it works)
    5. While implementation runs, discuss context management (CLAUDE.md, skills, MCPs)
    6. Run validation: overplot theory vs measurement, no fitting

    **Timing budget:**
    - Intro + install: ~10 min
    - Implementation block: ~20-25 min
    - Context management: ~15 min
    - Validation: ~10 min
    - Q&A buffer throughout

    **Key pedagogical choice:** don't autocompact, but point out this isn't how you want to work in practice. Show context window behavior in real time.
---
