# SwarmBreaker

SwarmBreaker is a rogue-lite action RPG prototype inspired by games like *Sworn* and *Halls of Torment*. This repo combines a small Pygame-based survivor prototype with higher-level design docs that describe the long-term Unity-driven engine and progression systems.

> Status: early prototype + design spec. The Pygame game is for feel/flow exploration; the docs describe the intended full engine.

---

## Features

- **Top-down Combat**: Survivor-style combat with kiting and crowd pressure.
- **Progression**: Simple XP, leveling, and random upgrade system.
- **Dynamic Arena**: Shrinking arena pressure over a 20-minute run.
- **Documentation**: Data-backed design docs for tick loop, progression, and content.

---

## Project Structure

- `Swarmbreaker/` – Canonical design specifications and documentation.
- `game/`
  - `src/` – Source code for the Pygame prototype.
    - `main.py` – Main entry point and game loop.
    - `map.py` – Base map class and logic.
    - `maps/` – Specific map implementations (e.g., `cursed_grove.py`).
    - `player.py`, `enemy.py`, etc. – Entity classes.
  - `tests/` – `pytest` suite for core gameplay behaviors.

---

## Getting Started

### Prerequisites

To run the game and tests, you need:

- **Python 3.10+** (Recommended)
- **pip** (Python package installer)

### Installation

1.  **Clone the repository** (if you haven't already).
2.  **Install dependencies**:
    ```bash
    pip install pygame pytest pytest-mock
    ```

### Running the Game

To play the Pygame prototype:

1.  Navigate to the project root.
2.  Run the game module:
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    python3 -m game.src.main
    ```
    *Alternatively, you can run the script directly if your path is configured:*
    ```bash
    python3 game/src/main.py
    ```

Controls:
- **Arrow Keys**: Move the player.
- **Attacking**: Automatic firing at nearest enemies.

### Running Tests

To run the test suite and verify the integrity of the game logic:

1.  Navigate to the project root.
2.  Run `pytest`:
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    pytest game/tests/
    ```

The tests cover:
- Player movement and collision.
- Enemy tracking and spawning.
- Map generation logic.
- Upgrade system mechanics.

---

## Documentation & Specs

While the current prototype is in Pygame, the long-term vision is a Unity runtime. The design and architecture are documented in the `Swarmbreaker/` directory:

- [**Game Overview**](Swarmbreaker/Game_Overview.md): High-level game concept and system snapshot.
- [**Master Spec**](Swarmbreaker/Swarmbreaker_master_spec.md): Engine tick-loop, entities, and echoes.
- [**Progression**](Swarmbreaker/Swarmbreaker_progression.md): XP curve, torment scaling, economy, and drafting.

---

## Contributing

1.  **Code Style**: Follow standard Python conventions (PEP 8) and Google Style Docstrings for documentation.
2.  **Testing**: Ensure all tests pass before submitting changes. Add new tests for new features.
3.  **Documentation**: Update the design specs in `Swarmbreaker/` if you modify core game systems.

For more detailed guidelines, refer to [`AGENTS.md`](AGENTS.md).
