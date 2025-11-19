# Documentation Home

This folder gathers canonical specifications and design notes for the SwarmBreaker.

## CLI + Toolchain Guide

SwarmBreaker is driven directly by the runtime (for example, the Unity game build or editor) rather than a standalone deterministic CLI simulation.

If you are working in the companion TypeScript/Node tools for content validation or batch tests, use:

- Run `npm run cli -- <command>` to execute gameplay tools (parsers, validators, smoke-test harnesses, etc.) via `tsx` without compiling.
- Run `npm run cli:dist -- <command>` to compile with `tsc` and execute the Node binary that mirrors how these tools are packaged.
- The published `swarmbreaker` bin emitted by `npm pack` maps to `dist/src/cli.js`, which dispatches into `src/main.ts` to run tool flows, not an authoritative game simulation.
- `npm run build` still performs the full Vite pipeline; the CLI helpers intentionally skip it for faster iteration.

> TODO: Expand with ArchitectAgent-curated diagrams summarizing runtime  tools  content responsibilities and outstanding RFCs.
