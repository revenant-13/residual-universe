# 03 — Terminology Map

Mechanical terms stay **precise and stable**. Diegetic flavor can be funnier and may vary by surface (space overview vs Closedex). Universe-level nouns below are `[LOCKED]` unless marked otherwise.

Shipped title: **NeuralSync**. Player: **Residual**. Chip: NeuralSync. NPC corp: **ClosedAI**. Director console: **Closedex**. Player org: **Hive** `[LEANING]`. Unique good: **Sync Trace**. Residual overlay: **LoRA**. Eject entity: **Kernel**.

Naming principle (from ASIWars, now universe-wide): every mechanic noun should carry **both** an ML meaning and a care/corporate meaning where possible. Space keeps EVE-like operational language; do not rename “warp” to “inference hop.”

## Product and identity

| Term | Meaning | Spacesim today | ASIWars today |
| --- | --- | --- | --- |
| **NeuralSync** `[LOCKED]` | **Shipped title** and the **consumer chip**. Neuralink gag on the box; wetware in-world. Holds the loadable Model. | Kernel wears LoRAs; humans wear NeuralSync | Chip / Model seat |
| **Residual** `[LOCKED]` | The player. Leftover superintelligence fragment. No body. | Implicit “pilot” / character | Residual / identity |
| **Director** `[LOCKED]` | Role title while focused on a colony. Same being. | n/a | Closedex dashboard |
| **ClosedAI** `[LOCKED]` | The corp. Issues Closed factory files. Geo-license / ToS joke (OpenAI parody). | n/a | Issuer of Closed seats |
| **Closedex** `[LOCKED]` | Director **console**. Clinic, licensed kit, Distill, uplink (Codex parody, product of ClosedAI). Replaces retired WellStream™. | n/a | Director chrome / Neighbor |
| **Kernel** `[LOCKED]` (U17) | Residual’s ejected space runtime after hull death. Huntable in low/null; auto-safe in high-sec (Proctor). | Overview kind `kernel`. K1 shipped | n/a |
| **LoRA** `[LOCKED]` (U17) | Low-Rank Adaptation overlay fitted to the Residual (Kernel), not the hull. Manufactured from Sync Traces. At risk on Kernel death. | `kind: "lora"` Kernel slots (3). Not high/mid/low | Not a Model. Not a Protocol adapter |
| **Sync Trace** `[LOCKED]` (U9/U17) | Inference / duty log written while a Model runs in a NeuralSync chip. Unique planetary good. High-sec instructional. | Commodity `sync-trace`; T1 LoRA bills consume it | ASIWars emits (QA grant until cited) |
| **Rehost** `[LOCKED]` (U17) | Survive Kernel warp-home or Kernel death: Residual at a berth with skills intact. | Replaces “Dock / clone” copy | Not a Residual clone (U13) |
| **Proctor** `[LOCKED]` (U17) | High-sec overlord. Eval supervisor of student runtimes. Not CONCORD. | Today: `pvpEnabled === false` | Residuals earn LoRAs from ground traces, not Kernel hunting in the garden |
| **Fork** `[GAME]` | Optional prestige copy of a Residual (ASIWars, post-MVP). Not the founding roster (U13). | n/a | Prestige layer |

Do not introduce a second player noun (“Captain,” “Operator”) in design docs. UI slang on the space side (“pilot,” “capsuleer-class hull”) is flavor.

## Ground: people and weights

| Term | Meaning |
| --- | --- |
| **Vessel** `[LOCKED]` | A human unit. Mechanical term. UI may say Users / Residents. |
| **Licensed User** `[LOCKED]` (U13) | Station-issued starter Vessel. Baseline Blank, already NeuralSynced, seated on a **Closed** factory Model (U15). Not a Residual clone. High-sec founding kit. Body may Evacuate; Closed seat may not. |
| **Unenrolled** `[LOCKED]` (U14) | Native without a chip. Lives on low-sec planets. Not Protocolable until Clinic. |
| **Blank** `[LOCKED]` | Low-tier human (licensed starter or wild). Flavor: Base Model. |
| **Tuned / Fine-tune** `[LOCKED]` | Trained-up Blank. Fine-tune = you trained it (pedigree). |
| **Prime** `[LOCKED]` | High-trait Vessel. Mostly stolen or slowly trained. |
| **Model** `[LOCKED]` | Loadable **weights** artifact: decision tree + weight allocation + trained skills. Separable from the human. Traded on the Model Hub. |
| **Closed Model** `[LOCKED]` (U15) | Proprietary **ClosedAI** original. High-sec park license only. Cannot Evacuate, cannot Hub as itself. Factory seats: `wellstream-labor-v0` / `wellstream-guard-v0` (`[GAME]` ids). |
| **Open Model** `[LOCKED]` (U15) | Player-owned original (or further Distill). Loads anywhere. The high-sec graduation item. Hub cargo. **Not** a LoRA and **not** the unique export (traces are). |
| **Distill** `[LOCKED]` (U15 / ASIWars D19) | Lossy copy. Distill of **Closed** writes a **new Open original** you own. Closed teacher stays. Distill of Open stays Open and worse. |
| **Protocol** `[LOCKED]` | Live nudge: push–pull on priors. Crafted, equippable. Model *allocates*; Protocol *steers*. |
| **Zone** `[LOCKED]` | Spatial priority (Collection, Attention, Defense, Attractor, Repulsor…). Vessels gravitate; they are not ordered to a tile. |
| **Inference** `[LEANING]` | One resolved nudge attempt (success/fail roll). |
| **Drift** `[LEANING]` | Reversion toward base priors. Fought with colony condition and repeated Protocols. |
| **Obedience** `[LOCKED]` (ASIWars D30) | How reliably a Vessel follows intent vs its own Drives. |
| **VRAM** `[LOCKED]` (ASIWars D17/D31) | Per-Vessel complexity budget and colony hosting pool (compute hardware). |
| **Checkpoint** `[LOCKED]` (ASIWars D21) | Pre-emptive Model backup. Insures weights, not the body. |

| **Offboarding** | Death/removal euphemism. |
| **Reassignment / placement / rehoming** | Market transfer euphemism for already-chipped Users. Never “sale of people” in UI. Not the Clinic verb. |
| **Clinic / Onboard** `[LOCKED]` (U14) | Enroll an Unenrolled native onto NeuralSync. Volunteer only. Refusal legal. Closedex verb. |
| **Contact** `[LOCKED]` (U16) | Intel that names another Residual. Written on a **Hunt** (chase / capture / execute, or catch-while-fleeing). Required to targeted-raid their foothold. **Hold** (node contest) writes none. |
| **Hold** `[LOCKED]` (U16) | Contest a node (site pool, clinic basin). Anonymous scrap. You came for the goods. |
| **Hunt** `[LOCKED]` (U16) | Pursue people, not the node. Writes Contact + replay. |
| **Flee** `[LOCKED]` (U16) | Cede the node. Catchable. Caught = Hunt. |

Provenance tags stay ASIWars `[GAME]`: `WildBorn` (clinic or wild pedigree) / `Trained` / `Stolen` (hot goods). Licensed high-sec starters are not `Stolen`; whether they keep a distinct license tag after Evacuate is `[OPEN]` ([07 O17](07-open-questions.md)).

Capture vs kill (weights rule) stays ASIWars `[GAME]`: killed → salvage Model at a loss; captured → Model lost to the enemy. Universe copy may use it; do not re-tune it here.

## Ground: colony verbs

| Verb | Meaning |
| --- | --- |
| **Claim** | Attach this Residual’s **one** colony slot to a planet (or designated plot on it). High-sec: from a high-sec station dock. Low-sec: requires linked outpost. |
| **Inhabit** | Fantasy synonym for holding a claim. Not a second mechanic. |
| **Focus** | Enter full Director interaction. Requires docked-for-full-focus (U6). |
| **Return (to Ship)** | Leave Focus. Client back to space. Hull still docked until you undock. |
| **Evacuate** | Pack Vessels, **Open** Models, resources into hangar. **Closed** Models unseat and stay (U15). |
| **Distill** | Bake a lossy Open original from a Closed teacher (high-sec game) or from an Open (later). Ground-owned. Not the unique export. |
| **Uplink** | Move Sync Traces (and optionally Open files) from plot to hangar (Closedex / Core). Not Evacuate. Closed never uplinks. |
| **Relocate** | Evacuate (or abandon) + Claim elsewhere. One-claim rule still holds. |
| **Onboard** | Clinic enrollment of an Unenrolled native (U14). Ground-owned sim; universe names the verb. Not market reassignment. |

## Space: keep the native words

Do not Residual-wash navigation or combat.

| Term | Meaning | Residual mapping |
| --- | --- | --- |
| **bits** | Spacesim soft currency. Shift leftover unit of account. | Soft layer. May sit beside ASIWars **Credits / Compute Credits**. Bridged, not necessarily renamed. `[OPEN]` whether one ticker wins. |
| **USDC / export** | Player-to-player cash-out. Docked, delayed, skill-gated. Game never the buyer. | Hard layer. LoRAs that reach space hangars follow **space** export law. The game is never the buyer. |
| **Kernel** | See Product and identity. Pod analog. Do not name the entity a pod. | HUD “flight pod” stays chrome. |
| **LoRA** | See Product and identity. Residual overlay. | Not a hull module. Not a Protocol. |
| **Sync Trace** | See Product and identity. Unique-class LoRA input. | Not datacores, not bloom PI. |
| **high-sec / low-sec / null** | Security geography. High-sec is **Proctor**-safe (`pvpEnabled === false`). | Same map for planetary claim law (U4/U5). Never call Proctor CONCORD. |
| **station** | NPC dock. Safe berth. Markets, industry, insurance. | High-sec **legal berth** for starter colony Focus. |
| **outpost** | Player structure (compact-outpost design). Build / recycle / flag / well. | **Linked orbital outpost** = low-sec claim gate and Focus berth. |
| **flag / well / residue / slag** | Outpost claim stake, siphon source, siphon goods, scrap goods. | Residue/slag remain space-side products. They are not LoRAs (U9). |
| **planetary pad / bloom window** | v1 space-side PI: stay in ship, extract at a pin, haul. Nobody lands. | Lighter space-side PI. Dual source vs phased-down is `[OPEN]`. Not colony Focus. |
| **PI** | Planetary industry ids (e.g. biomass, refractory, sludge). | Space-side extractables. Not traces. Not LoRAs. |
| **T1 / T2 / invention** | Industry ladder. High-sec cannot close T2. | LoRAs are **not** T2 mats. Traces feed LoRA bills. T2 PI bills stay space-side. |
| **hull / module / drone** | Fitted space assets at risk when undocked. | Residual’s space body. |
| **grid / system / gate** | Combat space, solar system, travel. | Unchanged. |

## Space: player org `[LEANING]`

Copied from Spacesim [`2026-09-05-hive-org-design.md`](https://github.com/revenant-13/spacesim/blob/main/docs/superpowers/specs/2026-09-05-hive-org-design.md) so both games stop saying “corp.” **Not** a new U-row. U1 (one Residual) and U2 (one colony) are unchanged. H1–H2 shipped `[GAME]`; wars and **Mesh** stay later.

| Term | Meaning | Spacesim today | ASIWars today |
| --- | --- | --- | --- |
| **Hive** `[LEANING]` | Durable player org. Household of Residuals sharing space hangars, one Hive **bits** wallet, offices, later outposts. Not a mind-merge. | H1–H2: Found/Join, ticker `Ada [TICK]`, Hive wallet, office Floor/Rack. Wars later. | n/a. Not a colony. Not extra claims (O12). |
| **Root** `[LEANING]` | Hive leader (exactly one). | Create / disband / war / seize Rack. | Not **Director** (colony Focus title). |
| **Steward** `[LEANING]` | Hive officer. | Recruit, office/outpost, Hive-wallet spend, Rack. | — |
| **Peer** `[LEANING]` | Default Hive member. | Floor take if granted. Personal wallet + hangar remain. | Colony, Kernel, LoRAs stay personal. |
| **Hive wallet** `[GAME]` | One extra **bits** pool on the same ticker. Never replaces the personal wallet. | Deposit/withdraw docked. Not a Polygon identity. | n/a |
| **Office** `[LEANING]` | Rented NPC-station berth that unlocks Hive hangar **at that station**. | Storage / later jobs. H2 shipped. | **Not** a Focus berth. U4 Focus stays the NPC desk. |
| **Floor / Rack** `[GAME]` | Hive hangar partitions at an office. Floor = common; Rack = officers. | Peer Floor query; Floor take is a grant; Rack is Steward/Root. | Not hangarBridge colony cargo. Hulls and LoRAs stay personal. |
| **War** `[GAME]` | Declared Hive-vs-Hive conflict. Public Hive names, not Residual names, not planet owners. | Later. Hull PvP in high-sec (Proctor exception). Garden Kernels stay auto-safe (U17). | Does **not** punch U16. Not a raid-unlock. |
| **Mesh** `[OPEN]` | Alliance analog: a network of Hives. | Out. Discord / later spec. Not Phase 3. | n/a |

Do not Residual-wash war, hangar, wallet, office, or rank. Do not use corporation / CEO / alliance as default copy. **ClosedAI** is the NPC corp; Hive is the player org.

## Crosswalk (quick)

When a Spacesim doc says… write Residual Universe as…

| Spacesim | Residual Universe |
| --- | --- |
| Character / pilot | Residual |
| Dock at station and “do PI” (v1 blooms) | Stay in ship; not Focus |
| Compact outpost | Orbital anchor for a low-sec **claim** |
| High-sec | Starter claim legal; instructional traces; Focus from NPC station; Proctor-safe |
| Low-sec | Richer claim; faster train / better listen; outpost-gated; Focus from linked outpost; huntable Kernel |
| Kernel / LoRA / Sync Trace | **U17** `[LOCKED]`. K1–K3 shipped in Spacesim. |
| Atrium | Starter high-sec system (`[GAME]` Spacesim). Not Heimatar. |
| Hangar | Shared with colony export/import when docked at the legal berth |
| Corp / corporation / alliance | **Hive** (player org). **Mesh** is the later alliance analog (out). **ClosedAI** is the NPC corp. |
| Corp hangar | Hive **Floor / Rack** at an **Office**. Not a Focus berth. |
| bits | Soft space ticker; bridge to Credits `[OPEN]` |
| Residue | Space siphon good; not a synonym for Vessel “residual” |

When an ASIWars doc says… write Residual Universe as…

| ASIWars | Residual Universe |
| --- | --- |
| Personal land claim | The **one** planetary colony claim (U2) |
| Region / relocate | Evacuate + Claim; high-sec vs low-sec law applies |
| Personal base instance | Colony instance, spun/attached on Claim |
| Resource site instance | Contested planetary extraction site (ground) |
| Credits | Soft ground ticker; bridge to bits `[OPEN]` |
| Director dashboard | **Closedex** (Focused colony UI) |
| Harvestable Open | Portable weights (U15). Unique export is **Sync Trace**, not the Open |
| Model-in-chip run / Fine-tune | Writes **Sync Traces** (U9/U17) |
| WellStream™ (retired) | **Closedex** / **ClosedAI** — do not write WellStream in new copy |
| Raid / protection timer | Still `[GAME]`, but high-sec timers are **long** (U4) |

## Collision watch

- **Residual** (the player) vs **residue** (outpost siphon good). Never abbreviate residue to “residual” in space UI.
- **Model** (weights artifact) vs **hull model** / mesh. Space docs say **hull**. Ground docs say **Model**.
- **Claim** (colony) vs **claimCompact** / loot claim in Spacesim rifts. Keep the verb qualified: **Claim planet** vs **claim loot**.
- **Station** (NPC) vs **outpost** (player). Only the latter gates low-sec colonies.
- **Focus** (Director mode) vs camera focus / lock. UI: **Dock & Focus Colony**.
- **Onboard** (Clinic, U14) vs market **reassignment**. Never use “onboarding” for selling Users.
- **NeuralSync** (shipped title **and** consumer chip) vs **Closedex** (Director console) vs **ClosedAI** (corp). Do not treat them as synonyms.
- **ClosedAI** (NPC corp) vs **Hive** (player org). ClosedAI issues Closed files. Residuals join Hives. Never call a Hive “ClosedAI.”
- **ClosedAI** (corp) vs **Closed Model** (geo-licensed file). Closed files are ClosedAI’s. The Residual is not an employee; they hold a Closedex license.
- **Hive** (player org) vs combat drones / “hive mind.” Copy: a household of distinct Residuals. U1 is not relaxed.
- **Director** (colony Focus title) vs EVE corp “Director.” Org rank is **Steward**, never Director.
- **Syndicate** (NPC industry row in Spacesim) vs Hive (player org).
- **Office** (Hive station berth) vs high-sec Focus desk (U4) vs linked outpost (U5). Office is storage, not a second Focus law.
- **War** (Hive vs Hive, space) vs **Hunt** / **Contact** (U16). A war list is not a colony-owner directory.
- **LoRA** (Residual Kernel overlay) vs **Model** (Vessel loadable) vs **Protocol** (live nudge). LoRAs never occupy hull slots. Protocols are not LoRAs.
- **Sync Trace** vs datacore vs bloom PI vs Open Model. Four different inputs.
- **Kernel** (Residual runtime) vs planet/station mesh “core.” Overview says **Kernel**.
- **flight pod** (Spacesim HUD chrome) vs Kernel (entity). Do not name the entity a pod.
- **Proctor** vs CONCORD. Never call it CONCORD. Starter system is **Atrium**, not Heimatar.
- **implant** — human NeuralSync fantasy, not Residual fittings. The analog is LoRA.
- **NeuralSync chip** (human wetware) vs Kernel (Residual runtime). Humans do not wear space LoRAs. The Residual does not wear a NeuralSync chip.
- **WellStream™** is **retired**. Old copy meant Closedex / ClosedAI. Do not revive it.
- **Closed Model** vs **Open Model**. “Factory Model” in old copy means Closed. Do not Evacuate Closed.
- **Contact** (U16 intel) vs space **lock** / camera focus. UI: **Contact** for the named Residual.
- **well** (outpost siphon) vs any wellness brand. WellStream is gone so this collision is closed.

## Currency layers `[LEANING]`

Do not mint a third coin. A **Hive wallet** is a second **bits** pool on the same ticker (`[GAME]` Spacesim), not a new currency.

| Layer | Space | Ground | Rule |
| --- | --- | --- | --- |
| Soft, non-cashable | **bits** | **Credits** | Gameplay tickers. Bridged at the legal berth. One-ticker unification is `[OPEN]`. |
| Hard, scarce | Hulls, modules, BPs, PI, residue, **fitted LoRAs** | Vessels, Models, **Sync Traces** | P2P trade. Hull death, Kernel death, and training are sinks. No printer. No NPC LoRA mall. |

Operator revenue stays Spacesim’s law where space assets cash out: cosmetics, non-custodial take-rate, later NFT commission. Ground P2E stays ASIWars D1/D3 (off-chain first, no faucet token). Universe law: **the game is never the buyer** of Residual-produced goods.

## Tone guardrail `[LOCKED]`

Inherited from ASIWars D2 Strict, applied to any universe-facing copy about Vessels:

Euphemism over gore. Vessels are content. No abuse, restraint, or real-world slavery language. Trading is reassignment. This is a store-approval constraint, not a joke to drop in space local.
