# SwarmBreaker Master Specification

This document defines the core combat simulation model for the SwarmBreaker prototype. It codifies the tick loop, RNG usage guidelines, entity structures, combat resolution steps, spawning model, echo emission contract, and expectations for observability.

## Goals

- Clear and predictable ordering of core systems (modifiers, input, cooldowns, spawns, movement, collisions, damage).
- Pure data-driven entities that validate against `schemas/entities.schema.json`.
- A simulation core that can be driven by both the real-time runtime (Unity) and headless tooling where it is useful to do so.
- Echo streams that make state changes observable for debugging, analytics, and optional replay tooling, without requiring strict determinism.

## Engine Architecture

### Tick Loop

Simulation advances using fixed timesteps (default 60 ticks per second). Each tick executes in the following order:

1. Apply queued modifiers (difficulty, torment, flow mode).
2. Process player input auto-actions.
3. Advance cooldown timers.
4. Execute the spawn scheduler.
5. Integrate movement for all entities.
6. Resolve collisions.
7. Resolve damage and deaths.
8. Emit any queued state-change echoes.

### RNG and Randomness

- Randomness should use well-defined, engine-level RNG sources so tuning and analytics stay tractable.
- Where feasible, RNG usage order should be documented to keep behavior stable across versions, but strict bit-perfect determinism is not required.
- Tooling may choose to emit `rng` echoes (including consumed values) to aid debugging and approximate replay, but the runtime is not obligated to reproduce runs exactly from these values alone.

### Echo System

The engine can emit echo messages so runs are observable and, where practical, reconstructable for debugging or analysis. Core echo types include:

- `spawn(entity_id, position)`
- `despawn(entity_id)`
- `hit(source, target, amount)`
- `status_apply(entity, type, stacks)`
- `rng(value)`
- `hero_init(hero_id, stats)` �?" emitted once per run after resolving the hero loadout.
- `xp_gain(amount)`
- `level_up(level)`
- `reward_pickup(type, amount)`
- `run_end(victory|death)`

## Entities

### Hero

- Loaded from JSON based on `entities.schema.json`.
- Includes base stats (HP, damage, speed, attack rate), ability sets, traits, and optional class tags.
- CLI nouns select the hero; when omitted the starter hero (`wanderer`) is used. Unknown hero IDs must error before simulation begins.

### Enemy

- Defined by tier, behaviors, stats, and AI patterns.
- Supported AI patterns:
  - **Chase:** move toward the hero.
  - **Ranged:** maintain distance and fire projectiles.
  - **Charge:** wind-up followed by a dash.
  - **Boss FSM:** multi-phase scripted behaviors.

### Ability

- Fully data-driven definitions.
- Contains base damage, type, cooldown, range, area, and projectile count.
- May apply status effects (burn, frost, electrify, affliction, etc.).

### Item

- Provides passive stat modifiers or procedural effects applied to heroes.

## Combat Systems

### Collision Model

- Entities use circle-based hitboxes.
- Projectile versus enemy checks use a spatial grid for efficiency.

### Damage Resolution Order

1. Calculate base damage.
2. Apply hero and ability multipliers.
3. Apply enemy defense reductions.
4. Roll for critical hits.
5. Apply any resulting status effects.
6. Emit a `hit` echo summarizing the event.

### Status Effects

Supported statuses include Burn (damage over time), Electrify (chain lightning), Frost (slow), Fragile (increased damage taken), and Affliction (% max HP damage). Each status defines its own stacking behavior.

## Spawn Scheduler

- Driven by data-defined wave tables.
- Supports timed bursts, continuous generation, elite and boss event scheduling.
- Emits `spawn` and `despawn` echoes for lifecycle tracking.

## Run Lifecycle

1. Initialize the run with the hero, map, seed, and modifiers from the parser.
2. Spawn the initial wave per map configuration.
3. Execute the main tick loop.
4. Spawn a miniboss at the designated timestamp.
5. Spawn the final boss near the end of the run.
6. Emit `run_end` once the hero wins or dies.
