# index.md

*(Structural System Map — full content)*

Below is the complete structural, content-agnostic SYSTEM MAP for the project.

## Top-Level System Map

```
+--------------------+
|    META SYSTEM     |
|  (Grid / Trees)    |
+---------+----------+
          |
          v
+----------------------------+----------------------------+
|                     PLAYER SYSTEM                       |
|  +-------------------+   +----------------------------+ |
|  |  KIT / INPUT      |   | PROGRESSION AXES           | |
|  |  (light/heavy)    |   | - Power                    | |
|  |  (spell/dash/ult) |   | - Combat Depth             | |
|  +---------+---------+   | - Style (Instinct/Tact.)   | |
|            |             +-------------+--------------+ |
|            v                           |                |
|   +--------+------------+              | influences     |
|   | IN-RUN UPGRADE CORE |<-------------+----------------+
|   | - Personal Augments |
|   | - Party Accords     |
|   +---------+-----------+
|             |
+-------------+-------------------------------------------+
              |
              v
      +-------+--------------------------------+
      |            RUN / TRIAL SYSTEM          |
      |----------------------------------------|
      | Run Structure:                         |
      | - Phase timeline                       |
      | - (optional) room graph                |
      |----------------------------------------|
      | Wave Engine:                           |
      | - Spawn scripts                        |
      | - Enemy scaling                        |
      |----------------------------------------|
      | Co-op Layer:                           |
      | - Enemy scaling by player count        |
      | - Team events                          |
      +-----------------------+----------------+
                              |
                              v
                 +------------+-------------+
                 |       ENEMY SYSTEM       |
                 | - Enemy tiers            |
                 | - Behaviors              |
                 | - Boss phases            |
                 +------------+-------------+
                              |
                              v
                       +------+------+
                       |  REWARDING  |
                       |   SYSTEM    |
                       | - XP        |
                       | - Drafts    |
                       | - Meta currency|
                       +-------------+
```

---

## Expanded System Map

### A. PLAYER SYSTEM

* **Kit Layer:** light, heavy, spell, dash, ultimate, aim model.
* **Progression Axes:** Power, Combat Depth, Style.
* **In-Run Upgrades:** personal augments, party accords.

### B. RUN / TRIAL SYSTEM

* **Run topology:** phase timeline or room graph.
* **Wave Engine:** scripts, pacing, elite/boss injection.
* **Co-op:** rescue/defend/channel events.
* **Difficulty Modifiers:** density, damage, HP, curses, hazards.

### C. ENEMY SYSTEM

* Tier 1–3, elites.
* Behaviors: melee, ranged, homing, stun, DoT, summoner, AoE.
* Boss phases with armor/frenzy/vulnerability windows.

### D. UPGRADE SYSTEM

* Archetypes: flat, %, on-hit, on-kill, crit, aura, AoE, chain, transformations.
* Draft engine with rarity and pools.

### E. META SYSTEM

* Meta grid/tree.
* Stats, unlocks, preferences, currencies.

### F. REWARD SYSTEM

* XP curve.
* Draft triggers.
* Meta currency gains.

---

## Run Flow (Event Graph)

```
START TRIAL
  |
  v
INITIALIZE RUN VARIABLES
  |
  v
PHASE / ROOM SELECTION
  |
  v
SPAWN WAVE
  |
  v
COMBAT LOOP
  |
  v
WAVE COMPLETE
  |
  v
UPGRADE DRAFT
  |
  v
(loop until boss)
  |
  v
BOSS PHASES
  |
  v
END OF RUN
  |
  v
META REWARDS
```

---
