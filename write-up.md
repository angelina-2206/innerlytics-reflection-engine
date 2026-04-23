# Innerlytics: Design Rationale

## 1. Problem Statement

The task was to design a deterministic reflection system that guides an employee through an end-of-day conversation. The system must encode psychological insight into a branching structure — not generate it at runtime. The constraint is deliberate: a well-designed tree provides consistent, auditable, trustworthy guidance precisely because a human encoded the intelligence into the structure beforehand.

This is fundamentally a knowledge engineering problem. The challenge is not building the software; it is deciding what to ask, in what order, and how to branch — such that a tired employee at 7pm actually pauses and thinks, rather than clicking through to finish.

---

## 2. Question Design: Why These Specific Questions

### Axis 1 — Locus of Control

The opening question is the most important node in the entire tree. It sets the emotional tone of the session and determines whether the employee engages or disengages.

I chose to open with *"When something didn't go as planned today, what was your first reaction?"* rather than a mood-labeling question like "How was your day?" for a specific reason: Rotter's Locus of Control framework (1954) is not about how someone *feels* — it is about where they locate causation. A mood question captures affect, not attribution. By asking about a *reaction to disruption*, the question forces the employee to reveal whether they instinctively reached for agency or surrendered to circumstance.

The four options map to two clusters:

- **Internal locus** — "I thought about what I could have done differently" (retrospective agency) and "I adapted and found another way" (active agency). These correspond to what Dweck (2006) calls growth-oriented responses: the belief that the situation is navigable through effort and strategy.
- **External locus** — "I felt frustrated by things outside my control" (emotional externalization) and "I waited for someone else to fix it" (behavioral passivity). These reflect the fixed-mindset pattern where the individual perceives the outcome as outside their influence.

The follow-up questions then probe the *texture* of that initial response. For the internal cluster, I ask what *drove* their agency — was it genuine ownership ("I felt responsible for the outcome") or merely pragmatic resignation ("I realized complaining wouldn't help")? This distinction matters because Rotter's framework recognizes that internal locus is not monolithic. Someone who acts out of felt responsibility occupies a different psychological position than someone who acts because they see no alternative. The tree captures this with four distinct reflection endpoints rather than a binary internal/external split.

For the external cluster, the follow-up asks how they *handled* feeling out of control. This is where the tree deliberately avoids moralizing. The option "I eventually looked for what I could control" creates a recovery pathway — signaling internal locus even though the opening response signaled external. This design choice reflects the reality that most people are not purely internal or external; they oscillate, and the tree should honor that complexity rather than flattening it.

### Axis 2 — Contribution vs. Entitlement

Entitlement is, by definition, invisible to the person holding it. Campbell et al. (2004) demonstrated that psychological entitlement operates as a stable dispositional trait — people who hold entitled beliefs do not experience them as "entitlement" but as reasonable expectations. This creates a design challenge: if I ask "Were you entitled or contributing today?", no one will self-identify as entitled.

The solution was to frame options around *actions and feelings* rather than self-labels. The opening question — "Think about an interaction you had today. Which statement feels most accurate?" — presents four behaviorally described scenarios:

- **Contribution indicators**: "I stepped in because someone needed help" and "I noticed something broken and fixed it." These describe Organizational Citizenship Behavior (Organ, 1988) — discretionary effort that goes beyond formal role requirements.
- **Entitlement indicators**: "I did my job, but felt underappreciated" and "I felt frustrated covering for others." These describe the experience of entitlement without using the word. They focus on perceived imbalance and unmet expectations.

The second-layer questions deepen this analysis. For the contribution path, I introduced a critical fork: "Solving the problem" vs. "Making sure I got credit later." Both describe someone who went beyond their tasks, but the motivation is entirely different. The latter reveals what I call *hidden entitlement* — the appearance of citizenship behavior that is actually transactional. This is a nuance that a binary contribution/entitlement split would miss entirely.

For the entitlement path, I included a recovery option: "I recognized my frustration but tried to help anyway." This mirrors the Axis 1 design philosophy — allowing the tree to capture psychological movement rather than static states.

### Axis 3 — Radius of Concern

Maslow's later work on self-transcendence (1969) — often overlooked in favor of the more famous hierarchy — argues that the healthiest psychological state involves orienting outward: from "What do I need?" to "What does the world need from me?" Batson's research on perspective-taking (2011) provides the cognitive mechanism: empathy-as-understanding, not empathy-as-sympathy.

I chose to frame this axis around stress rather than general reflection: "Think about the most stressful moment today. Who were you optimizing for?" Stress is the relevant context because it is under pressure that our radius of concern contracts. Asking about stress reveals the *floor* of someone's perspective — who they think about when resources are scarce — which is more diagnostic than who they think about when things are easy.

The four options form a deliberate gradient from narrow to wide:

1. **Self** — "Myself — I just needed to survive the day"
2. **Team** — "My immediate team — we needed to hit our goal"
3. **Individual other** — "A specific colleague — they needed my support"
4. **Abstract other** — "The customer/end-user — delivering value to them"

This progression from concrete-self to abstract-other mirrors Maslow's transcendence spectrum. The tree does not treat "self" as wrong — it treats it as a starting point, and the reflection surfaces the possibility of expansion without prescribing it.

---

## 3. Branching Design and Trade-offs

### Conversational Flow vs. Quiz Structure

The three axes are presented sequentially, connected by bridge nodes that reference the previous axis. The bridge from Axis 1 to Axis 2 reads: "Now let's shift from how you handled things — to what you contributed." This framing is intentional. It creates narrative continuity: agency (Axis 1) naturally leads to questions about what that agency produced (Axis 2), which naturally leads to who it was directed toward (Axis 3). The psychological progression is: awareness of control, then awareness of orientation, then awareness of scope.

### Depth vs. Cognitive Load

Each axis uses exactly two question layers. A deeper tree (three or four questions per axis) would increase diagnostic precision but would also exhaust a tired employee. The design constraint is not just psychological accuracy — it is usability at 7pm after a full workday. Two questions per axis keeps the total session to 5-7 questions, which falls within the cognitive load threshold for reflective tasks.

### Four Reflections Per Axis vs. Two

The tree produces four distinct reflection endpoints for Axis 1 (internal, pragmatic-internal, recovery, external) and four for Axis 2 (contribution, contribution-under-struggle, hidden-entitlement, overt-entitlement). This was a deliberate choice over a simpler binary split. The nuance matters: telling someone who acted pragmatically that they "stayed in the driver's seat" would feel inaccurate and patronizing. The four-way split allows the reflection to honor what actually happened rather than forcing it into a clean dichotomy.

### Signal Accumulation vs. Path-Only Routing

Signals serve a dual purpose. During the session, routing is handled by decision nodes that match the immediately preceding answer. At the summary stage, accumulated signals determine the dominant pole for each axis. This separation is important: it means the summary reflects the *aggregate* of the session rather than just the final answer. In a longer tree with more questions per axis, this architecture would allow for mixed signals — and the summary would still resolve to a dominant tendency.

### Interpolation as Trust-Building

The summary node quotes the employee's own words back to them via the `{A1_OPEN.answer}` placeholder. This is not a cosmetic feature. Reflection research consistently shows that people engage more deeply when they see their own language echoed back. It signals that the system listened, which increases trust in the insight that follows.

---

## 4. What the Signals Encode

| Signal | Meaning | Emitted By |
|--------|---------|------------|
| `axis1:internal` | Employee demonstrated or recovered agency | Reflection nodes in the internal, pragmatic, and recovery paths |
| `axis1:external` | Employee attributed outcomes to external factors | The external locus reflection |
| `axis2:contribution` | Employee oriented toward giving | Contribution and contribution-under-struggle reflections |
| `axis2:entitlement` | Employee oriented toward receiving or credit-seeking | Overt entitlement and hidden entitlement reflections |
| `axis3:self` | Narrow radius of concern under stress | Self-focused reflection |
| `axis3:altrocentric` | Expanded radius of concern under stress | Team, colleague, and purpose-driven reflections |

Signals are emitted by reflection nodes — not question nodes — because the signal represents the system's interpretation of the path, not the raw answer. This keeps the data layer clean: answers are stored verbatim for interpolation, signals are stored as categorical tallies for summary synthesis.

---

## 5. Sources

- Rotter, J.B. (1954). Social Learning and Clinical Psychology. Prentice-Hall.
- Dweck, C.S. (2006). Mindset: The New Psychology of Success. Random House.
- Campbell, W.K., Bonacci, A.M., Shelton, J., Exline, J.J., & Bushman, B.J. (2004). Psychological Entitlement: Interpersonal Consequences and Validation of a Self-Report Measure. Journal of Personality Assessment, 83(1), 29-45.
- Organ, D.W. (1988). Organizational Citizenship Behavior: The Good Soldier Syndrome. Lexington Books.
- Maslow, A.H. (1969). The Farther Reaches of Human Nature. Journal of Transpersonal Psychology, 1(1), 1-9.
- Batson, C.D. (2011). Altruism in Humans. Oxford University Press.

---

## 6. What I Would Improve With More Time

**Deeper branching within each axis.** The current tree uses two questions per axis. A production system would benefit from a third question that probes the *intensity* of the detected pattern — distinguishing between someone who is mildly external and someone who is deeply disengaged.

**Cross-axis routing.** Currently, the three axes are independent sequences connected by bridges. A more sophisticated design would allow Axis 2 questions to vary based on Axis 1 signals. For example, an employee who showed strong internal locus might receive a harder Axis 2 question that probes whether their agency was self-serving or other-serving.

**Longitudinal state.** A single session captures a snapshot. Over multiple sessions, the system could track signal trends and surface patterns: "You have been in survival mode three days this week. What changed on Tuesday?"

**Richer summary synthesis.** Rather than a single template with placeholder substitution, the summary could select from a library of pre-written paragraphs indexed by signal combinations. An internal/contribution/altrocentric path would receive a fundamentally different closing message than an external/entitlement/self path — not just different labels inserted into the same sentence.

**Validation testing with real users.** The current options were designed through research and roleplay testing. Production deployment would require testing with actual employees to verify that the options feel authentic, that the reflections land without condescension, and that the session length remains tolerable after a full workday.