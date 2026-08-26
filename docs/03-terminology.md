# 03 — Terminology Map

Mechanical terms stay **precise and stable**. Diegetic flavor can be funnier and may vary by surface (space overview vs Director dashboard). Universe-level nouns below are `[LOCKED]` unless marked otherwise.

Naming principle (from ASIWars, now universe-wide): every mechanic noun should carry **both** an ML meaning and a care/corporate meaning where possible. Space keeps EVE-like operational language; do not rename “warp” to “inference hop.”

## Residual identity

| Term | Meaning | Spacesim today | ASIWars today |
| --- | --- | --- | --- |
| **Residual** `[LOCKED]` | The player. Leftover superintelligence fragment. No body. | Implicit “pilot” / character | Residual / identity |
| **Director** `[LOCKED]` | Role title while focused on a colony. Same being. | n/a | Director dashboard |
| **WellStream™** `[LEANING]` | In-fiction implant + stewardship platform. Ground UI chrome. | n/a | WellStream™ / Neighbor |
| **Fork** `[GAME]` | Optional prestige copy of a Residual (ASIWars, post-MVP). | n/a | Prestige layer |

Do not introduce a second player noun (“Captain,” “Operator”) in design docs. UI slang on the space side (“pilot,” “capsuleer-class hull”) is flavor.

## Ground: people and weights

| Term | Meaning |
| --- | --- |
| **Vessel** `[LOCKED]` | A human unit. Mechanical term. UI may say Users / Residents. |
| **Blank** `[LOCKED]` | Low-tier wild / starter human. Flavor: Base Model. |
| **Tuned / Fine-tune** `[LOCKED]` | Trained-up Blank. Fine-tune = you trained it (pedigree). |
| **Prime** `[LOCKED]` | High-trait Vessel. Mostly stolen or slowly trained. |
| **Model** `[LOCKED]` | Loadable **weights** artifact: decision tree + weight allocation + trained skills. Separable from the human. Traded on the Model Hub. |
| **Protocol** `[LOCKED]` | Live nudge: push–pull on priors. Crafted, equippable. Model *allocates*; Protocol *steers*. |
| **Zone** `[LOCKED]` | Spatial priority (Collection, Attention, Defense, Attractor, Repulsor…). Vessels gravitate; they are not ordered to a tile. |
| **Inference** `[LEANING]` | One resolved nudge attempt (success/fail roll). |
| **Drift** `[LEANING]` | Reversion toward base priors. Fought with colony condition and repeated Protocols. |
| **Obedience** `[LOCKED]` (ASIWars D30) | How reliably a Vessel follows intent vs its own Drives. |
| **VRAM** `[LOCKED]` (ASIWars D17/D31) | Per-Vessel complexity budget and colony hosting pool (compute hardware). |
| **Checkpoint** `[LOCKED]` (ASIWars D21) | Pre-emptive Model backup. Insures weights, not the body. |
| **Distill** `[LOCKED]` (ASIWars D19) | Lossy copy of a Model. Originals stay premium. |
| **Offboarding** | Death/removal euphemism. |
| **Reassignment / onboarding** | Trade/transfer euphemism. Never “sale of people” in UI. |

Provenance tags stay ASIWars `[GAME]`: `WildBorn` / `Trained` / `Stolen` (hot goods).

Capture vs kill (weights rule) stays ASIWars `[GAME]`: killed → salvage Model at a loss; captured → Model lost to the enemy. Universe copy may use it; do not re-tune it here.

## Ground: colony verbs

| Verb | Meaning |
| --- | --- |
| **Claim** | Attach this Residual’s **one** colony slot to a planet (or designated plot on it). High-sec: from a high-sec station dock. Low-sec: requires linked outpost. |
| **Inhabit** | Fantasy synonym for holding a claim. Not a second mechanic. |
| **Focus** | Enter full Director interaction. Requires docked-for-full-focus (U6). |
| **Return (to Ship)** | Leave Focus. Client back to space. Hull still docked until you undock. |
| **Evacuate** | Pack Vessels / Models / resources into hangar, drop or abandon the claim, accept transit risk. |
| **Relocate** | Evacuate (or abandon) + Claim elsewhere. One-claim rule still holds. |

## Space: keep the native words

Do not Residual-wash navigation or combat.

| Term | Meaning | Residual mapping |
| --- | --- | --- |
| **bits** | Spacesim soft currency. Shift leftover unit of account. | Soft layer. May sit beside ASIWars **Credits / Compute Credits**. Bridged, not necessarily renamed. `[OPEN]` whether one ticker wins. |
| **USDC / export** | Player-to-player cash-out. Docked, delayed, skill-gated. Game never the buyer. | Hard layer. Ground unique goods that reach space hangars follow **space** export law. |
| **high-sec / low-sec / null** | Security geography. CONCORD-like response in high-sec. | Same map for planetary claim law (U4/U5). |
| **station** | NPC dock. Safe berth. Markets, industry, insurance. | High-sec **legal berth** for starter colony Focus. |
| **outpost** | Player structure (compact-outpost design). Build / recycle / flag / well. | **Linked orbital outpost** = low-sec claim gate and Focus berth. |
| **flag / well / residue / slag** | Outpost claim stake, siphon source, siphon goods, scrap goods. | Residue/slag remain space-side products. Planetary unique mats are a **different** input class (U9). |
| **planetary pad / bloom window** | v1 space-side PI: stay in ship, extract at a pin, haul. Nobody lands. | Lighter space-side PI. Dual source vs phased-down is `[OPEN]`. Not colony Focus. |
| **PI** | Planetary industry ids (e.g. biomass, refractory, sludge). | Space-side extractables. Ground contests add **unique / higher** ids that belts/blooms cannot print. |
| **T1 / T2 / invention** | Industry ladder. High-sec cannot close T2. | Ground unique mats are on the T2 / special path (U9). |
| **hull / module / drone** | Fitted space assets at risk when undocked. | Residual’s space body. |
| **grid / system / gate** | Combat space, solar system, travel. | Unchanged. |

## Crosswalk (quick)

When a Spacesim doc says… write Residual Universe as…

| Spacesim | Residual Universe |
| --- | --- |
| Character / pilot | Residual |
| Dock at station and “do PI” (v1 blooms) | Stay in ship; not Focus |
| Compact outpost | Orbital anchor for a low-sec **claim** |
| High-sec | Starter claim legal; trash yields; Focus from NPC station |
| Low-sec | Richer claim; outpost-gated; Focus from linked outpost |
| Hangar | Shared with colony export/import when docked at the legal berth |
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
| Director dashboard | Focused colony UI |
| Raid / protection timer | Still `[GAME]`, but high-sec timers are **long** (U4) |

## Collision watch

- **Residual** (the player) vs **residue** (outpost siphon good). Never abbreviate residue to “residual” in space UI.
- **Model** (weights artifact) vs **hull model** / mesh. Space docs say **hull**. Ground docs say **Model**.
- **Claim** (colony) vs **claimCompact** / loot claim in Spacesim rifts. Keep the verb qualified: **Claim planet** vs **claim loot**.
- **Station** (NPC) vs **outpost** (player). Only the latter gates low-sec colonies.
- **Focus** (Director mode) vs camera focus / lock. UI: **Dock & Focus Colony**.

## Currency layers `[LEANING]`

Do not mint a third coin.

| Layer | Space | Ground | Rule |
| --- | --- | --- | --- |
| Soft, non-cashable | **bits** | **Credits** | Gameplay tickers. Bridged at the legal berth. One-ticker unification is `[OPEN]`. |
| Hard, scarce | Hulls, modules, BPs, PI, residue | Vessels, Models, planetary mats | P2P trade. Destruction and training are sinks. No printer. |

Operator revenue stays Spacesim’s law where space assets cash out: cosmetics, non-custodial take-rate, later NFT commission. Ground P2E stays ASIWars D1/D3 (off-chain first, no faucet token). Universe law: **the game is never the buyer** of Residual-produced goods.

## Tone guardrail `[LOCKED]`

Inherited from ASIWars D2 Strict, applied to any universe-facing copy about Vessels:

Euphemism over gore. Vessels are content. No abuse, restraint, or real-world slavery language. Trading is reassignment. This is a store-approval constraint, not a joke to drop in space local.
