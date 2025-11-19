# 

Guidelines for AI agents and automated tools working in this repository.

## Scope & Layout

- This file applies to the entire repository.
- High-level game and engine design lives under `docs/` (e.g. `docs/Swarmbreaker_master_spec.md`, `docs/Game_Overview.md`, `docs/Swarmbreaker_progression.md`).
- The current playable prototype lives under `game/` (Pygame-based).
- Tests for the prototype live under `game/tests/`.

## General Principles

- Prefer small, focused changes that respect the existing structure.
- Keep code consistent with surrounding style rather than introducing new patterns ad hoc.
- Do not add licenses or copyright headers.
- Do not introduce new external dependencies without a clear reason and minimal footprint.

## Documentation

- Treat the specs in `docs/` as the conceptual source of truth for systems (tick loop, progression, entities).
- If code changes materially diverge from these specs, either:
  - Align the code with the spec, or
  - Clearly update the relevant doc section to match the new reality.
- When in doubt, add short, targeted notes rather than large rewrites of design docs.

## Python Game Prototype (`game/`)

- Language: Python 3, using Pygame.
- Style:
  - Follow PEP 8 where practical (snake_case, clear names, 79–100 column soft limit).
  - Avoid one-letter variables except for obvious loop indices.
  - Keep game logic testable and avoid unnecessary globals; when touching `main.py`, prefer moving logic into dedicated modules (`player.py`, `enemy.py`, `map.py`, `upgrades.py`, etc.) over growing the monolith.
- Behavior:
  - Preserve existing gameplay semantics (movement feel, wave timing, arena shrink, XP gain) unless a task explicitly calls for a balance or design change.
  - When refactoring, keep the public-facing API of existing classes and functions stable or update all call sites and tests together.

## Testing

- Test framework: `pytest`.
- Existing tests under `game/tests/` should continue to pass after changes.
- When modifying gameplay logic or adding features:
  - Add or extend tests in `game/tests/` that cover new behaviors.
  - Do not weaken or remove assertions without a strong, documented reason.
- Prefer small, fast unit tests over large integration tests for the Pygame prototype.

## Files & Structure

- New modules should live alongside related code (`game/src/` for core gameplay, `game/src/maps/` for additional maps, etc.).
- Keep module responsibilities narrow (e.g. enemies, player, upgrades, UI separated).
- Avoid large, multi-purpose “god objects”; pull out helpers or small classes instead.

## Tooling & CLI

- Any future tooling or CLIs should keep a clear boundary between:
  - Simulation/engine code,
  - Content/data,
  - Orchestration/CLI entry points.
- Follow the patterns described in the docs if adding TS/Node tools or similar (data-driven, spec-aligned, deterministic where practical).

