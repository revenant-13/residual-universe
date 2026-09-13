# Residual Universe

Canonical **shared design layer** for **NeuralSync** — [Spacesim](https://github.com/revenant-13/spacesim) (space) and [ASIWars](https://github.com/revenant-13/asiwars) (ground). Players see NeuralSync. Engineers see these repo names.

This repo is the **authority on universe-level rules**: who the player is, how a colony is born, how space and ground relate, claim/focus/evacuate, the one-colony cap, high-sec vs low-sec planetary law, and the Trace → LoRA → Kernel resource bridge. Project-specific implementation (combat ticks, Protocol math, Voxelize instances, Colyseus rooms, Kernel hunt) stays in the respective game docs.

It is **not** a code merge. The two engines stay separate. The merge that matters first is narrative, terminology, locked rules, and the handoff surface.

| Layer | Repo | Role |
| --- | --- | --- |
| Space continuum + combat sandbox | [spacesim](https://github.com/revenant-13/spacesim) | Residual presence in ships, Kernel, LoRA manufacture |
| Planetary colony / contested extraction | [asiwars](https://github.com/revenant-13/asiwars) | Closedex: Residual influence over NeuralSynced Vessels; Sync Trace emission |
| Universe rules (this repo) | residual-universe | Shared identity, claim law, focus/security model, Trace → LoRA bridge |

## How to read

Start here, then the numbered files. Each file is independently editable.

| File | Owns |
| --- | --- |
| [docs/01-vision.md](docs/01-vision.md) | Protagonist, dual-mode fantasy, tone, non-goals |
| [docs/02-locked-rules.md](docs/02-locked-rules.md) | Universe laws tagged `[LOCKED]` |
| [docs/03-terminology.md](docs/03-terminology.md) | Residual language + Spacesim ↔ ASIWars map |
| [docs/04-claim-and-focus.md](docs/04-claim-and-focus.md) | One claim, high/low-sec planets, docked-for-focus, state machine |
| [docs/05-resource-bridge.md](docs/05-resource-bridge.md) | Sync Traces → LoRAs → Kernel risk; stations as industrializers |
| [docs/06-handoff-sketch.md](docs/06-handoff-sketch.md) | Claim / Focus / Return / Evacuate verbs and contracts |
| [docs/07-open-questions.md](docs/07-open-questions.md) | What is still undecided at universe level |
| [docs/08-origin-and-founding.md](docs/08-origin-and-founding.md) | Founding myth, licensed kit, volunteer clinic, Closed/Open Models, NeuralSync / Closedex / ClosedAI, field Contacts, sequenced goal |
| [art/](art/) | Blender sources for Spacesim hulls, drones, Kernel, Atrium station, and stargate. Spec: [2026-09-07-hull-silhouette-donors-design.md](docs/superpowers/specs/2026-09-07-hull-silhouette-donors-design.md) |

## Status legend

Every universe claim is tagged so agents and humans know what they may change:

- **`[LOCKED]`** — changing it changes the universe. Both games must honor it.
- **`[LEANING]`** — current recommendation; reversible without a pillar fight.
- **`[OPEN]`** — undecided; variants live in [07-open-questions.md](docs/07-open-questions.md).
- **`[GAME]`** — owned by Spacesim or ASIWars, not this repo. Cited for context only.

## Authority split

```
residual-universe     universe identity, origin/founding, claim law, focus/security, Trace → LoRA bridge, NeuralSync / Closedex nouns
spacesim docs         space combat, navigation, markets, outpost *implementation*, bloom windows, Hive org
asiwars docs          Protocols, Models, Vessels, Zones, raids, scarring, deterministic sim
```

If a `[LOCKED]` rule here conflicts with a local game doc, **this repo wins** on universe law. Mark the local conflict, then update the game doc. Do not silently fork the rule.

Shipped title **NeuralSync** does not rename this repo. `wellstream-*` factory ids in ASIWars may stay until a game rename; universe copy says ClosedAI.

If the conflict is an implementation detail (how an outpost recycles, how a Protocol rolls), the **game doc wins**. Do not drag those numbers into this repo.

## How to extend

This is a living GDD. Keep it modular.

1. **New universe rule** — add it to `02-locked-rules.md` with a status tag and a one-line rationale. If it needs a home of its own, add `docs/08-….md` and link it from this README.
2. **New noun** — add it to `03-terminology.md` with Spacesim and ASIWars mappings (or “n/a”).
3. **New verb on the seam** — add it to `06-handoff-sketch.md` (name, preconditions, effects, who owns the sim).
4. **Settled open question** — move the resolution into the owning file, tag it `[LOCKED]` or `[LEANING]`, and strike it in `07` with a pointer.
5. **Do not** copy Spacesim combat specs or ASIWars Protocol math into this repo. Link them.

Every file should stay readable in isolation. Prefer short decision tables over narrative recap.

## Stack (context, not a rewrite)

`[LOCKED]` Hybrid, no engine merge:

- **Space:** Colyseus + TypeScript tick sim (Spacesim).
- **Ground:** Voxelize (Rust) + menu command/query (ASIWars).
- **Glue:** Nakama (or equivalent) for Residual identity, one-colony claim, linked outpost, inventory bridge, focus/docked state.

Code and schema stubs live in the game repos. This repo only specifies the contracts at a design level ([06-handoff-sketch.md](docs/06-handoff-sketch.md)).

## Source conversation

Design lock from the shared-universe conversation (2026-08-26): [AI Space-Ground Hybrid Game](https://grok.com/share/bGVnYWN5_ad47469d-2beb-4dd1-be63-b8851ef4a8d3). Origin and founding (U13/U14, licensed kit, volunteer clinic, sequenced goal) locked 2026-08-28 in [docs/08-origin-and-founding.md](docs/08-origin-and-founding.md). Kernel / LoRAs / Sync Traces (U17), NeuralSync as shipped title + chip, Closedex by ClosedAI, unique-mat demotion locked 2026-09-02. Spacesim K1–K3 shipped the space side. **Hive** (player org, EVE corp analog) named 2026-09-05; H1–H2 shipped `[GAME]`. O12 stays open: no hive-held colony.
