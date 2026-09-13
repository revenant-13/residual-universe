# Hull silhouette donors Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Archive the box-kitbash Rookie/Dart/Striker blends, then write three export-ready Blender hulls (`art/rookie.blend`, `art/dart.blend`, `art/striker.blend`) adapted from the CC0 pack donors with named parts, two materials, +Z nose, and engine origins on the nozzles.

**Architecture:** One verifier (`art/scripts/verify_hull.py`) encodes the spec contract. One adapter (`art/scripts/adapt_hull.py`) imports a pack GLB, reorients Y-forward Z-up → +Z nose +Y up, splits faces by spatial cuts (the donors are 110–161 disconnected islands, not watertight parts), assigns `hull`/`trim`, builds the empty hierarchy, snaps engine origins to the aft-most vertex. Each catalog id is a separate `.blend`. No Spacesim client changes.

**Tech Stack:** Blender 5.2 (MCP `execute_blender_code` + viewport screenshot). Pack GLBs at `C:\Users\jhall\Downloads\Spaceship_pack\dist\blend\`. Do **not** call `wm.read_homefile` (drops the MCP addon). Do **not** save over the Downloads pack or `art/pack-review.blend`. Skip git commit steps unless the user explicitly asked to commit.

**Spec:** [`docs/superpowers/specs/2026-09-07-hull-silhouette-donors-design.md`](../specs/2026-09-07-hull-silhouette-donors-design.md)

---

## File map

| File | Role |
|------|------|
| Create `art/archive/rookie-box-kitbash.blend` | Moved from `art/rookie.blend` |
| Create `art/archive/striker-box-kitbash.blend` | Moved from `art/striker.blend` |
| Create `art/archive/dart-frigate-box-kitbash.blend` | Moved from `art/dart-frigate.blend` |
| Create `art/scripts/verify_hull.py` | Contract checks (names, materials, +Z, engine origin, face counts, ranking) |
| Create `art/scripts/adapt_hull.py` | Import / reorient / split / material / hierarchy / save |
| Create `art/dart.blend` | Adapted ship1 |
| Create `art/rookie.blend` | Adapted ship2 (after archive) |
| Create `art/striker.blend` | Adapted ship5 (after archive) |
| Leave `art/pack-review.blend` | Unlabeled 9-ship lineup. Do not save into it. |
| Leave `art/bulwark.blend`, `kernel.blend`, `atrium-station.blend`, `stargate.blend` | Out of pass |
| Out | `spacesim/packages/client/src/hullMesh.ts` |

Donor GLBs (read-only):

| Catalog | GLB | Faces | Parts |
|---------|-----|------:|-------|
| dart | `ship1.glb` | 247 | body, nose, wingL, wingR, engine |
| rookie | `ship2.glb` | 348 | body, nose, wingL, wingR, engine |
| striker | `ship5.glb` | 451 | body, wingL, wingR, engineL, engineR |

Spatial cuts are in **donor local space** (X = width, Y = length with tail more negative, Z = height), then the mesh is reoriented. Measured on the pack GLBs:

| Hull | engine | nose | wingL | wingR |
|------|--------|------|-------|-------|
| dart | `y < -0.5` | `y > 1.0` | `x < -0.33` | `x > 0.33` |
| rookie | `y < -0.95 and abs(x) < 0.55` | `y > 0.85 and abs(x) < 0.6` | `x < -0.70` | `x > 0.70` |
| striker | L: `y < -1.05 and -1.35 < x < -0.55`; R: `y < -1.05 and 0.55 < x < 1.35` | none | `x < -0.70` | `x > 0.70` |

Remainder is `body`. First matching rule wins (engines and nose before wings).

---

### Task 1: Archive box-kitbash blends

**Files:**
- Move: `art/rookie.blend` → `art/archive/rookie-box-kitbash.blend`
- Move: `art/striker.blend` → `art/archive/striker-box-kitbash.blend`
- Move: `art/dart-frigate.blend` → `art/archive/dart-frigate-box-kitbash.blend`
- Move if present: matching `.blend1` autosaves next to those archive names

- [ ] **Step 1: Create archive dir and move the three sources**

Run from `C:\MyApps\residual-universe` in PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path art\archive | Out-Null
$pairs = @(
  @{ From = 'art\rookie.blend';          To = 'art\archive\rookie-box-kitbash.blend' },
  @{ From = 'art\striker.blend';         To = 'art\archive\striker-box-kitbash.blend' },
  @{ From = 'art\dart-frigate.blend';    To = 'art\archive\dart-frigate-box-kitbash.blend' }
)
foreach ($p in $pairs) {
  if (-not (Test-Path $p.From)) { throw "missing source $($p.From)" }
  if (Test-Path $p.To) { throw "archive already exists $($p.To) — stop, do not overwrite" }
  Move-Item -LiteralPath $p.From -Destination $p.To
  $bak = $p.From + '1'
  if (Test-Path $bak) {
    Move-Item -LiteralPath $bak -Destination ($p.To + '1')
  }
}
Get-ChildItem art\archive | Select-Object Name, Length
Get-ChildItem art\*.blend | Select-Object Name
```

Expected: archive contains the three `*-box-kitbash.blend` files. `art\` still has `pack-review.blend`, `bulwark.blend`, `kernel.blend`, `atrium-station.blend`, `stargate.blend`. No `rookie.blend`, `striker.blend`, or `dart-frigate.blend` at `art\` root.

- [ ] **Step 2: Confirm the Downloads pack is untouched**

```powershell
Get-ChildItem 'C:\Users\jhall\Downloads\Spaceship_pack\dist\blend\ship*.blend' | Select-Object Name, Length, LastWriteTime
```

Expected: `ship1.blend`–`ship9.blend` still present. Do not write these paths in later tasks.

- [ ] **Step 3: Commit (skip unless the user asked)**

```bash
git add art/archive/*.blend
git commit -m "chore(art): archive box-kitbash rookie, striker, dart-frigate"
```

---

### Task 2: Verifier (failing before any adapted hull exists)

**Files:**
- Create: `art/scripts/verify_hull.py`

- [ ] **Step 1: Write the verifier**

Create `art/scripts/verify_hull.py` with this exact content:

```python
"""Contract checks for silhouette-donor hull blends. Run inside Blender via exec()."""
from __future__ import annotations

from pathlib import Path

import bpy
from mathutils import Vector

ART_ROOT = Path(r"C:\MyApps\residual-universe\art")

PARTS = {
    "rookie": ["body", "nose", "wingL", "wingR", "engine"],
    "dart": ["body", "nose", "wingL", "wingR", "engine"],
    "striker": ["body", "wingL", "wingR", "engineL", "engineR"],
}
HULL_MAT_PARTS = {
    "rookie": ["body", "nose"],
    "dart": ["body", "nose"],
    "striker": ["body"],
}
TRIM_MAT_PARTS = {
    "rookie": ["wingL", "wingR", "engine"],
    "dart": ["wingL", "wingR", "engine"],
    "striker": ["wingL", "wingR", "engineL", "engineR"],
}
PACK_FACES = {"rookie": 348, "dart": 247, "striker": 451}
ENGINE_PARTS = {
    "rookie": ["engine"],
    "dart": ["engine"],
    "striker": ["engineL", "engineR"],
}
FORBIDDEN = {"selectRing", "engineGlow"}


class VerifyError(Exception):
    pass


def _mesh_bbox_world(obj) -> tuple[Vector, Vector]:
    inf = 1e9
    mn = Vector((inf, inf, inf))
    mx = Vector((-inf, -inf, -inf))
    for v in obj.data.vertices:
        w = obj.matrix_world @ v.co
        for i in range(3):
            mn[i] = min(mn[i], w[i])
            mx[i] = max(mx[i], w[i])
    return mn, mx


def _hull_bbox(root) -> tuple[Vector, Vector]:
    inf = 1e9
    mn = Vector((inf, inf, inf))
    mx = Vector((-inf, -inf, -inf))
    for obj in root.children_recursive:
        if obj.type != "MESH":
            continue
        a, b = _mesh_bbox_world(obj)
        for i in range(3):
            mn[i] = min(mn[i], a[i])
            mx[i] = max(mx[i], b[i])
    return mn, mx


def _mat_name(obj) -> str:
    if not obj.data.materials:
        return ""
    mat = obj.data.materials[0]
    return mat.name if mat else ""


def verify_open_scene(hull_id: str) -> list[str]:
    errors: list[str] = []
    root = bpy.data.objects.get(hull_id)
    if root is None or root.type != "EMPTY":
        return [f"missing root empty named {hull_id!r}"]
    if any(abs(x) > 1e-4 for x in root.rotation_euler):
        errors.append(f"root rotation not identity: {list(root.rotation_euler)}")
    if any(abs(x - 1.0) > 1e-4 for x in root.scale):
        errors.append(f"root scale not 1: {list(root.scale)}")
    hull = next((c for c in root.children if c.name == "hull"), None)
    if hull is None or hull.type != "EMPTY":
        errors.append("missing child empty named hull")
        return errors
    names = {o.name: o for o in hull.children}
    for part in PARTS[hull_id]:
        obj = names.get(part)
        if obj is None or obj.type != "MESH":
            errors.append(f"missing mesh part {part}")
    if hull_id == "striker" and "nose" in names:
        errors.append("striker must not have a nose object")
    for bad in FORBIDDEN:
        if bpy.data.objects.get(bad) is not None:
            errors.append(f"forbidden object present: {bad}")
    mats = {m.name for m in bpy.data.materials if m.users}
    extra = mats - {"hull", "trim"}
    if "hull" not in mats or "trim" not in mats:
        errors.append(f"need materials named hull and trim, have {sorted(mats)}")
    if extra:
        errors.append(f"unexpected materials: {sorted(extra)}")
    for part in HULL_MAT_PARTS[hull_id]:
        obj = names.get(part)
        if obj and _mat_name(obj) != "hull":
            errors.append(f"{part} material is {_mat_name(obj)!r}, want hull")
    for part in TRIM_MAT_PARTS[hull_id]:
        obj = names.get(part)
        if obj and _mat_name(obj) != "trim":
            errors.append(f"{part} material is {_mat_name(obj)!r}, want trim")
    present = [names[p] for p in PARTS[hull_id] if p in names and names[p].type == "MESH"]
    faces = sum(len(o.data.polygons) for o in present)
    if faces != PACK_FACES[hull_id]:
        errors.append(f"face count {faces} != pack {PACK_FACES[hull_id]}")
    if present:
        mn, mx = _hull_bbox(root)
        size = mx - mn
        if mx.z <= 0:
            errors.append(f"nose is not +Z (max.z={mx.z:.3f})")
        if mx.z <= -mn.z * 0.35:
            errors.append(f"+Z extent too small vs tail (max.z={mx.z:.3f} min.z={mn.z:.3f})")
        for part in ENGINE_PARTS[hull_id]:
            eng = names.get(part)
            if eng is None:
                continue
            origin = eng.matrix_world.translation
            if origin.z > mn.z + 0.2:
                errors.append(
                    f"{part} origin z={origin.z:.3f} not on nozzle (hull min.z={mn.z:.3f})"
                )
        print(
            f"VERIFY_BOUNDS {hull_id} size=[{size.x:.3f}, {size.y:.3f}, {size.z:.3f}] "
            f"min.z={mn.z:.3f} max.z={mx.z:.3f}"
        )
    return errors


def bbox_size(hull_id: str) -> Vector:
    root = bpy.data.objects[hull_id]
    mn, mx = _hull_bbox(root)
    return mx - mn


def verify_ranking() -> list[str]:
    errors: list[str] = []
    dart = bbox_size("dart")
    rookie = bbox_size("rookie")
    striker = bbox_size("striker")
    if dart.z <= rookie.z:
        errors.append(f"dart length {dart.z:.3f} must be > rookie {rookie.z:.3f}")
    if dart.x >= striker.x:
        errors.append(f"dart width {dart.x:.3f} must be < striker {striker.x:.3f}")
    return errors


def report(errors: list[str], label: str) -> None:
    if errors:
        print(f"VERIFY_FAIL {label}")
        for e in errors:
            print(" -", e)
        raise RuntimeError(f"VERIFY_FAIL {label}: {len(errors)} errors")
    print(f"VERIFY_PASS {label}")
```

- [ ] **Step 2: Run the verifier against the current Blender scene (expect FAIL)**

In Blender MCP `execute_blender_code`:

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\verify_hull.py", encoding="utf-8").read(), "verify_hull.py", "exec"))
errs = verify_open_scene("dart")
print(errs)
report(errs, "dart")
```

Expected: `VERIFY_FAIL dart` with `missing root empty named 'dart'`. Do not proceed if it passes — the scene already has an adapted hull and this task cannot prove the verifier catches a miss.

---

### Task 3: Adapter script

**Files:**
- Create: `art/scripts/adapt_hull.py`

- [ ] **Step 1: Write the adapter**

Create `art/scripts/adapt_hull.py` with this exact content:

```python
"""Adapt one pack GLB into a catalog hull in the current Blender scene."""
from __future__ import annotations

import math
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

ART_ROOT = Path(r"C:\MyApps\residual-universe\art")
PACK_DIR = Path(r"C:\Users\jhall\Downloads\Spaceship_pack\dist\blend")

HULLS = {
    "dart": {
        "glb": "ship1.glb",
        "out": ART_ROOT / "dart.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.5),
            ("nose", lambda c: c.y > 1.0),
            ("wingL", lambda c: c.x < -0.33),
            ("wingR", lambda c: c.x > 0.33),
        ],
        "hull_parts": ("body", "nose"),
        "trim_parts": ("wingL", "wingR", "engine"),
        "engines": ("engine",),
    },
    "rookie": {
        "glb": "ship2.glb",
        "out": ART_ROOT / "rookie.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.95 and abs(c.x) < 0.55),
            ("nose", lambda c: c.y > 0.85 and abs(c.x) < 0.6),
            ("wingL", lambda c: c.x < -0.70),
            ("wingR", lambda c: c.x > 0.70),
        ],
        "hull_parts": ("body", "nose"),
        "trim_parts": ("wingL", "wingR", "engine"),
        "engines": ("engine",),
    },
    "striker": {
        "glb": "ship5.glb",
        "out": ART_ROOT / "striker.blend",
        "rules": [
            ("engineL", lambda c: c.y < -1.05 and -1.35 < c.x < -0.55),
            ("engineR", lambda c: c.y < -1.05 and 0.55 < c.x < 1.35),
            ("wingL", lambda c: c.x < -0.70),
            ("wingR", lambda c: c.x > 0.70),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("wingL", "wingR", "engineL", "engineR"),
        "engines": ("engineL", "engineR"),
    },
}


def clear_work() -> None:
    keep_types = {"CAMERA", "LIGHT"}
    for obj in list(bpy.data.objects):
        if obj.type not in keep_types:
            bpy.data.objects.remove(obj, do_unlink=True)
    for mesh in list(bpy.data.meshes):
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for mat in list(bpy.data.materials):
        if mat.users == 0:
            bpy.data.materials.remove(mat)
    for curve in list(bpy.data.curves):
        if curve.users == 0:
            bpy.data.curves.remove(curve)


def _ensure_material(name: str, color: tuple[float, float, float, float], metallic: float, roughness: float):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        if "Metallic" in bsdf.inputs:
            bsdf.inputs["Metallic"].default_value = metallic
        if "Roughness" in bsdf.inputs:
            bsdf.inputs["Roughness"].default_value = roughness
    mat.diffuse_color = color
    return mat


def _import_glb(path: Path):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    new = [o for o in bpy.data.objects if o not in before and o.type == "MESH"]
    if len(new) != 1:
        raise RuntimeError(f"expected 1 mesh from {path.name}, got {[o.name for o in new]}")
    obj = new[0]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    return obj


def _reorient_plus_z_nose(obj) -> None:
    """Donor +Y nose +Z up → +Z nose +Y up. Apply. Recalc normals."""
    obj.rotation_euler = (math.radians(90.0), 0.0, 0.0)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    obj.scale = (1.0, -1.0, 1.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()


def _split(obj, rules: list) -> dict:
    me = obj.data
    groups = {name: [] for name, _fn in rules}
    groups["body"] = []
    for poly in me.polygons:
        hit = "body"
        for name, fn in rules:
            if fn(poly.center):
                hit = name
                break
        groups[hit].append(poly.index)
    empty = [name for name, idxs in groups.items() if not idxs]
    if empty:
        raise RuntimeError(f"{obj.name} produced empty parts: {empty} counts={[ (n,len(i)) for n,i in groups.items() ]}")
    created = {}
    for name, idxs in groups.items():
        keep = set(idxs)
        new_me = me.copy()
        new_me.name = name
        new_obj = bpy.data.objects.new(name, new_me)
        bpy.context.scene.collection.objects.link(new_obj)
        new_obj.matrix_world = obj.matrix_world.copy()
        bm = bmesh.new()
        bm.from_mesh(new_me)
        bm.faces.ensure_lookup_table()
        bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.index not in keep], context="FACES")
        bm.to_mesh(new_me)
        bm.free()
        new_me.update()
        created[name] = new_obj
    bpy.data.objects.remove(obj, do_unlink=True)
    return created


def _assign(obj, mat) -> None:
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def _set_origin_world(obj, world_pt: Vector) -> None:
    mw = obj.matrix_world.copy()
    local = mw.inverted() @ world_pt
    obj.data.transform(Matrix.Translation(-local))
    obj.data.update()
    new = mw.copy()
    new.translation = world_pt
    obj.matrix_world = new


def _aft_vertex_world(obj) -> Vector:
    return min((obj.matrix_world @ v.co for v in obj.data.vertices), key=lambda w: w.z)


def _center_root(root) -> None:
    inf = 1e9
    mn = Vector((inf, inf, inf))
    mx = Vector((-inf, -inf, inf * -1))
    meshes = [o for o in root.children_recursive if o.type == "MESH"]
    for o in meshes:
        for v in o.data.vertices:
            w = o.matrix_world @ v.co
            for i in range(3):
                mn[i] = min(mn[i], w[i])
                mx[i] = max(mx[i], w[i])
    center = (mn + mx) * 0.5
    for o in meshes:
        mw = o.matrix_world.copy()
        mw.translation = mw.translation - center
        o.matrix_world = mw
    root.location = (0.0, 0.0, 0.0)
    root.rotation_euler = (0.0, 0.0, 0.0)
    root.scale = (1.0, 1.0, 1.0)


def adapt(hull_id: str) -> None:
    spec = HULLS[hull_id]
    glb = PACK_DIR / spec["glb"]
    if not glb.is_file():
        raise FileNotFoundError(glb)
    if spec["out"].is_file():
        raise RuntimeError(f"refusing to overwrite {spec['out']}")
    clear_work()
    donor = _import_glb(glb)
    parts = _split(donor, spec["rules"])
    for obj in parts.values():
        _reorient_plus_z_nose(obj)
    hull_mat = _ensure_material("hull", (0.55, 0.62, 0.72, 1.0), 0.42, 0.46)
    trim_mat = _ensure_material("trim", (0.18, 0.20, 0.22, 1.0), 0.55, 0.38)
    for name in spec["hull_parts"]:
        _assign(parts[name], hull_mat)
    for name in spec["trim_parts"]:
        _assign(parts[name], trim_mat)
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0.0, 0.0, 0.0))
    root = bpy.context.active_object
    root.name = hull_id
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0.0, 0.0, 0.0))
    hull = bpy.context.active_object
    hull.name = "hull"
    hull.parent = root
    for name, obj in parts.items():
        obj.name = name
        obj.parent = hull
        obj.matrix_parent_inverse = hull.matrix_world.inverted()
    for name in spec["engines"]:
        eng = parts[name]
        _set_origin_world(eng, _aft_vertex_world(eng))
    _center_root(root)
    bpy.ops.wm.save_as_mainfile(filepath=str(spec["out"]))
    print("ADAPT_SAVED", spec["out"], "parts", sorted(parts))
```

Note: split happens **before** reorient so the cut planes stay in the measured donor local space (X width, Y length). Each separated part is then rotated the same way.

- [ ] **Step 2: Load the adapter in Blender (no hull yet)**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\adapt_hull.py", encoding="utf-8").read(), "adapt_hull.py", "exec"))
print(sorted(HULLS))
```

Expected: `['dart', 'rookie', 'striker']`. No `.blend` written yet.

---

### Task 4: Dart (ship1)

**Files:**
- Create: `art/dart.blend`
- Test: `art/scripts/verify_hull.py`

- [ ] **Step 1: Adapt Dart**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\adapt_hull.py", encoding="utf-8").read(), "adapt_hull.py", "exec"))
adapt("dart")
```

Expected: `ADAPT_SAVED C:\MyApps\residual-universe\art\dart.blend parts ['body', 'engine', 'nose', 'wingL', 'wingR']`. `art/dart.blend` exists. Downloads `ship1.blend` / `ship1.glb` unchanged.

- [ ] **Step 2: Verify Dart**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\verify_hull.py", encoding="utf-8").read(), "verify_hull.py", "exec"))
report(verify_open_scene("dart"), "dart")
```

Expected: `VERIFY_PASS dart`. Face count 247. Bounds print with `max.z > 0` and length (~Z) around 3.5.

If `engine origin z not on nozzle`: the origin snap used a vertex that is not the nozzle. Inspect the engine mesh, snap to the aft cluster (min Z), re-save, re-verify.

If `+Z extent too small`: reorient applied twice or skip. Re-run `adapt` only after deleting `art/dart.blend` (the adapter refuses overwrite).

If a part is empty: stop and tighten that one cut in `HULLS['dart']['rules']`; do not boolean and do not add faces.

- [ ] **Step 3: Viewport — top and ¾, confirm needle**

```python
import bpy
from mathutils import Euler

root = bpy.data.objects["dart"]
for o in bpy.data.objects:
    o.select_set(o == root or o.parent == root or (o.parent and o.parent.parent == root))
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.shading.type = "SOLID"
        space.shading.color_type = "MATERIAL"
        space.overlay.show_extras = False
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_axis(type="TOP")
            bpy.ops.view3d.view_selected()
```

Then `get_viewport_screenshot`. Expected: long needle, wings mid-aft, you can name it Dart from the mesh.

Then ¾:

```python
import bpy
from mathutils import Euler
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.region_3d.view_perspective = "PERSP"
        space.region_3d.view_rotation = Euler((1.05, 0.0, 0.7), "XYZ").to_quaternion()
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_selected()
```

Screenshot again. Expected: +Y is up (not flipped into the grid), engines at the tail.

- [ ] **Step 4: Commit (skip unless the user asked)**

```bash
git add art/dart.blend art/scripts/adapt_hull.py art/scripts/verify_hull.py
git commit -m "feat(art): dart hull from pack ship1 silhouette donor"
```

---

### Task 5: Rookie (ship2)

**Files:**
- Create: `art/rookie.blend`
- Test: `art/scripts/verify_hull.py`

- [ ] **Step 1: Adapt Rookie**

`adapt()` refuses to overwrite `dart.blend` because it `save_as` the current file — first confirm Blender’s `bpy.data.filepath` is not the pack. Then:

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\adapt_hull.py", encoding="utf-8").read(), "adapt_hull.py", "exec"))
adapt("rookie")
```

Expected: `ADAPT_SAVED ...\art\rookie.blend parts ['body', 'engine', 'nose', 'wingL', 'wingR']`. `art/archive/rookie-box-kitbash.blend` still exists. `art/dart.blend` still exists on disk (we saved a different filepath).

- [ ] **Step 2: Verify Rookie**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\verify_hull.py", encoding="utf-8").read(), "verify_hull.py", "exec"))
report(verify_open_scene("rookie"), "rookie")
```

Expected: `VERIFY_PASS rookie`. Face count 348. Length shorter than Dart’s ~3.5 (around 2.4).

- [ ] **Step 3: Viewport — top and ¾, confirm blunt trainer**

```python
import bpy
from mathutils import Euler

root = bpy.data.objects["rookie"]
for o in bpy.data.objects:
    o.select_set(o == root or o.parent == root or (o.parent and o.parent.parent == root))
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.shading.type = "SOLID"
        space.shading.color_type = "MATERIAL"
        space.overlay.show_extras = False
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_axis(type="TOP")
            bpy.ops.view3d.view_selected()
```

`get_viewport_screenshot`. Expected: short blunt trainer, side sticks, not a needle.

Then ¾:

```python
import bpy
from mathutils import Euler
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.region_3d.view_perspective = "PERSP"
        space.region_3d.view_rotation = Euler((1.05, 0.0, 0.7), "XYZ").to_quaternion()
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_selected()
```

Screenshot. Expected: +Y up, engine at the tail.

- [ ] **Step 4: Commit (skip unless the user asked)**

```bash
git add art/rookie.blend
git commit -m "feat(art): rookie hull from pack ship2 silhouette donor"
```

---

### Task 6: Striker (ship5)

**Files:**
- Create: `art/striker.blend`
- Test: `art/scripts/verify_hull.py`

- [ ] **Step 1: Adapt Striker**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\adapt_hull.py", encoding="utf-8").read(), "adapt_hull.py", "exec"))
adapt("striker")
```

Expected: `ADAPT_SAVED ...\art\striker.blend parts ['body', 'engineL', 'engineR', 'wingL', 'wingR']`. No `nose` in the parts list.

- [ ] **Step 2: Verify Striker**

```python
exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\verify_hull.py", encoding="utf-8").read(), "verify_hull.py", "exec"))
report(verify_open_scene("striker"), "striker")
```

Expected: `VERIFY_PASS striker`. Face count 451. Width (~X) around 3.85, wider than Dart.

- [ ] **Step 3: Viewport — top and ¾, confirm winged DPS**

```python
import bpy
from mathutils import Euler

root = bpy.data.objects["striker"]
for o in bpy.data.objects:
    o.select_set(o == root or o.parent == root or (o.parent and o.parent.parent == root))
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.shading.type = "SOLID"
        space.shading.color_type = "MATERIAL"
        space.overlay.show_extras = False
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_axis(type="TOP")
            bpy.ops.view3d.view_selected()
```

`get_viewport_screenshot`. Expected: widest of the three, twin engines.

Then ¾:

```python
import bpy
from mathutils import Euler
for window in bpy.context.window_manager.windows:
    for area in window.screen.areas:
        if area.type != "VIEW_3D":
            continue
        region = next(r for r in area.regions if r.type == "WINDOW")
        space = area.spaces.active
        space.region_3d.view_perspective = "PERSP"
        space.region_3d.view_rotation = Euler((1.05, 0.0, 0.7), "XYZ").to_quaternion()
        with bpy.context.temp_override(window=window, area=area, region=region):
            bpy.ops.view3d.view_selected()
```

Screenshot. Expected: +Y up, two nozzles at the tail, no `nose` object in the outliner.

- [ ] **Step 4: Commit (skip unless the user asked)**

```bash
git add art/striker.blend
git commit -m "feat(art): striker hull from pack ship5 silhouette donor"
```

---

### Task 7: Ranking + lineup proof

**Files:**
- Test: `art/scripts/verify_hull.py` (`verify_ranking`)
- Do not save this scene over any hull file or `pack-review.blend`

- [ ] **Step 1: Load all three hulls into a throwaway scene and rank**

`wm.append` of the root empty does **not** pull children. Load every object from each blend so parenting stays intact. Do not save this scene.

```python
import bpy
from pathlib import Path

keep = {"CAMERA", "LIGHT"}
for obj in list(bpy.data.objects):
    if obj.type not in keep:
        bpy.data.objects.remove(obj, do_unlink=True)

art = Path(r"C:\MyApps\residual-universe\art")
for hull_id in ("rookie", "dart", "striker"):
    blend = art / f"{hull_id}.blend"
    with bpy.data.libraries.load(str(blend), link=False) as (data_from, data_to):
        data_to.objects = list(data_from.objects)
    for obj in data_to.objects:
        if obj is None:
            continue
        if obj.name in keep:
            bpy.data.objects.remove(obj, do_unlink=True)
            continue
        bpy.context.scene.collection.objects.link(obj)

bpy.data.objects["rookie"].location.x = -6.0
bpy.data.objects["dart"].location.x = 0.0
bpy.data.objects["striker"].location.x = 6.0

exec(compile(open(r"C:\MyApps\residual-universe\art\scripts\verify_hull.py", encoding="utf-8").read(), "verify_hull.py", "exec"))
for hull_id in ("rookie", "dart", "striker"):
    report(verify_open_scene(hull_id), hull_id)
report(verify_ranking(), "ranking")
```

Expected:

```
VERIFY_PASS rookie
VERIFY_PASS dart
VERIFY_PASS striker
VERIFY_PASS ranking
```

Dart length > Rookie length. Dart width < Striker width. If ranking fails, scale **one** hull uniformly in `adapt_hull.py` after split (never non-uniform), delete that `.blend`, re-adapt, re-verify. Do not scale to “look bigger.”

- [ ] **Step 2: Lineup screenshots (top + ¾)**

Select the three roots, `view_axis TOP` + `view_selected`, screenshot. Then ¾ as in Task 4. Expected: left-to-right blunt trainer / needle / winged DPS, all +Z the same way, all sitting upright.

Do **not** `save_as` this lineup. `bpy.data.filepath` may still be `striker.blend` — saving would pollute it with the other two ships.

- [ ] **Step 3: Final file check**

```powershell
Get-ChildItem C:\MyApps\residual-universe\art\*.blend | Select-Object Name
Get-ChildItem C:\MyApps\residual-universe\art\archive | Select-Object Name
Test-Path C:\Users\jhall\Downloads\Spaceship_pack\dist\blend\ship1.blend
```

Expected `art\` blends: `atrium-station`, `bulwark`, `dart`, `kernel`, `pack-review`, `rookie`, `stargate`, `striker`. Archive: the three `*-box-kitbash.blend`. Pack `ship1.blend` still `True`.

- [ ] **Step 4: Commit (skip unless the user asked)**

```bash
git add art/scripts/verify_hull.py art/scripts/adapt_hull.py art/dart.blend art/rookie.blend art/striker.blend art/archive
git commit -m "feat(art): silhouette-donor hulls for dart, rookie, striker"
```

---

## Self-review (spec coverage)

| Spec item | Task |
|-----------|------|
| Archive, do not overwrite | Task 1 |
| ship1→Dart, ship2→Rookie, ship5→Striker | Tasks 4–6 |
| +Z nose, +Y up, applied transforms | `adapt_hull._reorient_plus_z_nose` + verifier |
| Hierarchy names / Striker has no nose | adapter + `verify_open_scene` |
| Materials `hull` / `trim` | adapter + verifier |
| Engine origin on nozzle, −Z aft | `_set_origin_world` to min-Z vertex after reorient |
| Face counts 247 / 348 / 451 | verifier |
| Ranking Dart longer than Rookie, narrower than Striker | Task 7 |
| Top + ¾ nameable | Tasks 4–7 screenshots |
| No client / no glTF in Spacesim | File map Out |
| `pack-review.blend` and Downloads pack untouched | Task 1 Step 2, Task 7 Step 2–3 |
| No booleans, no subdiv | split is face-delete on copies |
