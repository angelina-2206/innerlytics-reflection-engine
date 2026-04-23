<div align="center">

# 🔮 Innerlytics

### Deterministic Reflection Engine

*A structured knowledge system that encodes behavioral psychology into navigable decision trees — no LLMs, no guessing, no hallucinations.*

---

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![JSON](https://img.shields.io/badge/Data-JSON-292929?style=for-the-badge&logo=json&logoColor=white)](./tree/reflection-tree.json)
[![License](https://img.shields.io/badge/License-MIT-e94560?style=for-the-badge)](./LICENSE)
[![Deterministic](https://img.shields.io/badge/Runtime_AI-None-16213e?style=for-the-badge)](#guardrails)

</div>

---

## 🧠 What Is This?

Innerlytics is an end-of-day **reflection engine** that walks employees through a structured conversation using a fully deterministic decision tree. It encodes psychological frameworks — Locus of Control, Organizational Citizenship, Self-Transcendence — into a branching system that guides self-discovery without moralizing, scoring, or generating text.

> **The tree is the product. The intelligence is encoded in the structure, not in a model.**

This project was built as a submission for the [DeepThought CultureTech — Deterministic Reflection Tree](https://github.com/DT-CultureTech/recruitmentassignments/blob/main/DailyReflectionTree.md) assignment.

---

## 🎯 The Three Axes

The reflection progresses sequentially through three psychological dimensions:

| Axis | Spectrum | Psychology | What It Surfaces |
|:----:|:---------|:-----------|:-----------------|
| **1** | **Victim ↔ Victor** | Locus of Control *(Rotter, 1954)* / Growth Mindset *(Dweck, 2006)* | Does the employee see agency in their day, or feel acted upon? |
| **2** | **Entitlement ↔ Contribution** | Psychological Entitlement *(Campbell et al., 2004)* / OCB *(Organ, 1988)* | Is focus on what was received (credit, recognition) or what was given? |
| **3** | **Self-Centric ↔ Altrocentric** | Self-Transcendence *(Maslow, 1969)* / Perspective-Taking *(Batson, 2011)* | How wide is the employee's radius of concern under stress? |

Each axis builds on the previous — agency enables contribution, contribution widens perspective.

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                    reflection-tree.json                      │
│  ┌─────────┐   ┌──────────┐   ┌────────────┐   ┌────────┐  │
│  │ Question │──▶│ Decision │──▶│ Reflection │──▶│ Bridge │  │
│  │  nodes   │   │  nodes   │   │   nodes    │   │ nodes  │  │
│  └─────────┘   └──────────┘   └────────────┘   └────────┘  │
│       │              │              │               │        │
│       ▼              ▼              ▼               ▼        │
│   Fixed opts    Rule matching   Signal emit    Target jump   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  innerlytics_agent.py                        │
│  ┌────────┐   ┌────────────┐   ┌───────────────────────┐   │
│  │ Loader │──▶│ Tree Walker│──▶│ Interpolation Engine  │   │
│  └────────┘   └────────────┘   │  {NODE.answer} → val  │   │
│                     │          │  {axis.dominant} → tag │   │
│                     ▼          └───────────────────────┘   │
│              ┌─────────────┐                                │
│              │ Signal State │  axis1: {internal: 1}         │
│              │   Tracker   │  axis2: {contribution: 1}     │
│              └─────────────┘  axis3: {altrocentric: 1}     │
└─────────────────────────────────────────────────────────────┘
```

### Node Types

| Type | Role | User Action | Count |
|:-----|:-----|:------------|:-----:|
| `start` | Opens the session | None (auto-advance) | 1 |
| `question` | Presents fixed options | Employee selects one | 7 |
| `decision` | Routes based on prior answer | None (invisible) | 8 |
| `reflection` | Delivers insight tied to path | Reads, continues | 12 |
| `bridge` | Transitions between axes | None (auto-advance) | 2 |
| `summary` | Synthesizes the full session | Reads final insight | 1 |
| `end` | Closes session | None | 1 |
| | | **Total Nodes** | **32** |

---

## 📁 Project Structure

```
innerlytics/
│
├── 📂 tree/
│   ├── reflection-tree.json          # The decision tree (Part A deliverable)
│   └── tree-diagram.md               # Mermaid visual of full branching structure
│
├── 📂 agent/
│   └── innerlytics_agent.py          # CLI engine that walks the tree (Part B)
│
├── 📂 transcripts/
│   ├── persona-victim.md             # Full run: External / Entitled / Self-centric
│   └── persona-victor.md             # Full run: Internal / Contributing / Altrocentric
│
├── write-up.md                       # Design rationale and psychological grounding
└── README.md                         # ← You are here
```

---

## 🚀 Quick Start

### Prerequisites

- 🐍 Python 3.8+
- No external dependencies — stdlib only

### Run the Reflection Agent

```bash
cd agent
python innerlytics_agent.py
```

The agent loads `reflection-tree.json`, walks you through 5–7 questions across three axes, and delivers a personalized summary — all without any network calls or AI inference.

---

## 🔒 Guardrails

| Principle | Implementation |
|:----------|:---------------|
| **No LLM at runtime** | Zero API calls. The tree is static data walked by deterministic code. |
| **Full determinism** | Same answers → same path → same reflections → same summary. Every time. |
| **Fixed options only** | Every question has 4 predefined choices. No free-text, no ambiguity. |
| **No moralizing** | Reflections reframe without judging. The tone is a wise colleague, not a therapist. |
| **Auditable paths** | Every conversation can be traced through the JSON without running code. |
| **Dynamic interpolation** | Summary references actual user answers via `{NODE.answer}` placeholders. |

---

## 🔬 How Signals Work

As the employee answers questions, each reflection node emits a **signal** that accumulates in state:

```
axis1:internal   →  state["signals"]["axis1"]["internal"] += 1
axis1:external   →  state["signals"]["axis1"]["external"] += 1
axis2:contribution → state["signals"]["axis2"]["contribution"] += 1
axis2:entitlement  → state["signals"]["axis2"]["entitlement"] += 1
axis3:self         → state["signals"]["axis3"]["self"] += 1
axis3:altrocentric → state["signals"]["axis3"]["altrocentric"] += 1
```

At the summary node, the engine resolves `{axis1.dominant}` to whichever pole received more tallies, then interpolates user answers via `{A1_OPEN.answer}` to produce a personalized, non-generic closing statement.

---

## 🗺️ Tree Diagram

The full branching structure is visualized here:
👉 **[View Interactive Mermaid Diagram](./tree/tree-diagram.md)**

<details>
<summary>📊 Preview: Branching Overview</summary>

```
START
 └── Q1: First reaction when things go wrong?
      ├── [Reflected / Adapted] → Q2a: What drove that response?
      │    ├── [Responsible / Momentum] → 💡 Internal Locus
      │    └── [Pragmatic / Default]    → 💡 Pragmatic Agency
      └── [Frustrated / Waited]  → Q2b: How did you handle it?
           ├── [Found control]         → 💡 Recovery
           └── [Vented / Disengaged]   → 💡 External Locus
                         ↓
              BRIDGE → Contribution Axis
                         ↓
      Q3: Which interaction feels most accurate?
      ├── [Helped / Fixed] → Q4a: What was your focus?
      │    ├── [Solve / Support]   → 💡 Contribution
      │    └── [Credit / Escape]   → 💡 Hidden Entitlement
      └── [Underappreciated / Frustrated] → Q4b: Focus on lack or giving?
           ├── [Helped anyway]      → 💡 Contribution (struggled)
           └── [Recognition / Resentment / Checked out] → 💡 Entitlement
                         ↓
              BRIDGE → Perspective Axis
                         ↓
      Q5: Who were you optimizing for?
      ├── Myself        → 💡 Self-centric
      ├── Team          → 💡 Team-aware
      ├── Colleague     → 💡 Empathetic
      └── Customer      → 💡 Purpose-driven
                         ↓
              📊 SUMMARY → END
```

</details>

---

## 📝 Sample Paths

Two complete transcripts demonstrate divergent journeys through the tree:

| Persona | Axis 1 | Axis 2 | Axis 3 | Transcript |
|:--------|:-------|:-------|:-------|:-----------|
| **Victim** | External locus | Entitlement orientation | Self-centric radius | [View →](./transcripts/persona-victim.md) |
| **Victor** | Internal locus | Contribution orientation | Altrocentric radius | [View →](./transcripts/persona-victor.md) |

Both transcripts are **exact reproductions** of the agent's runtime output — no manual editing, no formatting additions.

---

## 📖 Design Rationale

The full write-up explaining question design, branching trade-offs, and psychological sources is available here:
👉 **[Read the Write-Up](./write-up.md)**

---

## 🧩 Key Design Decisions

| Decision | Rationale |
|:---------|:----------|
| **Behavioral options, not self-labels** | People rarely self-identify as "entitled." Options describe actions ("I did my job but felt underappreciated") to surface the pattern indirectly. |
| **4 reflections per axis** | Captures the nuance between strong-internal, pragmatic-internal, recovery, and external — not just a binary split. |
| **Bridge nodes reference prior axis** | "Now let's shift from how you handled things — to what you contributed" creates narrative continuity, not a survey feel. |
| **Summary interpolates raw answers** | Quoting the user's own words back to them is more impactful than abstract labels. |

---

## 🛠️ Tech Stack

| Component | Technology |
|:----------|:-----------|
| 🌳 Decision Tree | JSON (structured, portable, readable) |
| 🐍 Runtime Engine | Python 3.8+ (stdlib only — `json`, `re`, `collections`) |
| 📊 Diagram | Mermaid.js (renders on GitHub natively) |
| 🔮 AI at Runtime | **None** — fully deterministic |

---

## 👤 Author

**Angelina Chatterjee**

---

<div align="center">

*This is not a chatbot. It is a structured knowledge system.*
*The intelligence is in the questions, the branching, and the reflections — not in a model.*

</div>