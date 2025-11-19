# Branch Game Spec — Notes & Extraction Pointers

This document summarizes how external research from the *Branch · Game Spec Extraction Request* was incorporated into the SwarmBreaker Codex Bundle.

It acts as a map showing where every extracted insight now lives inside the project.

---

## 1. Purpose of This File

* Provide quick pointers to where extracted data was placed.
* Prevent future duplication or divergence between research and canonical specs.
* Offer a staging area for new research (patch notes, wiki updates, observed behaviors).

This file is **reference-only** and contains no authoritative rules.

---

## 2. Source Material

The original research came from:

* *Branch · Game spec extraction request.pdf*
* Reverse-engineered gameplay analysis
* Design pattern observation from other survival/SwarmBreaker titles

This research included:

* Enemy tiering and behavior patterns
* Spawn pacing and wave structure
* Stat progression and power curve logic
* Upgrade archetypes
* XP scaling approximations
* Difficulty curve expectations

These findings were not kept raw—they were normalized and mapped into the canonical documents described below.

---

## 3. Where the Extracted Information Lives Now

### 3.1 Simulation & Architecture → `Swarmbreaker_master_spec.md`

Mapped components:

* Tick-loop structure
* RNG usage guidelines
* Collision + movement interactions
* Scheduling and wave progression
* Entity interaction rules
* Damage, statuses, and scaling primitives

### 3.2 Parser & Input Layer → `Swarmbreaker_Parser_Command_Contract.md`

Mapped components:

* Valid verbs/nouns and arguments for CLI- or tool-driven entry points
* Modifiers (difficulty, flow, seed, mutators, duration) used by tools and batch simulations
* Error policies for these tools
* Structural guarantees for CLI → ParsedIntent translation

### 3.3 Progression & Difficulty → `Swarmbreaker_progression.md`

Mapped components:

* XP model and leveling cadence
* Rarity curves
* Meta-upgrade influence on runs
* Difficulty multipliers
* Torment scaling approximations
* Gold / drop economy structure

### 3.4 Content Structure → `entities.schema.json`

Mapped components:

* Hero stat block definitions
* Enemy tiering (T1/T2/T3/Elite/Boss)
* Ability and Item schemas
* Behavior references
* Core content ID architecture

### 3.5 Visual System Map → `systems.mermaid`

Mapped components:

* Class relationships
* Entity-to-system bindings
* Upgrade → stat → ability flow
* Required dependencies and data paths

---

## 4. How to Add Future Research

When new information is obtained:

1. Add a short note to this file under a new section (e.g., *Patch 1.1 Observations*).
2. Summarize only the extracted structural or numerical insights.
3. Point to which canonical doc must be updated.
4. Do not store raw source material here.

Example entry:

```
## Patch 1.1 Observations (Example)
- Observed increased elite density in late waves.
- Suggested mapping → Swarmbreaker_master_spec.md (spawn scheduler tuning).
- Update expected spawn cadence chart.
```

---

## 5. Role of This Doc in the Codex Workflow

Codex uses this doc to:

* Understand where research-derived logic originated.
* Avoid re-pulling or re-deriving identical insights.
* Keep research separated from rules.
* Maintain a clean architectural boundary between **data sources** and **canonical specifications**.

---

End of Branch Notes.
