---
title: Hierarchical Memory Standard (Levels 1-3 & Rationale)
date: 2026-04-18
category: best-practices
module: memory_hierarchy
problem_type: best_practice
component: assistant
severity: high
applies_when:
  - Storing long-term project decisions
  - Defining agent identity
  - Managing architectural constraints
tags: [memory, hierarchy, rationale, best-practice]
---

# Hierarchical Memory Standard (Levels 1-3 & Rationale)

## Context
Inconsistencies in agent behavior arose from treating core axioms and transient facts with equal weight. Without a "rationale" field, the reasoning behind past architectural decisions was lost, leading to accidental regressions or "mimicry" without understanding.

## Guidance
Standardized hierarchy and awareness requirements for all stored insights via the `store_insight` tool:

### 1. The 3-Level Hierarchy
- **Level 1 (Critical)**: **Project Axioms & Identity**. Rules that must never be broken (e.g., "Always use SQLite"). These are auto-loaded at session start via the `mem0://context/critical` resource.
- **Level 2 (Standard)**: **Decisions & Intentional Facts**. Workflow choices or stable project information.
- **Level 3 (Low)**: **Observations & Preferences**. Minor details or transient user preferences.

### 2. The Rationale Requirement
Every memory categorized as `decision` **must** include a `rationale`. This field captures the "Why" (e.g., "Chose Chroma because it supports local persistence").

## Why This Matters
1. **Context Integrity**: Level 1 memories prevent the agent from hallucinating or proposing incompatible architectures.
2. **Awareness**: Rationale preservation allows the agent (and future agents) to understand the *logic* of the project, not just the state.
3. **Efficiency**: Auto-loading only Level 1 memories at boot keeps the context window lean while maintaining fundamental rules.

## When to Apply
Apply this standard every time a significant decision is made or a project truth is discovered. Use Level 1 sparingly to avoid context bloat.

## Examples

### Level 1 Axiom (Identity)
```python
# Content: "The project uses Python 3.10+ and FastMCP."
# Category: "axiom"
# Importance: 1
# Rationale: "Standardized stack for Deli ecosystem compatibility."
```

### Level 2 Decision (Logic)
```python
# Content: "Renamed add_memory to store_insight."
# Category: "decision"
# Importance: 2
# Rationale: "Better alignment with the new hierarchical/rationale metadata model."
```

## Related Solutions
- [Metadata Filtering Fix (2026-04-17)](../integration-issues/mem0-v2-api-fix-2026-04-17.md): Established the technical ability to filter by metadata.
- [Chroma Concurrency Fix (2026-04-17)](../integration-issues/mem0-concurrency-chroma-filelock-2026-04-17.md): Source of the first L1 axiom regarding FileLock.
