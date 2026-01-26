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

We're adding a feature to [TreeCorr](https://github.com/rmjarvis/TreeCorr), which computes correlation functions for cosmology — shear-shear, position-position, that sort of thing.

**Quick physics context.** Gravitational lensing shear traces mass along the line of sight — light bends around structure. Transverse velocities on the sky flow toward overdense regions as matter falls into potential wells. So shear and velocity are correlated: both respond to the same underlying density field. The cross-correlation probes structure growth differently than either field alone.

We'll ask the agent to add shear-velocity correlations (spin-2 × spin-1). This feature doesn't exist yet.

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

Now the prompt:

> please add shear-velocity (spin-2 × spin-1) correlation functions for shear × cosmic velocity fields.

Then watch.

When I tried this, it took about 15 minutes and ran out of context once. Compaction finished in 2 minutes; the rest was tracking down sign conventions in tests. This is a task that might take a researcher more than a day. The agent doesn't know that. It just loops.

---

## Part 2: Context Management

**In-session context** is what the model sees right now — your conversation, files it's read, tool outputs. It fills up. When it does, older content gets compacted or dropped.

**CLAUDE.md** persists across sessions. It comes in two layers: project-level (`./CLAUDE.md`) for instructions specific to this codebase, and user-level (`~/.claude/CLAUDE.md`) for your preferences across all projects. Both load automatically at session start.

**Exercise:** Look at the `CLAUDE.md` the agent created during `/init`. What did it notice about the codebase? What conventions did it pick up?

**Commands** extend what the agent can do. `/init` is a command. So is `/commit`.

**Skills** are reusable capabilities — bundles of instructions the agent can invoke. This repo includes three in `.claude/skills/`: `data-visualization` for plotting, `revealjs` for slides, `frontend-design` for web interfaces.

**Plugins (MCP)** connect to external services — databases, APIs, whatever. The agent calls them like any other tool.

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

Fit the power spectrum to recover the cosmological parameters. This is a blind test — the data was generated with specific (Ω_m, S8) values that you don't know.

> Fit the lensing potential power spectrum C_ℓ^ΦΦ from `data/lcdm_fields/power_spectra.npz` to recover Ω_m and S8.
>
> Use CAMB to compute theory predictions. Fixed parameters: h=0.70, Ω_b=0.05, n_s=0.96, z_source=1.0.
>
> Grid search or MCMC over Ω_m ∈ [0.1, 0.5] and S8 ∈ [0.4, 1.0].

Check whether the fit recovers sensible values. The synthetic data has known truth — Planck 2018 gives Ω_m ≈ 0.315, S8 ≈ 0.83. The blind values are intentionally different.

The question is whether the agent gives the right answer.

---

## Steering

Most of the time, you can let the agent work. But sometimes you'll want to intervene:

---

## Backpressure

Your feedback is the bottleneck. Every time you manually check output, copy an error message, or eyeball a result, you're in the loop. You want to [engineer that away](https://banay.me/dont-waste-your-backpressure/).

The simplest case: you paste code into a chatbot, run it, hit an error, paste the error back. You're the feedback loop. Slow, but it works.

Better: give the agent the ability to run the code itself. Build errors, test failures, runtime exceptions — the agent catches them without you. You stay out of the loop until something needs judgment.

Better still: higher-level verification. The agent can view and interact with the webpage it built. A proof assistant checks the math. Numerical metrics grade the output (think [CMBAgent](https://arxiv.org/abs/2410.24076) benchmarks).

For science: what does backpressure look like when the thing you're verifying is a claim about the world? Tests catch bugs. What catches wrong conclusions?

---

The code writes itself. What doesn't write itself is knowing what to build, noticing when something's wrong, deciding what to try next.
