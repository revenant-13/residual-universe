# 07 — Open Questions

Universe-level only. Game-local opens stay in Spacesim specs and ASIWars `docs/07-open-questions.md`.

When something here locks, move it into the owning 01–06 file, tag it, and strike the row.

## A. Still genuinely open

| # | Question | Current lean | Blocks |
| --- | --- | --- | --- |
| O1 | Soft ticker: keep **bits** and **Credits**, or one Residual ticker? | Dual tickers, convert at legal berth | Resource bridge UX |
| O2 | Conversion rate / fees for bits ↔ Credits and mat uplift | Small fee as sink; tune later | Economy |
| O3 | Relocate cooldown / cost / quality drop | Real cost, not a hop tax that kills fun | One-claim honesty |
| O4 | Null-sec planetary law | Harsher low-sec (worse timers, no NPC desk Focus) until specified | Map |
| O5 | How many inhabitable planets, and are they unique-per-universe or instanced plots on a planet? | Handful of named planets; plots may instance underneath (ASIWars instance-everything) | Claim UX |
| O6 | Abandoned plot linger vs instant teardown | Short wreckage linger, then teardown | Relocation feel |
| O7 | Emergency Evacuate without a living berth | Allowed, **lossy** | Outpost death |
| O8 | Exact **async** command set (what is legal undocked) | Status + standing-order tweaks + one-shot Protocols; no layout/raid commit/Model workshop | U6/U7 boundary |
| O9 | Bloom windows vs ground unique mats (dual source forever?) | Dual source at first; blooms must not out-print uniques; may phase down | Spacesim PI |
| ~~O10~~ | ~~Visibility of a claimed planet / who~~ | **Settled U16.** Claim existence may be knowable in local. **Who** is not public. Violence writes a **Contact**. See [08](08-origin-and-founding.md) / [04](04-claim-and-focus.md). | — |
| O11 | Can space assets attack another Residual’s **orbital** claim / interdict Evacuate? | Yes in low-sec. High-sec CONCORD still applies. | Cross-mode PvP |
| O12 | Corp / clan / alt extra claims | Personal Residual = one. Corps later. | U2 scope |
| O13 | Physical monorepo vs stay dual-repo | Stay dual-repo until handoff packages exist | Tooling |
| O14 | Client shell: two URLs vs one app two modes | Two URLs is fine for prototype | Focus UX |
| O15 | Pack-out capacity / time for Evacuate | First low-sec drop `[LEANING]` **1–2** Vessels + Open Models (U16). Later relocates may pack more. Should hurt; should not brick. | Relocation |
| O16 | Clinic density, Volunteer odds, refusal rate | ASIWars `[GAME]` when Clinic is cited; universe only requires volunteer + legal refusal (U14) | Native onboard feel |
| O17 | Pedigree of evacuated Licensed Users | Keep a license tag vs fold into `Trained` after first relocate | Evacuate / market |
| O18 | Chip name: **NeuralSync** vs WellStream-only | Dual: chip = NeuralSync, platform = WellStream. Iterate the chip string, not the concept | Copy |
| O19 | Distill cost / caps so high-sec Closed Distill is not a Model-Hub wage | Real sink; maybe per-teacher cooldown. Closed skill ceilings stay instructional (U4) | U15 faucet |
| O20 | Flee catch math (speed, haul penalty, nerve, hunter Open) | Catchable; fail = Hunt. Tune so flee is a trade, not a teleport and not a death sentence | U16 |

## B. Explicitly not open (do not re-litigate here)

U1–U16 in [02-locked-rules.md](02-locked-rules.md). Soft influence primary. Ship stays in space. Docked-for-full-focus. One colony. High-sec limited permanent option. Low-sec outpost gate. Hybrid stack. This repo as universe authority.

**Settled 2026-08-28** (see [08-origin-and-founding.md](08-origin-and-founding.md)): first humans are a **high-sec licensed kit**, not an outpost drop and not a Residual clone. Native chips are **volunteer clinic only**. Felt goal is **sequenced**: stewardship garden → contested extractor that feeds space. Voxel wars interrupt; they are not the north star. High-sec factory Models are **Closed** (region-locked). **Distill** writes the first portable **Open** original. Closed never Evacuate. Low-sec drop is a **tiny party**; Open Models decide **Hold / Flee / Hunt**. **Hold** is anonymous. **Hunt** (and caught flees) write Contacts. Targeted raids require a name.

Engine merge as a *starting* move is a **non-goal**. Revisit only after both MVPs and a real seam.

## C. Owned elsewhere

| Topic | Home |
| --- | --- |
| Protocol math, Zone types, Model Hub, raid intents | ASIWars `docs/systems/` |
| Compact outpost recycle, wells, residue | Spacesim `docs/superpowers/specs/2026-08-20-compact-outposts-design.md` |
| Bloom pins, hopper, sludge | Spacesim `docs/superpowers/specs/2026-08-16-planetary-pads-design.md` |
| bits / USDC / no printer | Spacesim `docs/superpowers/specs/2026-08-12-spacesim-p2e-economy.md` |
| Deterministic instance ticks | ASIWars `docs/03-deterministic-simulation.md` |
| Nakama vs Colyseus vs Voxelize split | ASIWars `docs/08-architecture-and-stack.md`, Spacesim design spec |
| Origin myth, licensed kit, volunteer clinic, Closed/Open Distill, field Contacts | This repo [08-origin-and-founding.md](08-origin-and-founding.md). ASIWars owns Clinic **sim**, Distill math, and field-encounter resolution when cited. |

## How to close a question

1. Decide in conversation or playtest.
2. Patch the owning 01–06 or 08 file with `[LOCKED]` or `[LEANING]`.
3. Strike the row here and link the file heading.
4. If Spacesim or ASIWars must change, note it in that game’s design log — do not silently fork.
