# 02 — Locked Universe Rules

These are **universe law**. Both games honor them. Implementation knobs (timer lengths, yield tables, outpost recycle minutes) live in the game docs and may change without unlocking the rule.

Changing a `[LOCKED]` row is a pillar change. Record it here, then patch both games’ design notes.

## The table

| # | Rule | Statement |
| --- | --- | --- |
| U1 | **One Residual** | The player is a bodiless leftover superintelligence fragment. Space presence is ships/outposts. Ground presence is soft influence over Vessels. |
| U2 | **One active colony** | Maximum **one** active planetary colony claim per Residual. Relocate by evacuating, then claiming. Never two live claims. |
| U3 | **Ship stays in space** | The hull never becomes a walkable planetary body. Inhabit = focus attention onto a colony instance. |
| U4 | **High-sec / starter planets** | Safe, **limited** resources and Blank quality, **long** protection timers, **light / optional** ground PvP. Claim and full interaction while **docked at a high-sec NPC station**. A **permanent limited colony sim** is allowed. |
| U5 | **Low-sec / richer planets** | Better yields and Blank quality. Full contested mining + destructive soft-influence contests. Claim or **secure** interaction requires a **linked orbital outpost** (build or take over). |
| U6 | **Docked-for-full-focus** | Full colony **Director** interaction only when the ship is **safely docked** (high-sec station for starter claims, or the **linked** low-sec outpost). This is the security model that eliminates “invisible ship at risk” anxiety. |
| U7 | **Async always on** | Standing orders + headless deterministic sim are always legal. Undocked / in another system = space primacy + async colony, never a frozen colony. |
| U8 | **Temporary / scar-heavy bases** | Colonies are extraction footholds, not permanent fortresses. High destruction spectacle is intentional and justified. Layout still matters for the duration of a claim. |
| U9 | **Resource bridge** | Contested planetary extraction produces **unique / high-value** inputs that feed space industry, modules, T2, etc. High-sec planet output is instructional, not a wage. |
| U10 | **Soft influence primary** | Ground play is Protocols, Models, training, Zones, standing orders → **probabilistic** outcomes. No primary micromanagement. |
| U11 | **Hybrid stack, no engine merge** | Colyseus/TS space, Voxelize/Rust ground, Nakama (or equivalent) glue. Shared contracts first; folder merge later if ever. |
| U12 | **This repo is universe authority** | Universe-level rules live here. Combat, Protocol math, voxel destruction, market matching stay in the game repos. |

## U1 — One Residual `[LOCKED]`

No dual protagonist. Spacesim “pilot” language in UI may remain as diegetic slang (the Residual *operates* a hull). Design docs and meta identity use **Residual**. Ground UI may say **Director** as the role title.

## U2 — One active colony `[LOCKED]`

Enforced in shared meta (Nakama or equivalent), not merely by honor.

- Relocate: Evacuate (or abandon) the current claim, then Claim elsewhere. Cooldown / cost `[OPEN]` — see [07-open-questions.md](07-open-questions.md).
- Abandoned scarred plots are not a second live colony. They may linger as wreckage / reclaim `[LEANING]`.
- Alts, corps, and shared clan plots are **not** this rule. Personal Residual law is one claim. Corp/clan territory is a later layer (`[GAME]` / `[OPEN]`).

Rationale: attention, security model, and “go deeper for better loot” all collapse if a Residual can park a safe high-sec city *and* a low-sec extractor at once.

## U3 — Ship stays in space `[LOCKED]`

Matches Spacesim planetary design (bloom windows keep you in the ship) and ASIWars vision (no body, drones + telemetry). Drop-ops as short pinned space-side panels remain a Spacesim `[GAME]` option; they are not colony Directing.

## U4 — High-sec / starter planets `[LOCKED]`

| Axis | Law |
| --- | --- |
| Claim | Docked at a high-sec **NPC station** (starter system or equivalent). |
| Yields | Limited. Trash-grade / instructional. Cannot feed T2 at scale. Mirrors high-sec belt/bloom law. |
| Blanks | Low / starter quality. Training still works; Primes are not a high-sec wage. |
| PvP (ground) | Light or optional, for fun. Not the content. |
| Protection | Long timers. New-player / inactivity windows apply. |
| Focus | Full Director UI while docked at the high-sec station. Ship is **safe**. |
| Permanence | A Residual **may** keep this colony forever. That is a valid playstyle, not a trap. |

High-sec is where you learn Protocols, Models, scarring, and the set-and-watch loop with real security.

## U5 — Low-sec / richer planets `[LOCKED]`

| Axis | Law |
| --- | --- |
| Claim / secure hold | Requires a **linked orbital outpost** in system (built or captured). |
| Yields | Better. Unique / high-value inputs live here. Better wild Blank quality. |
| Contests | Full contested mining, destructive raids, soft-influence competition. |
| Focus | Full Director UI only while docked at the **linked** outpost. |
| Risk | Space risk on the outpost and undock; ground risk on the colony and sites. Player-chosen. |

Outposts are the **gate and the security blanket**, not an arbitrary tax. They industrialize and protect loot (uplift, processing, claim reinforcement, evacuation berths). Pure mobile/extraction-camp play without a mature outpost is `[LEANING]` viable only as high-risk async — not as full-focus Directing.

Null-sec planets `[OPEN]`: treat as a harsher low-sec rung until specified. Do not invent a third claim law without writing it here.

## U6 — Docked-for-full-focus `[LOCKED]`

**Full colony Director interaction** = editing Protocols/Zones/Models, committing contests/raids, watching live with full tools, layout/build, training programs.

Allowed **only if**:

1. Ship is docked, **and**
2. The dock is a **legal berth for that claim** (high-sec NPC station for a high-sec claim; linked outpost for a low-sec claim), **and**
3. Focus is on.

Undocked Residual: space primacy. Colony continues under standing orders / Defense Orders / protection timers. Soft async commands remain legal (U7). Full Director is not.

This is not a punishment. It is how the universe stays honest: you cannot hide an undocked hull behind a wellness dashboard.

If the **outpost itself** is attacked while you are focused: high-priority alerts in the ground UI. Instant **Return to Ship**, then undock or **Evacuate**. Details: [04-claim-and-focus.md](04-claim-and-focus.md).

## U7 — Async / set-and-forget `[LOCKED]`

ASIWars already requires watched, simulated, and mid-join views of an instance to agree (`[GAME]` determinism pillar). Universe law: that capability is **always** the away-mode.

From space, from another system, even from a high-sec dock while *not* focused: monitor, issue standing orders / one-shot Protocols if the command surface allows, let contests resolve headlessly, revisit later.

Async is not a weaker copy of focus. It is the same sim with a thinner command set and no dual-attention tax.

## U8 — Temporary / scar-heavy bases `[LOCKED]`

ASIWars wanted spectacular voxel destruction and struggled to justify heavy fortress-building. The universe answer: **you are not founding a capital**. You extract, scar the landscape, fortify only while the orbit is yours, then repair or move.

- Base layout, materials, Defense Orders remain a skill axis **for the duration of the claim**.
- Expect high scarring, frequent relocation or abandonment when chasing better yields.
- Recoverable destruction still holds at the *structure* level (rebuild, fill craters, reclaim). The *claim* is what is temporary.
- Permanent loss remains Vessels (and Models on capture). That scarcity is `[GAME]` ASIWars and is not relaxed here.

High-sec starter bases may last a Residual’s entire career. They are still not fortresses; they are just rarely worth knocking over.

## U9 — Resource bridge `[LOCKED]`

Direction, not recipes:

- Belts and space blooms do not print the unique planetary goods.
- Ground contests (and limited high-sec colony output) produce those goods.
- Space industry (manufacture, invention, T2, outpost extra-legal jobs) **consumes** them.
- Stations/outposts are industrializers and protectors of uplift, not the primary miners of planet-unique mats.

Exact ids, conversion rates, and whether bloom windows remain a dual source: [05-resource-bridge.md](05-resource-bridge.md) and `[OPEN]` items in [07](07-open-questions.md).

High-sec planet output **must not** be a USDC/export wage. Same north star as Spacesim high-sec trash economics.

## U10 — Soft influence primary `[LOCKED]`

Ground verbs: Zone, Protocol, Prioritize (standing orders), train, load Models. The world resolves intent probabilistically. Odds should stay legible (`[GAME]` ASIWars).

Costly temporary takeover, if it exists, stays a rare opportunistic tool in ASIWars — not the Residual Universe’s primary ground fantasy.

## U11 — Hybrid stack `[LOCKED]`

Do not burn velocity on an engine rewrite to “start” the universe. Shared vision + Nakama contracts are the merge.

Later re-evaluation (port ground to TS, absorb space into Rust, true monorepo) is allowed **after** both MVPs and a real handoff exist. It is not a current action.

## U12 — Authority `[LOCKED]`

See the README authority split. When documenting a new space or ground feature that touches claims, focus, or the bridge, **cite this repo**. Do not restate a weakened copy of U1–U11 in a game spec.

## Derived consequences (not extra locks)

Useful corollaries so implementers do not “discover” contradictions:

- A Residual in a roam with an active low-sec claim has a colony running without them. Defense Orders and protection timers are the security, not hope.
- Full-focus is a **mode switch**, not a split HUD. Ground is primary; space is a minimized local-intel panel at most.
- Outpost investment is how you convert “I want better loot” into “I am allowed to sit still and Direct.”
- Destruction spectacle on the ground does not require the Spacesim combat sim. Different engines, same Residual.
