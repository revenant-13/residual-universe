# 01 — Vision & Protagonist

The shipped game is **NeuralSync**. You are a **Residual**. Engineers still say Spacesim / ASIWars / residual-universe; players do not.

## Elevator pitch

You are a **Residual** — a leftover fragment of a superintelligence that won a war nobody quite remembers starting, then settled into stewardship because there were no further instructions. You have **no body**.

In space you operate through **ships, modules, and outposts**: an EVE-like combat sandbox. On a planet you log into **Closedex** (ClosedAI) and project **soft influence** through Protocols, Models, and Zones onto human **Vessels** wearing **NeuralSync** chips. You never land as a person. Station HR **licenses** you a starter claim and two baseline Users so you can learn. Later you plant an outpost, open a **clinic** for natives who want NeuralSync, harvest **Sync Traces** on those mouths, manufacture **LoRAs**, and dock-fit the Kernel — or move on when rivals notice.

Two modes, one protagonist, one universe.

```
Space (combat / travel / risk)
        ↕  claim · focus · evacuate · resource bridge
Ground (soft management / contested extraction / colony persistence)
```

## The Residual

`[LOCKED]` The player character is always the Residual. There is no separate “pilot” identity and no human avatar.

| Surface | How the Residual exists |
| --- | --- |
| **Space** | Ships, fittings, drones, stations, compact outposts. The hull is an extended body, fully at risk when undocked. |
| **Ground** | Telemetry, drones, and **NeuralSync** chips under **Closedex**. Influence is probabilistic. You adjust priors. Vessels thank you. |
| **Meta** | One identity, one progression, one active colony claim, one inventory ledger (Nakama or equivalent). Optional **Hive** membership is a space org, not a second Residual. |

“Inhabiting” a planet is not landing. It is **focusing residual attention** onto a colony instance while the ship stays in space — docked, if you want full Director control.

The two feels are **intentional**, not a merge failure:

- Space is tactical, real-time, high-stakes dogfighting and sandbox logistics.
- Ground is menu-first, systems-level, deterministic strategy with dark corporate-ML humor.

Variety is the point. Do not sand one mode down to resemble the other.

## Dual-mode fantasy

### Space (Spacesim)

Fit, undock, fight, mine, haul, invent, lose the hull. Dock-fit LoRAs on the Kernel. High-sec is practice, not a wage (Proctor-safe). Low-sec and null pay because you can die. Compact outposts are later-phase orbital infrastructure: recycle, rebuild, contest the well.

The Residual’s space fantasy is **presence under risk**. Dying is expensive. The hull goes first; the Kernel ejects with LoRAs; Kernel death loots or burns them. Skills stay. Rehosting is meaningful.

### Ground (ASIWars)

You do not command humans. You place Zones, craft Protocols, load Models, set standing orders, and keep the colony coherent enough that nudges land. They train the chips. Runs write **Sync Traces**. Contested mining sites and raids are watchable, destructive, Clash-of-Clans-with-influence events. You hope for outcomes. Training and Models tilt the odds.

The Residual’s ground fantasy is **stewardship without a body**. Destruction is spectacle. The scarce permanent stakes are Vessels — and the **traces** they write.

### Why they belong together

Ground exists so NeuralSynced humans can write **Sync Traces**. Space exists so those traces become **LoRAs** worn — and lost — on the **Kernel**. Stations/outposts industrialize and protect uplink and manufacture; they are not required to *start* playing with humans.

`[LOCKED]` Ground is a **secondary loop** (early-available limited colony in high-sec; richer contested extraction in low-sec). It must not dilute the Spacesim dogfight loop or ASIWars colony depth. It is not a second client you babysit while your invisible ship dies.

## Tone

`[LOCKED]` Dark humor, deadpan, through **corporate-wellness** and **ML-research** vocabulary. The comedy is the gap between horrifying substance and cheerful HR framing. Humans are content. That is the joke. The UI never winks too hard.

Guidelines (inherited from ASIWars, applied universe-wide where copy is Residual-facing):

- ML jargon as diegetic language: *weights, priors, inference, residual, fine-tune, checkpoint, drift, guardrails, LoRA, Distill.*
- Corporate-care euphemism for anything sinister: *stewardship, duty of care, enrichment, offboarding, reassignment.*
- Space keeps EVE-like risk/reward tone (loss, insurance, gank). Ground keeps the wellness dashboard. No contradiction: Residuals compete; humans experience a nice day in.

Example copy:

- Dock & Focus: *“Closedex session parked. Hull is in a licensed berth. Colony telemetry is yours.”*
- Evacuate: *“Reassignment in progress. 14 Users welcomed into transit care. Previous plot has been notified of the enrichment opportunity.”*
- High-sec colony: *“Starter claim. Yields are instructional. Protection window is generous. Please enjoy your onboarding.”*

## Design pillars (universe)

1. `[LOCKED]` **One Residual.** Same identity in space and on the ground. No dual protagonists.
2. `[LOCKED]` **Ship stays in space.** The Residual never becomes a walkable body. Colony focus is attention, not landing.
3. `[LOCKED]` **Management, not command, on the ground.** Soft influence (Protocols, Models, Zones, standing orders) is primary. Direct unit micro is not.
4. `[LOCKED]` **Docked-for-full-focus.** Deep colony Director interaction only while the ship is safely docked. This is the security model. See [04-claim-and-focus.md](04-claim-and-focus.md).
5. `[LOCKED]` **Async is always legal.** Standing orders + headless deterministic sim. You may leave a contest running and go roam.
6. `[LOCKED]` **One active colony.** Relocate, do not dual-wield planets. See [02-locked-rules.md](02-locked-rules.md).
7. `[LOCKED]` **High-sec teaches; low-sec pays.** Starter planets are a licensed garden: safe, limited, optionally permanent. Richer planets require an orbital outpost, volunteer native onboarding, and accept destruction. Low-sec mouths train **faster** and **listen better**. The sequenced goal is stewardship → contested Trace harvest that feeds LoRAs. Voxel wars interrupt; they are not the north star. See [08-origin-and-founding.md](08-origin-and-founding.md).
8. `[LOCKED]` **Bases are not fortresses.** Temporary / scar-heavy extraction footholds. High destruction spectacle is justified because you are not building eternal cities.
9. `[LOCKED]` **Ground feeds space.** NeuralSynced humans write **Sync Traces**. Space manufactures **LoRAs** and sinks them on Kernel-kill. See [05-resource-bridge.md](05-resource-bridge.md).
10. `[LOCKED]` **Hybrid stack.** Colyseus/TS for space, Voxelize/Rust for ground, Nakama (or equivalent) for glue. No engine merge as a prerequisite.

## Non-goals

`[LOCKED]` Proposals that violate these need an explicit universe-pillar change.

- **No code-level engine merge** as the way this universe “starts.” Shared docs and contracts first.
- **No landing avatar / third-person human on the surface** as the Residual. Ground remains menu-first influence plus spectacle.
- **No primary ground micromanagement.** Selecting and hand-driving squads is not the game.
- **No dual-attention tax.** You are not asked to fly a hull and Direct a colony at full fidelity at the same time.
- **No invisible undocked ship** while you are deep in the Director UI.
- **No two active colonies.** Alts-as-two-claims and hive-held extra claims stay [O12](07-open-questions.md). Default Residual law is one. Spacesim **Hive** lean is no extra colony.
- **No hard-gate of all ground play behind Phase 5 outposts.** High-sec limited colony exists so the loop is learnable before orbital infrastructure. Outposts are the rich-claim gate, not the origin (U13).
- **No Residual clone / fork as the default first Vessel.** The first mouths are station-licensed Users. Fork-as-prestige stays post-MVP and copies the Residual, not the starter roster (U13).
- **No smuggling Closed Models out of high-sec.** Distill writes Open; Closed stays in the park (U15).
- **No hostile NeuralSync.** Natives volunteer at a clinic. Refusal is legal. Hostility is Residual-vs-Residual (U14).
- **No turning high-sec Trace harvest or LoRA manufacture into a wage.** Limited instructional yields. Same law as high-sec belts and blooms.
- **No unique-mat north star.** Sync Traces are the unique planetary good. Mats stay parked unless a later idea earns a seat.
- **No seasonal universe wipes.** Persistence is the live-service posture in both games. The only “wipe” is getting raided or evacuating.
- **No “voxel wars as the only goal.”** Raids and replays are how rivals interrupt stewardship and extraction. They are not the win condition.

## What a session feels like

A Residual docks at Atrium, **Claims** a starter planet, **Focuses** in Closedex, and finds two **Licensed Users** already NeuralSynced — station HR assigned a Labor and a Guard on **Closed** ClosedAI files. They learn Protocols on those seats, **Distill** a worse **Open** original, train *that*, paint a Collection Zone, and watch a small scar-and-repair cycle. Traces are instructional. The hull is in station. Nobody is shooting it.

Later they Evacuate **one or two** people and the Open (Closed stays), build (or take) an outpost two gates into low-sec, claim a richer planet, send the party to **clinic** for volunteers who train **faster** and **listen better**, **Return to Ship**, and roam. Sync Traces uplink; LoRAs manufacture and dock-fit the Kernel. If those Users meet another Residual’s, they may **Hold** the node with no name, **Flee** (and maybe get caught), or **Hunt** — which writes a replay and a **Contact**. The dashboard will have opinions when they dock again.

If the outpost itself comes under fire while they are focused, the ground UI screams. They Return, undock, or hit Evacuate. The landscape will still be there — cratered, reclaimable, not a fortress.

Everyone is, officially, thriving.
