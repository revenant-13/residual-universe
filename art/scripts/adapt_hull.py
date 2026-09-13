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
    "light-combat-drone": {
        "glb": "ship8.glb",
        "out": ART_ROOT / "light-combat-drone.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.15 and abs(c.x) < 0.20),
            ("wingL", lambda c: c.x < -0.18),
            ("wingR", lambda c: c.x > 0.18),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("wingL", "wingR", "engine"),
        "engines": ("engine",),
    },
    "medium-combat-drone": {
        "glb": "ship9.glb",
        "out": ART_ROOT / "medium-combat-drone.blend",
        "rules": [
            # Donor y min is -0.341; y < -0.4 left engine empty.
            ("engine", lambda c: c.y < -0.20 and abs(c.x) < 0.25),
            ("wingL", lambda c: c.x < -0.40),
            ("wingR", lambda c: c.x > 0.40),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("wingL", "wingR", "engine"),
        "engines": ("engine",),
    },
    "bastion": {
        "glb": "ship7.glb",
        "out": ART_ROOT / "bastion.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.7 and abs(c.x) < 0.55),
            ("hangarL", lambda c: c.x < -0.55),
            ("hangarR", lambda c: c.x > 0.55),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("hangarL", "hangarR", "engine"),
        "engines": ("engine",),
    },
    "tender": {
        "glb": "ship3.glb",
        "out": ART_ROOT / "tender.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.25 and abs(c.x) < 0.50),
            ("tankL", lambda c: c.x < -0.55),
            ("tankR", lambda c: c.x > 0.55),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("tankL", "tankR", "engine"),
        "engines": ("engine",),
    },
    "sledge": {
        "glb": "ship6.glb",
        "out": ART_ROOT / "sledge.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.7 and abs(c.x) < 0.5),
            ("gunDeck", lambda c: c.z > 0.04 and abs(c.x) < 0.5 and c.y > -0.2),
            ("wingL", lambda c: c.x < -0.6),
            ("wingR", lambda c: c.x > 0.6),
        ],
        "hull_parts": ("body",),
        "trim_parts": ("wingL", "wingR", "engine", "gunDeck"),
        "engines": ("engine",),
    },
    "bulwark": {
        "glb": "ship4.glb",
        "out": ART_ROOT / "bulwark.blend",
        "rules": [
            ("engine", lambda c: c.y < -0.5 and abs(c.x) < 0.70),
            ("nose", lambda c: c.y > 0.70 and abs(c.x) < 0.60),
            ("armorL", lambda c: c.x < -0.70),
            ("armorR", lambda c: c.x > 0.70),
        ],
        "hull_parts": ("body", "nose"),
        "trim_parts": ("armorL", "armorR", "engine"),
        "engines": ("engine",),
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


def _ensure_tail_negative_y(obj) -> None:
    """Some pack GLBs bake a Y-up flip so the tail sits at +Y after apply. Dart/rookie
    keep tail at -Y. Rotate 180° around Z when the origin is at the nose."""
    ys = [v.co.y for v in obj.data.vertices]
    if min(ys) > -0.3 and max(ys) > 1.5:
        obj.rotation_mode = "XYZ"
        obj.rotation_euler = (0.0, 0.0, math.pi)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


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


def _purge_leftovers() -> None:
    """Drop imported GLB meshes/materials so only hull and trim remain."""
    for mesh in list(bpy.data.meshes):
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for mat in list(bpy.data.materials):
        if mat.name not in {"hull", "trim"}:
            bpy.data.materials.remove(mat, do_unlink=True)
    bpy.data.orphans_purge(do_recursive=True)


def _ensure_nose_plus_z(root) -> None:
    """If the body is fatter at +Z than at -Z, the nose is pointing aft. Flip 180° around Y."""
    body = None
    for obj in root.children_recursive:
        if obj.name == "body" and obj.type == "MESH":
            body = obj
            break
    if body is None:
        return

    def end_width(z_positive: bool) -> float:
        xs = []
        for v in body.data.vertices:
            w = body.matrix_world @ v.co
            if (w.z > 0.0) == z_positive:
                xs.append(abs(w.x))
        return (sum(xs) / len(xs)) if xs else 0.0

    if end_width(True) <= end_width(False) + 0.02:
        return
    rot = Matrix.Rotation(math.pi, 4, "Y")
    for obj in root.children_recursive:
        if obj.type == "MESH":
            obj.matrix_world = rot @ obj.matrix_world


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
    _ensure_tail_negative_y(donor)
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
    _ensure_nose_plus_z(root)
    for name in spec["engines"]:
        eng = bpy.data.objects[name]
        _set_origin_world(eng, _aft_vertex_world(eng))
    _purge_leftovers()
    bpy.ops.wm.save_as_mainfile(filepath=str(spec["out"]))
    print("ADAPT_SAVED", spec["out"], "parts", sorted(parts))
