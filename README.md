# Agent Loops

*or: software engineering in 2026*

---

An agent is a while loop with tool access:

```python
context = startup_information + user_prompt
while True:
    response = llm(context)
    if response.has_tool_calls:
        context += execute(response.tool_calls)
    else:
        break
```

Claude Code, Cursor, Codex all work this way.

Implementation — turning a specification into code — is increasingly something these tools handle. What remains is shaping what to build, noticing when it's wrong, deciding what to try next — and managing context.

---

## Part 1: Watch It Work

We're adding a feature to [TreeCorr](https://github.com/rmjarvis/TreeCorr), a widely-used library for computing correlation functions in cosmology — shear-shear, position-position, that sort of thing.

**What's TreeCorr?** When we analyze galaxy catalogs for weak lensing, we measure how galaxy shapes (shear) or positions correlate as a function of separation. TreeCorr handles the pair-counting efficiently using tree structures.

**The new feature.** Gravitational lensing shear traces mass — light bends around structure. Transverse velocities flow toward overdense regions as matter falls into potential wells. Shear and velocity both respond to the same underlying density field, so they're correlated. We'll ask the agent to add shear-velocity correlation functions. This feature doesn't exist yet.

```bash
git clone https://github.com/rmjarvis/TreeCorr.git
cd TreeCorr
pip install -e .
```

Initialize a project context:

```
/init
```

This creates a `CLAUDE.md` file — the agent reads the codebase and writes itself notes on how to work here. Project-level context that persists across sessions.

Now the prompt (in plan mode):

> Please add shear-velocity correlation functions for measuring correlations between gravitational shear and transverse velocity fields.

Then watch.

When I tried this, it took about 15 minutes and ran out of context once. Compaction finished in 2 minutes; the rest was tracking down sign conventions in tests. This is a task that might take a researcher more than a day. The agent doesn't know that. It just loops.

---

## Part 2: Context Management

**In-session context** is what the model sees right now — your conversation, files it's read, tool outputs. It fills up. When it does, older content gets compacted or dropped.

**CLAUDE.md** persists across sessions. It comes in two layers: project-level (`./CLAUDE.md`) for instructions specific to this codebase, and user-level (`~/.claude/CLAUDE.md`) for your preferences across all projects. Both load automatically at session start.

**Exercise:** Look at the `CLAUDE.md` the agent created during `/init`. What did it notice about the codebase? What conventions did it pick up?

**Commands** extend what the agent can do. `/init` is a command. 

**Skills** are reusable capabilities — folders of instructions that Claude loads dynamically. This repo includes a few in `.claude/skills/`: `data-visualization` for plotting, `revealjs` for slides.

Anthropic maintains an official skills library at [github.com/anthropics/skills](https://github.com/anthropics/skills):

```bash
# Register the skills marketplace
/plugin marketplace add anthropics/skills

# Install a skill set
/plugin install document-skills@anthropic-agent-skills
```

Then mention the skill in your prompt: "Use the PDF skill to extract form fields from this document."

**Plugins** bundle skills, commands, and MCP servers into installable packages. Anthropic maintains [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official):

```bash
# Browse available plugins
/plugin > Discover

# Install a specific plugin
/plugin install {plugin-name}@claude-plugin-directory
```

MCP (Model Context Protocol) lets plugins connect to external services. For most scientific work, though, skills and command-line tools are more practical than MCP integrations.

---

## Part 3: Use What You Built

Clear your context (`/clear`) and start fresh. This simulates a new session — no memory of the implementation, just the codebase as it now exists.

A collaborator sent you synthetic lensing power spectra. The physics: four correlated fields derived from a gravitational potential Φ — convergence (spin-0), deflection derivative (spin-1), and shear (spin-2). See [Calum's slides](calum_spin_fields.pdf) for the theory.

Plot the measured power spectra:

> Using the data-visualization skill, plot the lensing power spectra from `data/lcdm_fields/power_spectra.npz`. Show C_ℓ^ΦΦ, C_ℓ^δδ, C_ℓ^αα (EE), and C_ℓ^γγ (EE) on a log-log plot.

The agent will use matplotlib/seaborn through the skill. When it shows you the plot, look at it. Ask:

> Is the information well conveyed? Does the result make sense physically?

The agent can read the plot (it's multimodal) and reason about what it sees.

---

## Part 4: Verify

How do we know Claude didn't just write tests that pass by construction? Independent validation.

The synthetic catalog was generated with a known signal. We measure the correlation function and check that it matches our theoretical expectation. No fitting — just overplotting theory vs measurement.

> Using the new shear-velocity correlation, measure ξ_+ and ξ_- from the catalog in `data/lcdm_fields/`. Overplot the theoretical prediction from the input power spectrum.

The agent will run TreeCorr, compute the correlation functions, and compare to theory. Error bars come from the measurement; the theory curve is known exactly.

**The teachable moment:** We're not entirely trusting the AI. We're using critical thinking to build an independent check. The classic approach: generate data with expected signal → measure → verify measurement matches expectation.

If measurement and theory agree within error bars, the implementation is probably correct. If they don't, something's wrong — and now you have a concrete discrepancy to debug.

---

## Steering

Most of the time, you can let the agent work. But sometimes you'll want to intervene:

---

## Backpressure

Your feedback is the bottleneck. Every time you manually check output, copy an error message, or eyeball a result, you're in the loop. You want to [engineer that away](https://banay.me/dont-waste-your-backpressure/).

**Tiers of verification:**

1. **Manual loop.** You paste code into a chatbot, run it, hit an error, paste the error back. You're the feedback loop. Slow, but it works.

2. **Agentic loop.** The agent runs the code itself. Build errors, test failures, runtime exceptions — caught without you. You stay out until something needs judgment.

3. **Autonomous verification.** Higher-level checks that don't require you at all. The agent views the webpage it built. A proof assistant (Lean) checks the math. Numerical metrics grade the output.

For science: what does verification look like when you're checking claims about the world, not just code correctness? Tests catch bugs. What catches wrong conclusions?

**Context as RAM.** We're back to working with systems that have a Commodore 64's worth of memory — about 128K tokens. Memory management matters again. Polluting context with irrelevant content is harmful. Don't let things run to the end of the context window; the model gets dumb. The game is getting as much verification as possible into the autonomous tier, so your scarce attention goes to what actually needs judgment.

---

The code writes itself. What doesn't write itself is knowing what to build, noticing when something's wrong, deciding what to try next.
