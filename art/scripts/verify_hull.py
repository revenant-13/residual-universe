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
    "bulwark": ["body", "nose", "armorL", "armorR", "engine"],
    "sledge": ["body", "gunDeck", "wingL", "wingR", "engine"],
    "tender": ["body", "tankL", "tankR", "engine"],
    "bastion": ["body", "hangarL", "hangarR", "engine"],
    "light-combat-drone": ["body", "wingL", "wingR", "engine"],
    "medium-combat-drone": ["body", "wingL", "wingR", "engine"],
}
HULL_MAT_PARTS = {
    "rookie": ["body"],
    "dart": ["body"],
    "striker": ["body"],
    "bulwark": ["body", "nose"],
    "sledge": ["body", "wingL", "wingR"],
    "tender": ["body"],
    "bastion": ["body"],
    "light-combat-drone": ["body"],
    "medium-combat-drone": ["body"],
}
TRIM_MAT_PARTS = {
    "rookie": ["wingL", "wingR", "engine"],
    "dart": ["wingL", "wingR", "engine", "nose"],
    "striker": ["wingL", "wingR", "engineL", "engineR"],
    "bulwark": [],
    "sledge": [],
    "tender": [],
    "bastion": [],
    "light-combat-drone": ["wingL", "wingR"],
    "medium-combat-drone": ["wingL", "wingR"],
}
ARMOR_MAT_PARTS = {
    "rookie": ["nose"],
    "dart": [],
    "striker": [],
    "bulwark": ["armorL", "armorR", "engine"],
    "sledge": ["gunDeck", "engine"],
    "tender": ["tankL", "tankR", "engine"],
    "bastion": ["hangarL", "hangarR", "engine"],
    "light-combat-drone": ["engine"],
    "medium-combat-drone": ["engine"],
}
# Dart wing guns stripped (pack 247 minus turret islands).
PACK_FACES = {"rookie": 348, "dart": 110, "striker": 451, "bulwark": 445, "sledge": 640, "tender": 377, "bastion": 500, "light-combat-drone": 236, "medium-combat-drone": 288}
ENGINE_PARTS = {
    "rookie": ["engine"],
    "dart": ["engine"],
    "striker": ["engineL", "engineR"],
    "bulwark": ["engine"],
    "sledge": ["engine"],
    "tender": ["engine"],
    "bastion": ["engine"],
    "light-combat-drone": ["engine"],
    "medium-combat-drone": ["engine"],
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
    allowed = {"hull", "trim", "emissive", "armor"}
    extra = mats - allowed
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
    for part in ARMOR_MAT_PARTS[hull_id]:
        obj = names.get(part)
        if obj and _mat_name(obj) != "armor":
            errors.append(f"{part} material is {_mat_name(obj)!r}, want armor")
    present = [names[p] for p in PARTS[hull_id] if p in names and names[p].type == "MESH"]
    faces = sum(len(o.data.polygons) for o in present)
    expected = PACK_FACES[hull_id]
    if expected is not None and faces != expected:
        errors.append(f"face count {faces} != pack {expected}")
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
            emin, _emax = _mesh_bbox_world(eng)
            if origin.z > emin.z + 0.2:
                errors.append(
                    f"{part} origin z={origin.z:.3f} not on nozzle (engine min.z={emin.z:.3f})"
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
