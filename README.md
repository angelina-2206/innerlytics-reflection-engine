# Innerlytics — Deterministic Reflection Engine

Innerlytics is a structured, deterministic reflection system that guides users through an end-of-day conversation using a decision tree. It encodes psychological frameworks into a navigable structure, enabling consistent and interpretable behavioral insights.

---

## Features

- Deterministic decision tree (no runtime AI/LLM)
- Multi-axis behavioral analysis:
  - Locus (Victim ↔ Victor)
  - Orientation (Entitlement ↔ Contribution)
  - Radius (Self ↔ Others)
- Signal-based state tracking
- Contextual reflection generation
- Structured summary synthesis

---

## Design Philosophy

Reflection systems should be predictable, interpretable, and structured—not generative.

Innerlytics encodes intelligence into:
- Decision paths  
- Carefully designed questions  
- Predefined reflection templates  

---

## Guardrails

- No hallucination risk — no generative outputs  
- Deterministic behavior — same input produces same output  
- Fixed options only — no ambiguity  
- Transparent logic — all reasoning visible in the tree  

---

## Project Structure


innerlytics/
│
├── tree/
│ ├── reflection-tree.json
│ └── tree-diagram.md
│
├── agent/
│ └── innerlytics_agent.py
│
├── transcripts/
│ ├── persona-victim.md
│ └── persona-victor.md
│
├── write-up.md
└── README.md

---

## Tree Diagram

You can view the full decision tree structure here:  
👉 [View Tree Diagram](./tree/tree-diagram.md)

---

## How to Run (Part B)


cd agent
python innerlytics_agent.py


---

## Example Flow

Input:
- Tough day  
- External reaction  
- Entitlement orientation  
- Self-focused perspective  

Output:
- Reflection highlighting lack of perceived control  
- Shift toward contribution  
- Expanded awareness toward others  

---

## Key Insight

Innerlytics is not a chatbot.  
It is a structured knowledge system.

The intelligence lies in:
- How questions are framed  
- How decisions are structured  
- How reflections are delivered  

---

## Author

Angelina Chatterjee