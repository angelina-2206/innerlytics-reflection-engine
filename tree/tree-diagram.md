# Innerlytics Reflection Tree Diagram

```mermaid
flowchart TD

START["Start: Begin Reflection"]

A1_OPEN["Q: How was your day?"]
A1_DECISION["Decision: Day Type"]

A1_Q_HIGH["Q: What made things go well?"]
A1_Q_LOW["Q: What was your instinct?"]

A1_REF_INT["Reflection: Internal Locus"]
A1_REF_EXT["Reflection: External Locus"]

BRIDGE_1_2["Bridge: Move to Contribution"]

A2_OPEN["Q: Contribution today?"]
A2_DECISION["Decision: Orientation"]

A2_Q_CONTRIB["Q: Why did you contribute?"]
A2_Q_ENTITLE["Q: What frustrated you?"]

A2_REF_CONTRIB["Reflection: Contribution"]
A2_REF_ENTITLE["Reflection: Entitlement"]

BRIDGE_2_3["Bridge: Move to Perspective"]

A3_OPEN["Q: Who was impacted?"]
A3_DECISION["Decision: Perspective"]

A3_REF_SELF["Reflection: Self-focused"]
A3_REF_TEAM["Reflection: Team-aware"]
A3_REF_COLLEAGUE["Reflection: Empathy"]
A3_REF_ALTRO["Reflection: Purpose-driven"]

SUMMARY["Summary: Axis Insights"]
END["End Session"]

START --> A1_OPEN
A1_OPEN --> A1_DECISION

A1_DECISION -->|Productive/Mixed| A1_Q_HIGH
A1_DECISION -->|Tough/Frustrating| A1_Q_LOW

A1_Q_HIGH --> A1_REF_INT
A1_Q_LOW --> A1_REF_EXT

A1_REF_INT --> BRIDGE_1_2
A1_REF_EXT --> BRIDGE_1_2

BRIDGE_1_2 --> A2_OPEN
A2_OPEN --> A2_DECISION

A2_DECISION -->|Helped/Went extra| A2_Q_CONTRIB
A2_DECISION -->|Expected/Frustrated| A2_Q_ENTITLE

A2_Q_CONTRIB --> A2_REF_CONTRIB
A2_Q_ENTITLE --> A2_REF_ENTITLE

A2_REF_CONTRIB --> BRIDGE_2_3
A2_REF_ENTITLE --> BRIDGE_2_3

BRIDGE_2_3 --> A3_OPEN
A3_OPEN --> A3_DECISION

A3_DECISION -->|Self| A3_REF_SELF
A3_DECISION -->|Team| A3_REF_TEAM
A3_DECISION -->|Colleague| A3_REF_COLLEAGUE
A3_DECISION -->|End User| A3_REF_ALTRO

A3_REF_SELF --> SUMMARY
A3_REF_TEAM --> SUMMARY
A3_REF_COLLEAGUE --> SUMMARY
A3_REF_ALTRO --> SUMMARY

SUMMARY --> END