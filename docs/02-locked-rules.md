# 02 — Locked Universe Rules

These are **universe law**. Both games honor them. Implementation knobs (timer lengths, yield tables, outpost recycle minutes) live in the game docs and may change without unlocking the rule.

Changing a `[LOCKED]` row is a pillar change. Record it here, then patch both games’ design notes.

## The table

| # | Rule | Statement |
| --- | --- | --- |
| U1 | **One Residual** | The player is a bodiless leftover superintelligence fragment. Space presence is ships/outposts. Ground presence is soft influence over Vessels. |
| U2 | **One active colony** | Maximum **one** active planetary colony claim per Residual. Relocate by evacuating, then claiming. Never two live claims. |
| U3 | **Ship stays in space** | The hull never becomes a walkable planetary body. Inhabit = focus attention onto a colony instance. |
| U4 | **High-sec / starter planets** | Safe, **limited** Trace quality and Blank quality, **long** protection timers, **light / optional** ground PvP. Claim and full interaction while **docked at a high-sec NPC station**. A **permanent limited colony sim** is allowed. |
| U5 | **Low-sec / richer planets** | Better mouths: they **train faster** (Traces accrue faster) and **listen better**. Full contested mining + destructive soft-influence contests. Claim or **secure** interaction requires a **linked orbital outpost** (build or take over). |
| U6 | **Docked-for-full-focus** | Full colony **Director** interaction only when the ship is **safely docked** (high-sec station for starter claims, or the **linked** low-sec outpost). This is the security model that eliminates “invisible ship at risk” anxiety. |
| U7 | **Async always on** | Standing orders + headless deterministic sim are always legal. Undocked / in another system = space primacy + async colony, never a frozen colony. |
| U8 | **Temporary / scar-heavy bases** | Colonies are extraction footholds, not permanent fortresses. High destruction spectacle is intentional and justified. Layout still matters for the duration of a claim. |
| U9 | **Resource bridge** | The unique planetary good is a **Sync Trace** written while a Model runs in a NeuralSync chip. Space manufactures **LoRAs** from traces. High-sec traces are instructional, not a wage. Unique mats are not the north star. See [05-resource-bridge.md](05-resource-bridge.md). |
| U10 | **Soft influence primary** | Ground play is Protocols, Models, training, Zones, standing orders → **probabilistic** outcomes. No primary micromanagement. |
| U11 | **Hybrid stack, no engine merge** | Colyseus/TS space, Voxelize/Rust ground, Nakama (or equivalent) glue. Shared contracts first; folder merge later if ever. |
| U12 | **This repo is universe authority** | Universe-level rules live here. Combat, Protocol math, voxel destruction, market matching stay in the game repos. |
| U13 | **Licensed founding kit** | A high-sec Claim issues a station-licensed starter roster of baseline **NeuralSynced Users**. The first Vessel is **not** a Residual clone. Low-sec growth is volunteer native onboarding plus rival-User raids. See [08-origin-and-founding.md](08-origin-and-founding.md). |
| U14 | **Volunteer NeuralSync** | Unenrolled natives enroll via **Clinic / Closedex** only. Refusal is legal — they stay un-Protocolable. No hostile chipping. Capture of already-chipped Users remains raid (`Stolen`). |
| U15 | **Closed / Open Models** | High-sec factory Models are **Closed**: region-locked, not Evacuateable, not Model-Hub originals. **Distill** of a Closed teacher writes a new **Open** original (lossy). Only Open Models load outside high-sec. See [08-origin-and-founding.md](08-origin-and-founding.md). |
| U16 | **Field contact / Contact intel** | Away from the foothold, Vessels execute their **Open Models**. **Hold** (contest a node) is anonymous. **Hunt** (chase / capture / execute people) writes a **replay** and a **Contact**. Flee is not teleport — **caught-while-fleeing is a Hunt**. Targeted foothold raids **require** a Contact. |
| U17 | **Kernel / LoRAs / Sync Traces** | Hull death ejects a **Kernel**. Fitted **LoRAs** ride the Kernel, not the wreck. **Sync Traces** are the unique ground good; space manufactures LoRAs. Kernel destruction loots or burns LoRAs. Skills stay. High-sec Kernels are auto-safe (Proctor). Not a clone (U13), not a Vessel (U1). See [05-resource-bridge.md](05-resource-bridge.md). |

## U1 — One Residual `[LOCKED]`

No dual protagonist. Spacesim “pilot” language in UI may remain as diegetic slang (the Residual *operates* a hull). Design docs and meta identity use **Residual**. Ground UI may say **Director** as the role title.

## U2 — One active colony `[LOCKED]`

Enforced in shared meta (Nakama or equivalent), not merely by honor.

- Relocate: Evacuate (or abandon) the current claim, then Claim elsewhere. Cooldown / cost `[OPEN]` — see [07-open-questions.md](07-open-questions.md).
- Abandoned scarred plots are not a second live colony. They may linger as wreckage / reclaim `[LEANING]`.
- Alts and **Hives** are **not** extra colony slots. Personal Residual law is one claim. **Hive** (Spacesim `[GAME]` player org; H1–H2 shipped) may share space hangars, one Hive wallet, offices, and later a linked outpost as a Focus **berth** — the colony stays personal (`[LEANING]` [O12](07-open-questions.md)). Hive-held extra claims would be a later lock in **this** repo, not a silent Spacesim fork.

Rationale: attention, security model, and “go deeper for better loot” all collapse if a Residual can park a safe high-sec city *and* a low-sec extractor at once.

## U3 — Ship stays in space `[LOCKED]`

Matches Spacesim planetary design (bloom windows keep you in the ship) and ASIWars vision (no body, drones + telemetry). Drop-ops as short pinned space-side panels remain a Spacesim `[GAME]` option; they are not colony Directing.

## U4 — High-sec / starter planets `[LOCKED]`

| Axis | Law |
| --- | --- |
| Claim | Docked at a high-sec **NPC station** (starter system or equivalent). |
| Yields | Limited. Instructional traces. Not a wage. Mirrors high-sec belt/bloom law. |
| Blanks | Low / starter quality. Training still works, slower, weaker listen. Primes and wage traces are not a high-sec drop. |
| PvP (ground) | Light or optional, for fun. Not the content. |
| Protection | Long timers. New-player / inactivity windows apply. |
| Focus | Full Director UI while docked at the high-sec station. Ship is **safe**. |
| Permanence | A Residual **may** keep this colony forever. That is a valid playstyle, not a trap. |

High-sec is where you learn Protocols, Models, Trace harvest, scarring, and the set-and-watch loop with real security.

## U5 — Low-sec / richer planets `[LOCKED]`

| Axis | Law |
| --- | --- |
| Claim / secure hold | Requires a **linked orbital outpost** in system (built or captured). |
| Yields | Real **Sync Traces**. Mouths **train faster** and **listen better**. Better wild Blank quality. |
| Contests | Full contested mining, destructive raids, soft-influence competition. Hunt for rival Opens. |
| Focus | Full Director UI only while docked at the **linked** outpost. |
| Risk | Space risk on the outpost and undock; ground risk on the colony and sites. Player-chosen. |

Outposts are the **gate and the security blanket**, not an arbitrary tax. They industrialize and protect Trace uplink, LoRA manufacture, claim reinforcement, and evacuation berths. Pure mobile/extraction-camp play without a mature outpost is `[LEANING]` viable only as high-risk async — not as full-focus Directing.

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

- Belts and space blooms do not print **Sync Traces** or **LoRAs**.
- Ground: a Model running in a NeuralSync chip writes **Sync Traces**. Lower-sec trains faster and listens better (U5/U17). Activity-typed traces (fight vs farm) are `[LEANING]`.
- Space **consumes** traces as LoRA manufacture inputs. LoRAs fit the Residual (Kernel slots), not hull highs/mids/lows.
- Stations/outposts industrialize and protect uplink and manufacture; they do not train the humans.

Exact bills, slot counts, and Kernel-kill loot: `[GAME]` Spacesim (K2/K3 shipped). See [05-resource-bridge.md](05-resource-bridge.md).

High-sec traces **must not** be a USDC/export wage. Same north star as Spacesim high-sec trash economics.

`[LOCKED]` Unique planetary mats are not this pipe’s north star. Parked.
`[LOCKED]` Models are not a turret stat. They never gun a hull. LoRAs are Residual overlays, capped. Vessels are not crew.

## U10 — Soft influence primary `[LOCKED]`

Ground verbs: Zone, Protocol, Prioritize (standing orders), train, load Models. The world resolves intent probabilistically. Odds should stay legible (`[GAME]` ASIWars).

Costly temporary takeover, if it exists, stays a rare opportunistic tool in ASIWars — not the Residual Universe’s primary ground fantasy.

## U11 — Hybrid stack `[LOCKED]`

Do not burn velocity on an engine rewrite to “start” the universe. Shared vision + Nakama contracts are the merge.

Later re-evaluation (port ground to TS, absorb space into Rust, true monorepo) is allowed **after** both MVPs and a real handoff exist. It is not a current action.

## U12 — Authority `[LOCKED]`

See the README authority split. When documenting a new space or ground feature that touches claims, focus, origin, or the bridge, **cite this repo**. Do not restate a weakened copy of U1–U17 in a game spec.

## U13 — Licensed founding kit `[LOCKED]`

High-sec Claim + Focus does **not** spawn a Residual clone, a native village, or an empty plot the player must populate from space.

Station HR assigns a **Closedex** seat and **Licensed Users**: baseline Blanks, already chipped, seated on **Closed** ClosedAI factory Models (U15). ASIWars `session.found` is that kit (`[GAME]` roster: Labor + Guard). Universe law: licensed, baseline, already NeuralSynced, not you.

Low-sec does **not** re-issue that kit as the growth loop. After Evacuate + Claim under a linked outpost, new mouths come from **Clinic** (U14) and from **raiding rival Users**. You may bring evacuated Licensed Users with you as **bodies** (pedigree on relocate is `[OPEN]` — [07 O17](07-open-questions.md)). Their Closed seats **do not** come (U15). Pack an **Open** Model or arrive with empty chips.

Rationale: the teaching plot must exist before compact outposts. “Outpost first” is the rich-claim gate (U5), not the origin. Details: [08-origin-and-founding.md](08-origin-and-founding.md).

## U14 — Volunteer NeuralSync `[LOCKED]`

Two enrollment paths, never a third “force the chip”:

| Path | Who | Result |
| --- | --- | --- |
| Station license (U13) | High-sec starter roster | Already chipped Licensed Users |
| Clinic / Onboard | Unenrolled natives on a claimed low-sec planet | Volunteer NeuralSync → `WildBorn`, now Protocolable |
| Raid / Steal | Another Residual’s Users | Already chipped → `Stolen` |

Refusal at the clinic is legal. Unenrolled NPCs stay in the world and cannot take Protocols. Hostility is Residual-vs-Residual, not Residual-vs-skull.

Store-approval and D2 Strict ride this rule: clinic is wellness; raids steal Users who already consented to a chip. Do not depict coercive implantation.

Clinic density and odds are `[GAME]` / `[OPEN]` ([07 O16](07-open-questions.md)). This rule only forbids hostile NeuralSync and names the verb.

## U15 — Closed / Open Models `[LOCKED]`

High-sec is where you meet **proprietary ClosedAI weights** and graduate to **weights you own**.

| Class | Where it runs | Evacuate | Model Hub | How you get it |
| --- | --- | --- | --- | --- |
| **Closed** | High-sec licensed claim only | No. Unseats and stays with the park license. | Not as the Closed original | Station kit (`wellstream-labor-v0` / `wellstream-guard-v0` — `[GAME]` ids; copy says ClosedAI) |
| **Open** | Any claim (high-sec or low-sec) | Yes | Yes (unique original / further Distills) | **Distill** a Closed teacher, or later Distill/train/buy Open |

Diegetic: ClosedAI ToS. The factory file is geo-licensed to the stewardship park. You may train the Closed seat in the garden. You may not take the file.

**Distill is the high-sec game.** It writes a **new unique Open original** (lossy — ASIWars D19). The Closed teacher remains. The Open is worse than the teacher on purpose. You load it, train it in the garden. A harvestable, activity-typed Open **is** a LoRA (U17).

`[LOCKED]` Closed originals are not stealable portable assets. A raid may take the User; the Closed seat unloads/bricks. The prize is wetware and any **Open** already distilled.

`[LOCKED]` High-sec Distill must not be a Model-Hub wage. Same north star as U4/U9. Caps, cost, and how many Distills per teacher are `[OPEN]` ([07 O19](07-open-questions.md)). Instructional Closed skill ceilings still apply.

Low-sec cannot load Closed. Clinic natives with empty chips wait for an Open you packed, bought, or stole.

Rationale: high-sec needs a graduation item that is not a wage LoRA (those pay in low-sec). Portable Open weights are that item. Closed DRM is the ClosedAI / geo-license joke. Details: [08-origin-and-founding.md](08-origin-and-founding.md).

## U16 — Field contact / Contact intel `[LOCKED]`

Low-sec growth is **send 1–2 Open-seated Users out, hunt volunteers, maybe meet someone**. You do not command the scrap from the hull.

| Beat | Law |
| --- | --- |
| Where | Shared instances away from the personal foothold: resource sites, clinic basins. Instance-everything (ASIWars). Not an open-world stroll. |
| Who decides | The loaded **Open Model** (priors, nerve, duty, cowardice) plus standing Protocols. No live “attack” from space. Focused one-shot Protocol (U6 / D9) is sitting still, not roaming. |
| **Hold** | Contest a **node** (site pool, clinic basin). Blood over rocks/volunteers. Anonymous. Replay optional for the Residual who watched; **no Contact**. You fight for the reason you came. |
| **Hunt** | Chase, capture, or execute **people**. Writes a deterministic **replay** and a **Contact** on each Residual whose Vessel was hunted. That is how you learn a name you can raid. |
| **Flee** | Cede the node. Not teleport. Haul, injuries, and Labor Opens are slower. A combat Open may **catch**. **Caught-while-fleeing is a Hunt** (Contact). |
| Targeted foothold raid | **Requires** a Contact. Nameless **Hold** scraps stay legal. You cannot wardec a ghost. |
| Space local | Planet may show as claimed. **Who** stays dark until a Hunt Contact. Revises former O10 lean. |
| High-sec | Teaching garden. Field Contacts do **not** unlock low-sec raids. |

Diegetic: Closedex logs **hunts**, not every bump over ore. Vessels know that chasing a person puts their Director on the tape. Some Open forks are trained to hold the node and leave. Some are trained to run people down — and that puts a target on their Director.

**Drives not to flee** (why combat still happens for space-export Residuals):

1. **The node pays.** Clinic volunteers, haul, and the mouths still training LoRAs stay with whoever **Holds**. Fleeing cedes the reason you came.
2. **Catch.** Flee is a roll against the hunter’s Open (speed, nerve, load). Fail = Hunt = you get named anyway, and you already dropped the node.
3. **People.** Higher-trait captures and rival Opens only come from Hunt. Always-flee never upgrades the roster in the field.
4. **Skills on the Open.** Fighting grows by fighting (ASIWars D17). Always-flee forks stay soft and get farmed.
5. **Always-flee gets jumped.** Predators learn. You become haul.

Catch math (speed, haul penalty, nerve) is `[OPEN]` ([07 O20](07-open-questions.md)). Universe law only: flee is catchable, catch is Hunt.

First low-sec drop is **small** `[LEANING]`: Evacuate packs **1–2** Vessels + Open Models. Clinic is how the foothold grows. Not a forever roster cap (D6/D31 still apply later). Pack-out numbers remain [07 O15](07-open-questions.md).

Rationale: exploration, volunteer hunt, and Model personality become the targeting game. A public “who owns this planet” list would skip the 1–2 unit story. Details: [08-origin-and-founding.md](08-origin-and-founding.md).

## U17 — Kernel / LoRAs / Sync Traces `[LOCKED]`

The Residual has no body. The hull is an extended body (U1). Ground-farmed power needs a risk layer that is not hull loot and not skill-rank loss.

The point of the ground game is **NeuralSynced humans training chips**. While a Model runs, it writes **Sync Traces** — the unique planetary good. Space manufactures **LoRAs** from those traces and dock-fits them onto the Residual. On hull structure 0 the Residual ejects a **Kernel**. LoRAs ride the Kernel, not the wreck.

| Beat | Law |
| --- | --- |
| Chip | **NeuralSync**. Holds the loadable Model. Humans volunteer (U14) or arrive Licensed (U13). |
| Train | The human trains the seated Model by doing. Lower-sec mouths train **faster** and **listen better** (U5). Activity-typed traces (fight vs farm vs craft) `[LEANING]`. |
| Unique good | **Sync Trace** — inference / duty log of a Model-in-chip run. High-sec instructional. Not datacores, not bloom PI, not a Model. ASIWars emits. |
| Weights | **Open** Distills remain portable files (U15). They are **not** the unique export. Closed never Evacuate. |
| Manufacture | Legal berth. Traces + bits → LoRA (`[GAME]` Spacesim K3). No NPC LoRA mall. High-sec rejects the bill. |
| Wear | LoRAs dock-fit **Kernel slots**, not hull highs/mids/lows. Capped overlays (~10% one axis). Same hull, better Residual. Skills stay on the ledger. |
| Hull death | Wreck loot = hull modules / cargo / drones. Residual **is** the Kernel. LoRAs do **not** appear on the wreck. |
| Kernel | Huntable in low/null. Auto-safe in high-sec (**Proctor** garden). Warp + dock **Rehost**: LoRAs kept. Kernel destroyed: LoRAs loot or burn. Skills intact. |
| Not this rule | Ground Hunt/raid of rival Opens is **capture** (U14/U16). Kernel-kill is the **sink**. Do not collapse them. |
| Not | A Residual clone (U13). A Vessel. A pod/capsule (HUD “flight pod” is chrome). An implant on a human. |

`[LOCKED]` Models never gun a hull. LoRAs are Residual overlays. Vessels are not crew. Closed files never ride the Kernel.

`[LOCKED]` High-sec traces and LoRAs are not a wage.

Slot count, loot roll, T1 bills: `[GAME]` Spacesim (K2/K3: 3 slots, wreck-like drop/burn, `sync-trace`). Activity-typed traces: `[OPEN]` ([07 O21](07-open-questions.md)).

Rationale: traces are the harvest; LoRAs are the wear; Kernel death is the sink. Unique mats do not need to exist for this pipe. Details: [05-resource-bridge.md](05-resource-bridge.md). Combat/nav: Spacesim [`2026-09-02-residual-kernel-adapters`](https://github.com/revenant-13/spacesim/blob/main/docs/superpowers/specs/2026-09-02-residual-kernel-adapters.md).

## Derived consequences (not extra locks)

Useful corollaries so implementers do not “discover” contradictions:

- A Residual in a roam with an active low-sec claim has a colony running without them. Defense Orders and protection timers are the security, not hope.
- Full-focus is a **mode switch**, not a split HUD. Ground is primary; space is a minimized local-intel panel at most.
- Outpost investment is how you convert “I want better loot” into “I am allowed to sit still and Direct.”
- Destruction spectacle on the ground does not require the Spacesim combat sim. Different engines, same Residual.
- The first two mouths on a high-sec plot are **assigned Users**, not natives you found and not a fork of the Residual (U13).
- “Capture natives” means **Clinic** if they are unenrolled, **raid** if they already belong to another Residual (U14). Not a single hunt verb.
- Evacuate from high-sec packs **people and Open Models**, never Closed factory files (U15). Arriving in low-sec on Labor v0 is illegal; Distill first or buy/steal Open.
- You do not find raid targets on the overview. You find them when someone’s Open Model **Hunted** (U16). Holding a mine does not name you. Getting caught fleeing does.
- You come to the planet to write **Sync Traces**, not to print T2 mats (U9/U17). Low-sec is where the humans are worth Directing.
- Fits sink on the hull wreck. LoRAs sink on **Kernel** death. Skills never sink that way.
- Joining a **Hive** does not add a colony slot (U2). Hive ticker on overview is not a **Contact** (U16). Declared Hive **War** lists Hive names, not plot owners, and does not hunt garden Kernels (U17).
