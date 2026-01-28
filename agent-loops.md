author: @cailmdaley, @EiffL, @calumhrmurray
summary: Learn how to use AI Agents for your research workflows, focusing on context management, skill extension, and verification of scientific code.
id: agent-loops
categories: AI, agents, cosmology, scientific-computing
environments: Web
status: Published
feedback link: https://github.com/CosmoStat/Tutorials/issues

# Agent Loops: Software Engineering in 2026

## Overview
Duration: 0:01:00

### What You'll Learn

- How AI coding agents work, what a model harness is, and why agents are different from chatbots 
- Managing context: in-session vs. persistent memory
- Extending agents with skills and plugins
- Verifying AI-generated scientific code
- Engineering feedback loops to reduce manual intervention

### What You'll Do

You'll use an AI agent to implement a real feature in a cosmology library, then verify the results by building an independent, scientifically motivated check.

![Claude Code in action](img/claude-code-demo.gif)

### Prerequisites

- Python 3.9+ with pip
- Basic familiarity with the command line
- A working Claude Code installation (`curl -fsSL https://claude.ai/install.sh | bash`)
- Helpful: familiarity with cosmology concepts (lensing, correlation functions)

## What Makes an Agent Different from a Chatbot?
Duration: 0:10:00

### LLM vs. Agent

A **large language model (LLM)** takes text in and produces text out. Claude, GPT-4, Gemini — at their core, they're sophisticated **simulators** of text.

An **agent** is an LLM wrapped (trapped?) in a loop with access to tools (Read, Write, Bash):

```python
context = startup_context + user_prompt
while True:
    response = llm(context)
    if response.has_tool_calls:
        context += execute(response.tool_calls)
    else:
        break # pass turn back to user
```

| Chatbot | Agent |
|---------|-------|
| Single turn: prompt → response | Multi-turn: prompt → action → observation → action → ... |
| You execute the suggestions | Agent executes its own suggestions |
| No memory of execution results | Sees results, adapts, retries |
| You are the feedback loop | Agent is the feedback loop |

![Chatbot vs Agent: One-shot vs Action Loop](img/chatbot-vs-agent.png)

Every AI coding tool you've heard of — Claude Code, Cursor, Codex, Gemini CLI — is built on this same pattern. The model is the engine and does almost all the work. The loop + tools is what makes it an agent.

### What is a Model Harness?

The **harness** is everything except the model itself. Think of the model as an engine; the harness is the car — steering, brakes, dashboard, fuel system.

![Model harness as car analogy](img/model-harness-diagram.png)

Note: The model is increasingly commodity — Claude Opus 4.5, ChatGPT 5, Gemini 3 perform similarly on benchmarks. **The harness determines whether agents succeed or fail.** This is why Anthropic, Google, and OpenAI are all investing heavily in harness engineering, not just model training.

A caveat: this is only true because frontier models are roughly equivalent. When there are big jumps in capability, SOTA model beats best harness. But with Opus 4.5, we may be at the point where raw intelligence isn't the limiting factor — harnessing is.

### The Agent Landscape in 2026

By the end of 2025, roughly 85% of developers regularly used AI tools for coding. Andrej Karpathy on the shift:

```text
Given the latest lift in LLM coding capability, like many others I rapidly
went from about 80% manual+autocomplete coding and 20% agents in November
to 80% agent coding and 20% edits+touchups in December.
```
This isn't just for code: mathematicians like Terence Tao use agentic harnesses for mathematics.

---

All major AI labs now ship agent harnesses for coding:

| Tool | Interface | Approach |
|------|-----------|----------|
| **Claude Code** / **Codex** | Terminal-first CLI | Autonomous multi-file operations, background agents, context compaction. Codex is open source, longer-running, harder to steer. Claude Code is more interactive, easier to steer, better at communicating what it's doing. |
| **Cursor** | AI-native IDE | Real-time code completion, inline chat, repository-wide edits |
| **Gemini CLI** | Terminal CLI | Google Search grounding, 1M token context, MCP extensibility, unlimited image generation |

These tools are **converging**. Cursor's agent mode looks like Claude Code's agents. Codex adopted similar patterns. 

### Claude Code: A Closer Look

Since we'll use Claude Code in this tutorial, here's what it does under the hood:

**Core capabilities:**
- **File operations**: Read, write, edit files in your codebase
- **Shell execution**: Run tests, build commands, git operations
- **Web search**: Look up documentation, APIs, error messages
- **Sub-agents**: Spawn background workers for parallel tasks

**Context management:**
- **In-session**: Everything the model sees right now (conversation, file contents, tool outputs). As context fills up, performance tends to go down (some call this the "dumb zone"). This is somewhat to analgous to how human performance goes down towards the end of a long work day.
- **Compaction**: When context fills up, older content gets summarized in a lossy compression. The compression may not keep the right context, and some think it's much better to `/clear` and rebuild context from "disk" so to speak.
- **Persistent (CLAUDE.md)**: Instructions that survive across sessions

**The workflow:**

```
You: "add shear-velocity correlations"
     │
     ▼
┌─────────────────────────────────────┐
│ Claude Code reads codebase          │
│ → finds existing correlation classes│
│ → understands patterns              │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│ Claude Code writes new class        │
│ → runs tests                        │
│ → sees failure                      │
│ → reads error, fixes, retries       │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│ Tests pass                          │
│ → Claude Code reports completion    │
│ → You verify the result             │
└─────────────────────────────────────┘
```

Implementation — turning a specification into code — is increasingly handled by agents. What remains is **shaping what to build**, **noticing when it's wrong**, and **deciding what to try next**.

## Setup
Duration: 0:05:00

### Install Claude Code

**Prerequisites:** A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or a [Claude Console](https://console.anthropic.com/) account with API access.

**macOS / Linux / WSL (recommended):**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### First Run & Authentication

Navigate to any project and start Claude Code:

```bash
cd your-project
claude
```

On first run, you'll be prompted to authenticate:
1. A browser window opens to claude.ai
2. Log in with your Anthropic account
3. Authorize Claude Code
4. Return to your terminal — you're ready to go

**How to verify:** Run `claude --version` — you should see a version number. Run `claude` and type `/help` to see available commands.

### Install TreeCorr (for this tutorial)

We'll add a feature to [TreeCorr](https://github.com/rmjarvis/TreeCorr), a library for computing correlation functions in cosmology.

```bash
git clone https://github.com/rmjarvis/TreeCorr.git
cd TreeCorr
pip install -e .
```

### Project Structure

After setup, your workspace should look like:

```
TreeCorr/
├── treecorr/           # Main library code
│   ├── corr2.py        # 2-point correlation functions
│   ├── ggcorrelation.py
│   └── ...
├── tests/              # Test suite
├── CLAUDE.md           # Will be created by /init
└── .claude/
    └── skills/         # Custom skills (optional)
```

**How to verify TreeCorr:** Run `python -c "import treecorr; print(treecorr.__version__)"` — you should see a version number.

## Watch It Work
Duration: 0:20:00

### The Task

We'll ask the agent to add **shear-velocity correlations (spin-2 × spin-1)** to TreeCorr. This feature doesn't exist yet.

**Physics context:** Gravitational lensing shear traces mass along the line of sight — light bends around structure. Transverse velocities flow toward overdense regions as matter falls into potential wells. The cross-correlation probes structure growth differently than either field alone.

### Initialize Project Context

First, let the agent learn about the codebase:

```console
/init
```

This creates a `CLAUDE.md` file — the agent reads the codebase and writes itself notes on how to work here.

**How to run:** In your terminal, navigate to the TreeCorr directory and run `claude`. Then type `/init` and press Enter. Watch as the agent explores the codebase.

### Run the Implementation

Now give this prompt (use plan mode for complex tasks):

```text
please add shear-velocity correlation functions for shear × cosmic velocity fields.
```

Then watch.

### What to Observe

As the agent works, notice:

1. **File exploration** — it reads existing correlation classes to understand patterns
2. **Test discovery** — it finds how other correlations are tested
3. **Iterative fixing** — when tests fail, it reads the error and adjusts
4. **Context compaction** — if context fills up, older content gets summarized

### Before vs. After

| Manual Implementation | Agent Implementation |
|-----------------------|----------------------|
| Read existing code patterns | Agent reads code patterns |
| Write new correlation class | Agent writes class |
| Write tests | Agent writes tests |
| Run tests, debug, repeat | Agent runs tests, debugs, repeats |
| ~1-2 days for a researcher | ~15-20 minutes |

**Reality check:** The agent may run out of context and need compaction. It may make mistakes and backtrack. This is normal — the key is that it handles the feedback loop, not you.

## Context Management
Duration: 0:10:00

Understanding context is essential for effective agent use.

### Two Types of Context

**In-session context** is what the model sees right now:
- Your conversation
- Files it has read
- Tool outputs and errors

When it fills up, older content gets compacted or dropped.

**Persistent context (CLAUDE.md)** survives across sessions:

```
~/.claude/
└── CLAUDE.md              # User-level: your preferences everywhere

TreeCorr/
└── CLAUDE.md              # Project-level: instructions for this codebase
```

Both load automatically at session start.

### Context as RAM

We're back to working with systems that have a Commodore 64's worth of memory — about 128K tokens. Memory management matters again.

Polluting context with irrelevant content is harmful. Don't let things run to the end of the context window; the model gets dumb. The game is keeping context focused on what matters for the current task.

### Exercise: Inspect the Context

Look at the `CLAUDE.md` the agent created during `/init`:

```bash
cat CLAUDE.md
```

**How to run:** Open the CLAUDE.md file and examine it. What conventions did the agent notice? What build commands did it record?

Ask yourself:
- What did it notice about the codebase structure?
- What testing patterns did it identify?
- What would you add or correct?

### Extending Capabilities

**Skills** are reusable instruction bundles:

```
.claude/
└── skills/
    ├── data-visualization/
    │   └── SKILL.md        # Instructions for plotting
    ├── revealjs/
    │   └── SKILL.md        # Instructions for slides
    └── frontend-design/
        └── SKILL.md        # Instructions for web UIs
```

**Plugins (MCPs)** connect to external services — databases, APIs, issue trackers. The agent calls them like any other tool.

## Use What You Built
Duration: 0:15:00

Clear your context and start fresh:

```console
/clear
```

This simulates a new session — no memory of the implementation, just the codebase as it now exists.

### The Data

A collaborator sent you synthetic lensing power spectra derived from a gravitational potential Φ:

| Field | Spin | Description |
|-------|------|-------------|
| κ (convergence) | 0 | Magnification from lensing |
| δ (deflection derivative) | 1 | Gradient of deflection angle |
| γ (shear) | 2 | Shape distortion |

### Exercise: Plot the Power Spectra

```text
Using the data-visualization skill, plot the lensing power spectra from
`data/lcdm_fields/power_spectra.npz`. Show C_ℓ^ΦΦ, C_ℓ^δδ, C_ℓ^αα (EE),
and C_ℓ^γγ (EE) on a log-log plot.
```

**How to run:** Start a fresh Claude session in the Tutorials directory. Paste the prompt above. The agent will use matplotlib through the data-visualization skill.

### Critical Evaluation

When the plot appears, ask:

```text
Is the information well conveyed? Does the result make sense physically?
```

The agent is multimodal — it can see and reason about the plot it created.

## Verify the Results
Duration: 0:20:00

This is a **blind test**. The synthetic data was generated with specific cosmological parameters (Ω_m, S8) that you don't know.

### The Fitting Task

```text
Fit the lensing potential power spectrum C_ℓ^ΦΦ from
`data/lcdm_fields/power_spectra.npz` to recover Ω_m and S8.

Use CAMB to compute theory predictions. Fixed parameters:
h=0.70, Ω_b=0.05, n_s=0.96, z_source=1.0.

Grid search or MCMC over Ω_m ∈ [0.1, 0.5] and S8 ∈ [0.4, 1.0].
```

**How to run:** This may take several minutes. The agent will install CAMB if needed, write fitting code, and iterate until it converges.

### Validate Against Physical Expectations

Reference values from Planck 2018:
- Ω_m ≈ 0.315
- S8 ≈ 0.83

The blind test values are intentionally different — but they should be physically reasonable (within the prior range).

**The question is whether the agent gives the right answer.** Don't blindly trust AI output. Check that the fit converged, the uncertainties are reasonable, and the values make physical sense.

## Managing Backpressure
Duration: 0:10:00

Your feedback is the bottleneck. Every manual check is you in the loop.

### Levels of Automation

**Level 1: Manual loop**
```
You paste code → run it → paste error → repeat
```
Slow, but it works.

**Level 2: Agent runs code**
```
Agent writes code → runs it → sees error → fixes → repeats
You intervene only when judgment is needed
```

**Level 3: Higher-level verification**
```
Agent builds webpage → views it → adjusts layout
Proof assistant checks the math
Numerical benchmarks grade the output
```

### The Science Question

For science: what does backpressure look like when the thing you're verifying is a claim about the world? Tests catch bugs. What catches wrong conclusions?

This is an open problem. Some approaches:
- Cross-validation against independent datasets
- Comparison with published results
- Physical consistency checks (e.g., parameters within expected ranges)
- Human expert review of methodology

## Steering and Intervention
Duration: 0:05:00

Most of the time, let the agent work. But know when to intervene.

### When to Step In

| Situation | Action |
|-----------|--------|
| Going in circles on the same error | Provide a hint or different approach |
| Fundamental misunderstanding | Clarify the requirements |
| You have domain knowledge it lacks | Share the relevant context |
| Inefficient approach | Suggest a better path |

### When to Stay Out

| Situation | Action |
|-----------|--------|
| Making steady progress | Let it continue |
| Minor style issues | Fix later or ignore |
| Taking longer than expected | Patience — it's still faster than manual |

Think of yourself as a senior engineer reviewing a junior's work in real-time. Guide when needed, but don't micromanage.

## Summary
Duration: 0:02:00

### What You Learned

- **Agents are while loops** with tool access — they handle the feedback loop so you don't have to
- **Context has two layers**: in-session (ephemeral) and CLAUDE.md (persistent)
- **Skills and plugins** extend what agents can do
- **Verification is your job** — especially for scientific claims
- **Engineer away backpressure** where possible, but keep humans in the loop for judgment

### The Key Insight

The code writes itself. What doesn't write itself:
- Knowing what to build
- Noticing when something's wrong
- Deciding what to try next

You are the steering mechanism. The agent handles implementation; you handle judgment.

### Next Steps

- Explore the `.claude/skills/` directory and try writing your own
- Practice the verification workflow on your own data
- Identify where you're still the bottleneck — and automate it
