# Innerlytics: Designing a Deterministic Reflection Tree

## 1. Objective

The goal of this assignment was to design a deterministic reflection system that guides users through a structured end-of-day conversation. The system avoids probabilistic or generative outputs and instead encodes behavioral insights into a decision tree, ensuring consistency, interpretability, and auditability.

This task focuses on knowledge engineering—translating psychological frameworks into a structured, navigable system.

---

## 2. Design Approach

The system is built around three psychological axes:

### Axis 1: Locus (Victim ↔ Victor)

This axis evaluates whether users perceive outcomes as externally driven or influenced by their own actions.

- Inspired by: Locus of Control (Julian Rotter), Growth Mindset (Carol Dweck)
- Design focus:
  - Avoid blame
  - Surface awareness of personal agency

Strategy:
- Split users based on emotional framing of the day
- Use follow-up questions to detect perceived control

---

### Axis 2: Orientation (Entitlement ↔ Contribution)

This axis examines whether users focus on what they received or what they contributed.

- Inspired by: Psychological Entitlement, Organizational Citizenship Behavior
- Design focus:
  - Make entitlement visible without judgment

Strategy:
- Use realistic workplace scenarios
- Branch into contribution vs expectation pathways

---

### Axis 3: Radius (Self ↔ Others)

This axis captures the breadth of the user’s perspective.

- Inspired by: Self-Transcendence (Maslow), Perspective-Taking
- Design focus:
  - Expand awareness beyond self

Strategy:
- Gradually widen scope (self → team → colleague → end user)

---

## 3. Tree Structure & Logic

The system uses the following node types:

- **Question Nodes**: Collect structured input through fixed options  
- **Decision Nodes**: Route deterministically based on user answers  
- **Reflection Nodes**: Provide contextual insights  
- **Bridge Nodes**: Transition smoothly across axes  
- **Summary Node**: Synthesizes user behavior  

The tree is designed as a progressive conversation where each axis builds on the previous one.

---

## 4. Signals & State

User responses generate signals that accumulate in state:

- axis1: internal / external  
- axis2: contribution / entitlement  
- axis3: self / altrocentric  

The system uses simple tallies to determine dominant tendencies, which are used in the final summary.

This avoids:
- Black-box models  
- Sentiment analysis  
- Non-deterministic outputs  

---

## 5. Key Design Decisions

### Fixed Options Only
Ensures determinism and eliminates ambiguity in interpretation.

### No Moralizing Tone
Reflections are designed to encourage awareness, not judgment.

### Conversational Flow
The tree behaves like a guided reflection, not a survey:
- Axis 1 builds awareness  
- Axis 2 redirects focus  
- Axis 3 expands perspective  

---

## 6. Trade-offs

- Depth vs Readability: More branches increase nuance but reduce simplicity  
- Determinism vs Personalization: Consistency is prioritized over dynamic responses  
- Breadth vs Cognitive Load: Questions are limited to avoid fatigue  

---

## 7. Future Improvements

- Deeper branching within each axis  
- More advanced summary synthesis  
- Persistent history tracking  
- UI-based interaction for better engagement  

---

## 8. Conclusion

Innerlytics demonstrates how psychological insights can be encoded into deterministic systems. The system provides structured reflection through carefully designed questions and decision paths, ensuring consistency and interpretability without relying on AI at runtime.