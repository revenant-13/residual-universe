# Hull silhouette donors (pack adaptation)

**Date:** 2026-09-07  
**Status:** Approved  
**Parent:** Spacesim [2026-08-22-hull-kitbash-design.md](https://github.com/revenant-13/spacesim/blob/main/docs/superpowers/specs/2026-08-22-hull-kitbash-design.md)  
**Art root:** `art/` in this repo

The in-game catalog hulls are still box-kitbash (`createHullMesh` in Spacesim). They read as debug frustums. A CC0 low-poly pack (Inborn Ninja / OpenGameArt “3D Spaceships pack”) has readable silhouettes at 236–640 faces. We adapt three of those meshes as **silhouette donors** — keep pack topology, split into the named parts the client already expects, do not drop the glTF in raw and do not rebuild from primitives.

This spec owns the Blender sources. It does **not** wire glTF into Spacesim. Box kitbash stays live in the client until a later PR.

## Locked

| Item | Choice |
|------|--------|
| Method | Silhouette donors. Pack topology kept. Face-island split into named parts. No booleans. No subdiv. |
| Who (this pass) | Rookie, Dart, Striker |
| Donor map | ship2 → Rookie; ship1 → Dart; ship5 → Striker |
| Forward | Local **+Z is nose**, **+Y up**, **−Z engines**. Same as kitbash. |
| Origin | Visual center. Engine mesh origin = nozzle, local −Z aft. |
| Transforms | Applied before save. No leftover rotation/scale on export. |
| Materials | Two only: `hull` (body + nose, team-tint target) and `trim` (wings, engines, gun barrels). No textures. |
| Client-only | `selectRing` and `engineGlow` are **not** in the blend. Plume stays code. |
| Scale | Same units as current procedural meshes. Scale a hull only if a ranking below would fail. |
| Poly | Keep pack counts: Dart 247, Rookie 348, Striker 451 faces. |
| Client | No Spacesim PR. No glTF in the client. |
| Old blends | Archive, do not overwrite. |

## Donor map

Source (read-only): `C:\Users\jhall\Downloads\Spaceship_pack\dist\blend\`  
Review lineup (unlabeled): `art/pack-review.blend`

| Catalog | Donor | Read as | Faces | Distinct parts |
|---------|-------|---------|------:|----------------|
| Rookie | ship2 | Short blunt trainer | 348 | body, nose, wingL, wingR, engine |
| Dart | ship1 | Needle frigate | 247 | body, nose, wingL, wingR, engine |
| Striker | ship5 | Winged DPS frig | 451 | body, wingL, wingR, engineL, engineR |

Striker has **no** `nose` object. Do not invent one.

Kernel stays the emissive octahedron. Combat drone, Bulwark, Sledge, Bastion, Tender, station, and gate are out of this pass.

## Hierarchy

Object names **are** the contract. Catalog id is the root empty.

```
<hullId>                 empty
  hull                   empty
    body                 mesh, material hull
    nose                 mesh, material hull   (Rookie, Dart only)
    wingL                mesh, material trim
    wingR                mesh, material trim
    engine               mesh, material trim   (Rookie, Dart)
    engineL / engineR    mesh, material trim   (Striker)
```

Split method: edit mode, select face islands, Separate. If a part has no clean island (likely Rookie `nose`), cut a loop. Do not boolean. Do not add volume the pack did not have.

## Silhouette ranking

Must still hold after adaptation (same inequalities Spacesim `hullMesh.test.ts` uses for these three):

1. Dart length (+Z extent) **>** Rookie length.
2. Dart width (+X extent) **<** Striker width.

Pack sizes already satisfy this (Dart ~3.58 long × 1.99 wide; Rookie ~2.44 long; Striker ~3.85 wide). Touch scale only to keep those two inequalities.

## Archive then write

Before creating a new catalog-id blend, move the current basic file:

| Current | Archive as |
|---------|------------|
| `art/rookie.blend` | `art/archive/rookie-box-kitbash.blend` |
| `art/striker.blend` | `art/archive/striker-box-kitbash.blend` |
| `art/dart-frigate.blend` | `art/archive/dart-frigate-box-kitbash.blend` |

`.blend1` autosaves move with the parent or are deleted. They are not sources.

Do **not** move `art/bulwark.blend`, `kernel.blend`, `atrium-station.blend`, or `stargate.blend`.

New sources:

| File | Contents |
|------|----------|
| `art/rookie.blend` | Adapted ship2 |
| `art/dart.blend` | Adapted ship1 (new name; does not reuse `dart-frigate`) |
| `art/striker.blend` | Adapted ship5 |

`art/pack-review.blend` stays the nine-ship unlabeled lineup. The Downloads pack is never saved over.

## Done when

A hull file is done when all of these are true:

1. Object names match the hierarchy table for that hull id.
2. Transforms applied: +Z nose, origin centered, identity rotation/scale on the root.
3. Exactly two materials, named `hull` and `trim`, assigned as above.
4. Each engine mesh origin sits on its nozzle; local −Z points aft.
5. Silhouette ranking holds (Dart longer than Rookie; Dart narrower than Striker).
6. Top view and ¾ view: the hull is nameable from the mesh alone (needle / winged DPS / blunt trainer).

## Out

- Spacesim `hullMesh.ts` / glTF loader / tests
- Textures, UVs, baked AO
- Animated turrets, engine trails in the blend
- Kernel, drones, Bulwark, Sledge, Bastion, Tender
- Station and gate
- Sim, navigation, fits, slots
- Overwriting the archived box-kitbash blends
