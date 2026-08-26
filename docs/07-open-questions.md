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
| O10 | Visibility of a claimed planet on space overview | Claimed planets are knowable in local; intel on *who* `[LEANING]` public in low-sec | Multiplayer |
| O11 | Can space assets attack another Residual’s **orbital** claim / interdict Evacuate? | Yes in low-sec. High-sec CONCORD still applies. | Cross-mode PvP |
| O12 | Corp / clan / alt extra claims | Personal Residual = one. Corps later. | U2 scope |
| O13 | Physical monorepo vs stay dual-repo | Stay dual-repo until handoff packages exist | Tooling |
| O14 | Client shell: two URLs vs one app two modes | Two URLs is fine for prototype | Focus UX |
| O15 | Pack-out capacity / time for Evacuate | Should hurt; should not brick | Relocation |

## B. Explicitly not open (do not re-litigate here)

U1–U12 in [02-locked-rules.md](02-locked-rules.md). Soft influence primary. Ship stays in space. Docked-for-full-focus. One colony. High-sec limited permanent option. Low-sec outpost gate. Hybrid stack. This repo as universe authority.

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

## How to close a question

1. Decide in conversation or playtest.
2. Patch the owning 01–06 file with `[LOCKED]` or `[LEANING]`.
3. Strike the row here and link the file heading.
4. If Spacesim or ASIWars must change, note it in that game’s design log — do not silently fork.
