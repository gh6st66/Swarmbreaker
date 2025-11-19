# SwarmBreaker

SwarmBreaker is a rogue-lite action RPG prototype inspired by games like *Sworn* and *Halls of Torment*. This repo combines a small Pygame-based survivor prototype with higher-level design docs that describe the long-term Unity-driven engine and progression systems.

> Status: early prototype + design spec. The Pygame game is for feel/flow exploration; the docs describe the intended full engine.

---

## Features

- Top-down survivor-style combat with kiting and crowd pressure
- Simple XP, leveling, and random upgrade system
- Shrinking arena pressure over a 20-minute run
- Data-backed design docs for tick loop, progression, and content

---

## Project Structure

- `game/`
  - `src/`
    - `main.py` – Pygame game loop, player/enemy/orb logic, arena shrink, waves
    - `map.py` – base map class (layout, obstacles, spawn points)
    - `maps/cursed_grove.py` – example “Cursed Grove” map with maze-like obstacles
    - (additional modules for player, enemies, UI, upgrades, etc.)
  - `tests/` – `pytest` suite for core gameplay behaviors
- `docs/`
  - `Game_Overview.md` – high-level game concept and system snapshot
  - `Swarmbreaker_master_spec.md` – engine/tick-loop, entities, echoes
  - `Swarmbreaker_progression.md` – XP curve, torment scaling, economy, drafting
  - `Branch_Game_Spec_Notes.md`, `index.md`, etc. – additional design notes

---

## Getting Started

### Requirements

- Python 3.10+ (recommended)
- [Pygame](https://www.pygame.org/news)
- `pytest` (for running tests)

Install dependencies (example):

```bash
pip install pygame pytest
Run the Game (Pygame Prototype)
From the repo root:

cd game
python -m game.src.main
If your Python path isn’t configured for packages, you can also run:

cd game
python src/main.py
You should see a window with:

A player square you move with the arrow keys
Waves of enemies spawning from map-defined points
XP orbs dropping and leveling/upgrades over time
A shrinking arena over a ~20-minute run
Running Tests
From the repo root:

cd game
pytest
The tests cover:

Player/enemy collisions and health loss
Game-over behavior at 0 HP and run timeout
XP gain and level-up logic
Arena shrink math and out-of-bounds damage
Map behaviors and upgrades (via dedicated test modules)
Design Docs & Engine Vision
While the current prototype is in Pygame, the long-term vision is a Unity runtime with a documented engine core:

Fixed-tick loop with defined system order (modifiers → input → cooldowns → spawns → movement → collisions → damage → echoes)
Data-driven heroes, enemies, abilities, and maps
Echo-based observability for debugging, analytics, and (where useful) replays
Progression and economy tuned around ~20–25 level-ups per run
Start here if you’re exploring the design:

docs/Game_Overview.md
docs/Swarmbreaker_master_spec.md
docs/Swarmbreaker_progression.md
docs/index.md (when filled out) for a system map
Contributing
Keep gameplay changes small and test-backed (game/tests/).
When modifying core systems (tick order, progression, content structure), make sure changes are consistent with the docs in docs/ or update the docs accordingly.
Prefer refactoring toward modular code (player.py, enemy.py, map.py, upgrades.py, etc.) rather than growing main.py.
Roadmap (High-Level)
Refine and modularize the Pygame prototype (separate engine vs. presentation)
Align prototype logic more closely with the documented tick loop and echo system
Expand maps, enemy types, and upgrade variety
Integrate or mirror key systems in a Unity-based runtime
