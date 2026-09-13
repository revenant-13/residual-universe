"""Dump catalog blend hierarchies and export GLBs for Spacesim.

Run:
  blender --background --python art/scripts/export_glb.py
"""
from __future__ import annotations

import json
import traceback
from pathlib import Path

import bpy

ART_ROOT = Path(r"C:\MyApps\residual-universe\art")
EXPORT_DIR = ART_ROOT / "export"
SPACESIM_DIR = Path(r"C:\MyApps\spacesim\packages\client\public\models")

CATALOG = [
    "rookie",
    "dart",
    "striker",
    "bulwark",
    "sledge",
    "bastion",
    "tender",
    "kernel",
    "light-combat-drone",
    "medium-combat-drone",
    "atrium-station",
    "stargate",
]


def _bbox(obj) -> dict | None:
    if obj.type != "MESH" or not obj.data.vertices:
        return None
    inf = 1e9
    mn = [inf, inf, inf]
    mx = [-inf, -inf, -inf]
    for v in obj.data.vertices:
        w = obj.matrix_world @ v.co
        for i in range(3):
            mn[i] = min(mn[i], w[i])
            mx[i] = max(mx[i], w[i])
    return {"min": mn, "max": mx}


def dump_scene() -> dict:
    objects = []
    for obj in bpy.data.objects:
        objects.append(
            {
                "name": obj.name,
                "type": obj.type,
                "parent": obj.parent.name if obj.parent else None,
                "loc": [round(x, 4) for x in obj.location],
                "rot": [round(x, 4) for x in obj.rotation_euler],
                "scale": [round(x, 4) for x in obj.scale],
                "mats": [m.name for m in getattr(obj.data, "materials", []) if m],
                "faces": len(obj.data.polygons) if obj.type == "MESH" else 0,
                "bbox": _bbox(obj),
            }
        )
    mats = []
    for mat in bpy.data.materials:
        color = None
        if mat.use_nodes:
            bsdf = mat.node_tree.nodes.get("Principled BSDF")
            if bsdf and "Base Color" in bsdf.inputs:
                color = [round(c, 4) for c in bsdf.inputs["Base Color"].default_value]
        mats.append({"name": mat.name, "color": color})
    return {"objects": objects, "materials": mats}


def export_glb(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=str(path),
        export_format="GLB",
        use_selection=False,
        export_apply=True,
        export_yup=False,
        export_extras=False,
        export_cameras=False,
        export_lights=False,
        export_skins=False,
        export_animations=False,
        export_morph=False,
    )


def main() -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    SPACESIM_DIR.mkdir(parents=True, exist_ok=True)
    reports = []
    for name in CATALOG:
        blend = ART_ROOT / f"{name}.blend"
        rec = {"id": name, "blend": str(blend), "ok": False}
        try:
            if not blend.is_file():
                rec["error"] = "missing blend"
                reports.append(rec)
                continue
            bpy.ops.wm.open_mainfile(filepath=str(blend), load_ui=False)
            rec["scene"] = dump_scene()
            glb = EXPORT_DIR / f"{name}.glb"
            export_glb(glb)
            dest = SPACESIM_DIR / f"{name}.glb"
            dest.write_bytes(glb.read_bytes())
            rec["glb_bytes"] = glb.stat().st_size
            rec["ok"] = True
        except Exception as e:
            rec["error"] = f"{e}\n{traceback.format_exc()}"
        reports.append(rec)
        print(json.dumps({k: rec[k] for k in rec if k != "scene"}, indent=2), flush=True)

    out = EXPORT_DIR / "dump.json"
    out.write_text(json.dumps(reports, indent=2), encoding="utf-8")
    print(f"wrote {out}", flush=True)


if __name__ == "__main__":
    main()
