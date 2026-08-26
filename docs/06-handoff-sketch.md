# 06 — Handoff Sketch

Design contracts for the seam. Not a schema dump. Stubs may be local mocks until Nakama exists. ASIWars is young enough to bake these into its command surface now; Spacesim adds the dock-side verbs.

Universe authority: the **names, preconditions, and effects**. JSON fields and RPCs are `[LEANING]` until a glue spec lands.

## Shared meta objects `[LEANING]`

Held in Nakama (or equivalent). Not in a Colyseus room and not in a Voxelize world as source of truth.

| Object | Purpose |
| --- | --- |
| `residualId` | Single identity. |
| `activeColonyId` | Null or one. Enforces U2. |
| `colonySecBand` | `high` \| `low` (null later). |
| `planetId` / `systemId` | Where the claim sits. |
| `linkedOutpostId` | Required for low-sec claim/Focus. |
| `docked` | Mirrored from space dock commit. |
| `berthKind` | `npc-station` \| `linked-outpost` \| `none`. |
| `focus` | `true` only if docked at a **legal** berth for this claim. |
| `hangarBridge` | Pending uplifts/downlifts. |

Room state is never the ledger (Spacesim hard rule). Ground instance state is never the Residual’s account (ASIWars instance-everything). Glue copies **intents** in; sims remain authoritative for their own ticks.

## Verbs

### Claim planet

**Intent:** Attach the Residual’s one colony slot to an inhabitable planet.

| | High-sec | Low-sec |
| --- | --- | --- |
| Must be | Docked at high-sec NPC station | Linked outpost online in system |
| `activeColonyId` | Must be null | Must be null |
| Effect | Create/attach colony instance; set meta | Same + bind `linkedOutpostId` |

Fails closed: already claimed by you, planet not inhabitable, wrong berth, outpost missing.

Does **not** auto-Focus. Claim then **Dock & Focus** (or a combined UI button that does both if preconditions hold).

### Dock & Focus Colony

**Intent:** Full Director interaction. U6.

Preconditions:

1. Docked.
2. Active colony exists.
3. Berth is legal for that colony (U4/U5).

Effects:

- `focus = true`.
- Ground API enables full command set.
- Client switches to ASIWars Director (or embedded equivalent).
- Hull remains docked and safe.

Space server **refuses undock** while `focus` (or auto-Returns first). `[LEANING]` auto-Return then undock.

### Return to Ship

**Intent:** Leave Director without moving the hull.

Effects:

- `focus = false`.
- Client back to Spacesim docked UI.
- Pending hangar transfers may complete.
- Colony continues (now async from the Residual’s POV, still ticking).

### Undock

Spacesim native. Additional universe rule: illegal or sequenced while `focus`. After undock: space primacy, U7 async colony.

### Evacuate

**Intent:** End the claim and take what you can.

Preconditions: `[LEANING]` must be docked at legal berth for a clean pack-out. Emergency evacuate from Focus while the outpost is dying is allowed and **lossy**.

Effects:

- Select Vessels, Models, resources into hangar (caps, time, cost `[OPEN]`).
- Clear `activeColonyId`, `linkedOutpostId` bind, `focus`.
- Colony instance tears down or remains as abandoned wreckage `[LEANING]` wreckage linger.
- Assets now follow cargo/hangar law. Gankable once undocked.

### Resource / Vessel transfer

**Intent:** Move stock across the seam at a legal berth.

| Direction | Typical payload |
| --- | --- |
| Uplift | Planetary mats, maybe Credits→bits, Models as artifacts |
| Downlift | Tools, compute hardware, ammo analog, food analog, bits→Credits |

Vessels in hangar are **in transit**, not crew (U9). They do nothing for DPS.

Async **standing export** into the outpost/station hangar is allowed so roamers are not a bottleneck. High-sec export remains trash-capped.

### Status query

Read-only from either client: colony condition, protection timer, live contest, outpost HP, pending transfers. Menu-first. Agent-legal.

## Client mode switch `[LEANING]`

Two clients (or two modes in one shell) is fine. The universe does not require a single WebGL canvas.

```
[ Spacesim client ]  --dock+focus-->  [ ASIWars console ]
[ Colyseus room  ]                    [ Voxelize instance + sim API ]
         \                               /
          \                             /
               [ Nakama / glue ]
```

A crude prototype is enough to validate U6: dock in Spacesim → set focus flag → open Director → issue one Protocol → Return → see mock mats in hangar.

## Ground command gating `[LOCKED]`

ASIWars command/query API must distinguish:

| Class | When legal |
| --- | --- |
| **Full Director** | `focus && docked && legalBerth` |
| **Async** | Colony exists; Residual may be anywhere |
| **Read / replay** | Always, if you own or are raid-watching per ASIWars rules |

Full Director examples: layout, training programs, raid commit, Model workshop, Zone paint.

Async examples `[LEANING]`: standing-order tweaks, one-shot Protocol, abort contest, Evacuate **request** (may still need a berth to complete).

If glue is down, fail closed: no Focus, colony keeps last standing orders.

## Space server gating `[LOCKED]`

| Action | Extra universe check |
| --- | --- |
| Undock | Deny or Return-then-undock if `focus` |
| Dock at outpost | May advertise “Focus Colony” if this outpost is `linkedOutpostId` |
| Recycle outpost | Cannot complete while a Residual is Focused docked inside (`[GAME]` already: recycle vs docked). Universe agrees. |
| Destroy / capture outpost | Breaks legal berth. Focused Residual is kicked to Return; claim becomes insecure; Evacuate pressure. |

## Event names (suggested)

Stable strings for both command surfaces. Rename only with a doc bump.

```
universe.claim_planet
universe.focus_colony
universe.return_to_ship
universe.evacuate
universe.transfer_uplift
universe.transfer_downlift
universe.status
```

Payloads carry `residualId`, `planetId` / `colonyId`, `berthId`, idempotency keys. Ground sim logs them on the instance input log at the effective tick (ASIWars determinism). Space dock/undock remains Spacesim dock-commit.

## Prototype order (no code in this repo)

1. Meta stub: one Residual, one colony flag, focus boolean (file or Nakama storage).
2. Spacesim: docked action **Inhabit / Focus Colony** calls the stub.
3. ASIWars: refuse full commands unless stub says focused; accept async always.
4. Mock uplift: Focus → tick a Collection Zone → Return → grant a hangar stack the space industry already consumes (or a tagged dummy).
5. Only then: real unique ids, outpost bind, Evacuate.

This is the first **merged** playable moment. It does not need a monorepo.

## What not to build yet

- Unified engine.
- Walking Residual on voxels.
- Crew-on-hull.
- Two colonies.
- Focus from space while undocked.
- Planet-unique faucet with no consumer recipe.
