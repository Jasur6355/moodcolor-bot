from PIL import Image, ImageDraw

def paint_scene(scene, colors):
    img = Image.open(scene["image"]).convert("RGB")
    draw = ImageDraw.Draw(img)

    parts = scene.get("parts", {})
    shapes = scene.get("shapes", {})

    for seg, rgb in colors.items():
        if seg not in parts:
            continue

        seg_type = shapes.get(seg, "rect")
        coords = parts[seg]

        if seg_type == "rect":
            draw.rectangle(coords, fill=rgb)

        elif seg_type == "ellipse":
            draw.ellipse(coords, fill=rgb)

        elif seg_type == "multi_rect":
            for c in coords:
                draw.rectangle(c, fill=rgb)

        elif seg_type == "multi_ellipse":
            for c in coords:
                draw.ellipse(c, fill=rgb)

        elif seg_type == "polygon":
            draw.polygon(coords, fill=rgb)

    painted = scene["image"].replace("scene_", "painted_")
    img.save(painted)
    return painted
