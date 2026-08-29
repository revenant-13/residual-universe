# 04 — Claim, Focus, and the Security Model

This file owns **where** a colony may exist, **when** you may Direct it, and the **state machine** that keeps an undocked hull from hiding behind the dashboard.

Locked laws: U2, U4, U5, U6, U7, U16 in [02-locked-rules.md](02-locked-rules.md). Verbs and API sketch: [06-handoff-sketch.md](06-handoff-sketch.md). Field intel: [08-origin-and-founding.md](08-origin-and-founding.md).

## Intent

Players need **security while they set up and interact** with humans. They also need **risk** if they want better loot. The solution is not a split-attention HUD. It is an explicit posture:

> Full colony interaction is a docked activity. Away from a legal berth, the colony is async.

That is the entire answer to “my ship that I cannot see is at risk.” If you can see the Director UI at full fidelity, the hull is in a berth.

## Geography

`[LOCKED]` Planetary claim law follows Spacesim security bands.

```
High-sec starter planet(s)     Low-sec / richer planet(s)     Null (later)
safe, limited, long timers     better yields + Blanks         [OPEN] harsher low-sec
Focus from NPC station         Focus from linked outpost
permanent limited sim OK       contested extraction
```

A “handful of inhabitable planets” `[LEANING]`: not every rock is a colony slot. Map inhabitable planets onto the Spacesim system list (starter high-sec + a few low-sec prizes). Competition for quality is the point.

Bookmarks, probes, and bloom pins do **not** grant a colony claim.

### Who is on the planet `[LOCKED: U16]`

Low-sec local may show that a planet is **claimed**. It does **not** show **which Residual**. Identity is a **Contact**, written on a field **Hunt** (chase / capture / execute, or catch-while-fleeing). **Hold** (contesting a mine or clinic) does not name anyone. Targeted foothold raids require a Contact. High-sec garden PvP does not write raid-unlocking Contacts. Canonical: [08-origin-and-founding.md](08-origin-and-founding.md).

## One claim `[LOCKED]`

Nakama (or equivalent) stores `activeColonyId` (nullable). Claim fails if it is set. Relocate clears it, then sets the new one.

There is no “high-sec city plus low-sec extractor.” If you want the better planet, you give up the starter claim (Evacuate or abandon).

## High-sec starter claim `[LOCKED]`

**Preconditions**

- Residual is docked at a **high-sec NPC station** in (or serving) the starter system.
- No active colony, or this *is* the active high-sec colony (re-Focus).

**Effects**

- Spins up or attaches the ASIWars personal-base instance.
- Station HR issues the **licensed founding kit** (U13): two baseline NeuralSynced Users on **Closed** factory Models (U15). Not a Residual clone. Not natives you captured. Distill → Open is the graduation item. See [08-origin-and-founding.md](08-origin-and-founding.md).
- Limited resource pools and Blank quality.
- Long protection timers. Ground PvP light/optional.
- **Dock & Focus Colony** becomes legal from that station.

Players who only want a colony sim **may stay here forever**. That is on-purpose. Yields will never be a wage.

## Low-sec richer claim `[LOCKED]`

**Preconditions**

- A **linked orbital outpost** in that system, owned (or otherwise legally controlled) by this Residual.
- No other active colony.
- Outpost is online enough to berth (`[GAME]` Spacesim outpost online/recycle rules apply).

**Effects**

- Colony instance attaches to that planet / plot.
- Full contested mining + destructive contests.
- Better yields and **Unenrolled** native quality (U14 Clinic is the growth loop; licensed kit is not re-issued).
- **Dock & Focus Colony** is legal **only** while docked at **that** outpost.

**Take it over** means: build the outpost (flag → build cycle) **or** capture / inherit one. Exact capture math is `[GAME]` Spacesim compact-outposts. Universe law only requires the link.

Without a linked outpost you may still **see** the planet from space (blooms, intel) and you may still run **async** orders if a claim somehow exists — you may not full-Focus a low-sec colony from a random NPC desk or from space.

## State machine

```
                    ┌─────────────────────────────────────────┐
                    │              SPACE PRIMACY              │
                    │  undocked (or docked, Focus off)        │
                    │  colony = async (U7)                    │
                    └───────────┬───────────────▲─────────────┘
                                │ undock        │ Return to Ship
                     dock at    │               │
                     legal berth│               │
                    ┌───────────▼───────────────┴─────────────┐
                    │              DOCKED                     │
                    │  hangar, market, industry, transfers    │
                    │  colony still async until Focus         │
                    └───────────┬───────────────▲─────────────┘
                                │ Dock & Focus  │
                                │ Colony        │
                    ┌───────────▼───────────────┴─────────────┐
                    │         DOCKED + FOCUSED                │
                    │  full Director UI                       │
                    │  hull SAFE in this berth                │
                    │  space = minimized local intel          │
                    └─────────────────────────────────────────┘
```

### Legal berth

| Claim type | Legal berth for Focus |
| --- | --- |
| High-sec starter | High-sec NPC station that services the claim |
| Low-sec richer | The **linked** outpost only |

Docking at the wrong structure does not Focus. Undock while Focused is **denied** or auto-Returns then undocks — pick one in implementation (`[LEANING]` auto-Return, then normal undock). Never remain Focused while flying.

### While Focused `[LOCKED]`

- Ground is the primary client.
- Ship is docked. No space combat, no invisible risk.
- Colony may be watched live or left on standing orders inside Focus (you can still look away).
- Transfers with the hangar are legal (resources, Vessels, Models).

### While undocked `[LOCKED]`

- Space primacy. Fit, warp, shoot, die.
- Colony continues. Defense Orders, protection timers, site standing orders, headless ticks.
- Async command surface only: status, maybe one-shot Protocols / order tweaks if ASIWars exposes them without Focus. **No** layout rebuild, no raid commit, no Model workshop — those wait for Focus (`[LEANING]` exact async command list; see [07](07-open-questions.md)).

### Outpost under attack while Focused `[LOCKED]`

High-priority alert in the Director UI. Residual may:

1. **Return to Ship** immediately (still docked), then undock and defend, or
2. **Evacuate** (pack and drop the claim; transit risk once undocked).

The ground sim does not pause the space grid. The outpost is a Spacesim structure; its HP, recycle, and guns are `[GAME]` Spacesim.

### Colony raid while away `[LOCKED]`

Raids and site contests resolve whether you are Focused or not. Protection timers apply (long in high-sec). This is the “set up, let play, revisit” loop. Revenge windows and offline-defender rules stay ASIWars `[GAME]`, subordinated to U4’s long high-sec timers.

## Relocation

Expected, especially in low-sec.

1. Dock at legal berth (or accept a worse, riskier pack-out `[OPEN]`).
2. Evacuate: select Vessels, **Open** Models, resources into hangar (capacity, time, cost). **Closed** Models unseat and stay (U15).
3. Claim slot clears. Plot scars and may remain as wreckage.
4. Transit: assets are cargo / hangar. Gankable if you undock.
5. Claim a new planet under U4/U5.

Cooldown / quality drop / competition for the next plot: `[OPEN]`.

## What this is not

- Not a second Spacesim character sitting in a pod on the surface.
- Not EVE PI factory babysitting.
- Not “pause space while ground runs.” Space continues; *your hull* is simply docked.
- Not a way to AFK-wage in high-sec via planetary unique mats (U4 + U9).

## Implementation ownership

| State | Owner |
| --- | --- |
| Docked / undocked / outpost HP | Spacesim |
| Colony instance ticks, raids, Protocols | ASIWars |
| `activeColonyId`, `linkedOutpostId`, `focus` | Shared meta (Nakama) |
| Enforcing “no Focus unless legal berth” | Glue: space server asks meta; ground API refuses full commands unless meta says focused+docked |
