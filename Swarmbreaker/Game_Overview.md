# Game Overview

SwarmBreaker is a rogue-lite action RPG inspired by games like Sworn and Halls of Torment. Its combat, progression, and content are defined via the canonical Codex bundle and realized in a real-time Unity runtime. Earlier iterations experimented with a fully deterministic simulation layer; SwarmBreaker now treats the runtime as authoritative, with tooling hooks used for debugging, replays, and automated verification where practical rather than strict bit-perfect determinism. This overview gives architects and agents the high-level picture that the missing PDF used to supply, emphasizing how the Unity runtime, tick loop, and progression systems interlock.

## Vision

- **Real-time, run-based combat:** SwarmBreaker focuses on moment-to-moment action-dodging, kiting, crowd control, and build expression in dense enemy swarms rather than fire-and-forget auto-battles.
- **Documented engine core for tools:** Under the hood, a tick loop (`docs/Swarmbreaker_master_spec.md`) defines the order in which combat systems run. Unity drives this loop and integrates input, physics, and presentation. Tools may approximate this loop for balance testing and automated runs, but the runtime is authoritative and strict determinism is not required.
- **Data-driven content:** Heroes, enemies, abilities, and maps live in JSON (and Unity ScriptableObjects) that validate against `schemas/entities.schema.json`, letting ContentAgent iterate without touching engine code.

## Systems Snapshot

- **Player & input layer:** The Unity runtime owns real-time input (keyboard/mouse/controller), movement, and aiming. Player kits (weapons, spells, dash, ultimates) map onto the deterministic combat systems.
- **Tick loop order:** Each tick applies modifiers, advances abilities and cooldowns, runs the spawn scheduler, integrates movement, resolves collisions and damage, then emits echoes (`run_init`, `hero_init`, `spawn`, `hit`, `status_*`, `xp_gain`, `reward_pickup`, `run_end`).
- **Hero & enemy models:** Heroes have level-based damage, attack rates, statuses, and signatures; enemies have tiers, resistances, AI roles (chaser, ranged, charger, boss), knockback resist, and defense values per `docs/Gap_Fill_and_Overlooked_Data.md`.
- **Spawn & hazard layer:** Maps describe timed waves, continuous pools, and elite chances. The scheduler also injects miniboss/boss entries and temporary hazards so runs have pacing, density, and objectives beyond pure DPS.
- **Progression loop:** XP, level-ups, torment scaling, and reward drafts feed into the meta system described in `docs/Swarmbreaker_progression.md`. XP gain and level-ups emit echoes for traceless QA and tie into drafts/reward pickups.

## Runtime guarantees

- **Echo-first telemetry:** Every significant event (random draw, status application, hit, spawn, run end) is logged to an echo stream for analytics and debugging purposes.
- **Phase-based rollout:** `docs/Gameplay_Engine_Rollout.md` governs the engine migration (tick/movement → combat/status → spawns/hazards → progression/economy) and spells out the test/replay suite (`docs/gameplay_engine_tracker.md`, `RFC-SB-003`).
- **Agent coordination:** ArchitectAgent owns the specs/manifest, Engine/Client agents implement respective layers, ContentAgent supplies JSON. The agent charter `instructions/agents_swarmbreaker.md` and instructions `instructions/codex_instructions.md` explain those boundaries.

## Next steps for new contributors

1. Read `docs/index.md` for the system map connecting meta, player, run, enemy, and reward systems.
2. Follow `docs/Gameplay_Engine_Rollout.md` phases before modifying engine logic to stay aligned with project goals.
3. Validate all new content schemas against `schemas/entities.schema.json` before adding abilities, bosses, or waves.
