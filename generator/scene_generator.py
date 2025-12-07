# scene_generator.py

import os
import uuid
import random
from PIL import Image, ImageDraw
from config import TEMP_DIR

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR, exist_ok=True)


# ================================
#  UTILITY FUNKSIYA
# ================================
def _new_image():
    """600×600 oq fonli image yaratadi."""
    W, H = 600, 600
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    return img, draw



# ===========================================================
#  SCENE 1 — FOREST (sizning hozirgi sahna)
# ===========================================================
def scene_forest():
    uid = str(uuid.uuid4())[:8]
    img_path = os.path.join(TEMP_DIR, f"scene_{uid}.png")

    img, draw = _new_image()
    W, H = 600, 600

    parts = {
        "quyosh": (430, 40, 530, 140),

        "bulut": [
            (150, 90, 230, 150),
            (200, 70, 320, 140),
            (260, 90, 360, 150),
        ],

        # Trees (merged segments)
        "tanasi": [
            (80, 350, 130, 520),
            (450, 360, 500, 520),
        ],

        "barglar": [
            (40, 250, 170, 360),
            (410, 260, 540, 370),
        ],

        "tepalik": (0, 400, 600, 580),
        "gul": [
            (270, 500, 330, 560),
            (260, 490, 290, 520),
            (310, 490, 340, 520),
            (260, 530, 290, 560),
            (310, 530, 340, 560),
        ],

        "zamin": (0, 520, W, H)
    }

    shapes = {
        "quyosh": "ellipse",
        "bulut": "multi_ellipse",
        "tanasi": "multi_rect",
        "barglar": "multi_ellipse",
        "tepalik": "ellipse",
        "gul": "multi_ellipse",
        "zamin": "rect",
    }

    # --- DRAWING ---
    import math

    # Sun
    draw.ellipse(parts["quyosh"], outline="black", width=5)
    cx = (430 + 530) // 2
    cy = (40 + 140) // 2
    for i in range(10):
        a = (math.pi * 2 / 10) * i
        draw.line(
            (cx + 45 * math.cos(a), cy + 45 * math.sin(a),
             cx + 80 * math.cos(a), cy + 80 * math.sin(a)),
            fill="black", width=4
        )

    # Clouds
    for c in parts["bulut"]:
        draw.ellipse(c, outline="black", width=5)

    # Tree trunks
    for c in parts["tanasi"]:
        draw.rectangle(c, outline="black", width=5)

    # Leaves
    for c in parts["barglar"]:
        draw.ellipse(c, outline="black", width=5)

    # Hill
    draw.ellipse(parts["tepalik"], outline="black", width=5)

    # Flowers
    for c in parts["gul"]:
        draw.ellipse(c, outline="black", width=4)

    # Ground
    draw.rectangle(parts["zamin"], outline="black", width=5)

    img.save(img_path)

    return {
        "id": uid,
        "image": img_path,
        "segments": list(shapes.keys()),
        "parts": parts,
        "shapes": shapes
    }



# ===========================================================
#  SCENE 2 — MEADOW (keng dalalar, daraxt, gulzor)
# ===========================================================
def scene_meadow():
    uid = str(uuid.uuid4())[:8]
    img_path = os.path.join(TEMP_DIR, f"scene_{uid}.png")

    img, draw = _new_image()

    parts = {
        "quyosh": (50, 40, 160, 150),

        "bulut": [
            (300, 80, 380, 130),
            (340, 60, 450, 120),
            (380, 90, 480, 140),
        ],

        "tanasi": [
            (280, 300, 330, 520),
        ],

        "barglar": [
            (220, 180, 380, 320),
        ],

        "tepalik": (0, 380, 600, 580),

        "gul": [
            (100, 500, 140, 540),
            (140, 520, 180, 560),
            (60, 530, 100, 570),
        ],

        "zamin": (0, 520, 600, 600)
    }

    shapes = {
        "quyosh": "ellipse",
        "bulut": "multi_ellipse",
        "tanasi": "multi_rect",
        "barglar": "multi_ellipse",
        "tepalik": "ellipse",
        "gul": "multi_ellipse",
        "zamin": "rect",
    }

    # DRAW
    # Sun
    draw.ellipse(parts["quyosh"], outline="black", width=5)

    # Clouds
    for c in parts["bulut"]:
        draw.ellipse(c, outline="black", width=5)

    # Tree trunk
    for c in parts["tanasi"]:
        draw.rectangle(c, outline="black", width=5)

    # Tree leaves
    for c in parts["barglar"]:
        draw.ellipse(c, outline="black", width=5)

    # Hill
    draw.ellipse(parts["tepalik"], outline="black", width=5)

    # Flowers
    for c in parts["gul"]:
        draw.ellipse(c, outline="black", width=4)

    # Ground
    draw.rectangle(parts["zamin"], outline="black", width=5)

    img.save(img_path)

    return {
        "id": uid,
        "image": img_path,
        "segments": list(shapes.keys()),
        "parts": parts,
        "shapes": shapes
    }



# ===========================================================
#  SCENE 3 — HILLS (3–4 ta katta tepalik + bulutlar)
# ===========================================================
def scene_hills():
    uid = str(uuid.uuid4())[:8]
    img_path = os.path.join(TEMP_DIR, f"scene_{uid}.png")

    img, draw = _new_image()

    parts = {
        "quyosh": (250, 40, 350, 140),

        "bulut": [
            (100, 80, 200, 140),
            (150, 60, 250, 120),
            (180, 90, 280, 150),
        ],

        "tepalik": [
            (0, 350, 400, 650),
            (200, 380, 600, 680),
            (100, 420, 500, 700),
        ],

        "gul": [
            (500, 500, 550, 550)
        ],

        "tanasi": [],
        "barglar": [],
        "zamin": (0, 520, 600, 600)
    }

    shapes = {
        "quyosh": "ellipse",
        "bulut": "multi_ellipse",
        "tepalik": "multi_ellipse",
        "gul": "multi_ellipse",
        "tanasi": "multi_rect",
        "barglar": "multi_ellipse",
        "zamin": "rect",
    }

    # DRAW
    draw.ellipse(parts["quyosh"], outline="black", width=5)
    for c in parts["bulut"]:
        draw.ellipse(c, outline="black", width=5)
    for c in parts["tepalik"]:
        draw.ellipse(c, outline="black", width=5)
    for c in parts["gul"]:
        draw.ellipse(c, outline="black", width=5)
    draw.rectangle(parts["zamin"], outline="black", width=5)

    img.save(img_path)

    return {
        "id": uid,
        "image": img_path,
        "segments": list(shapes.keys()),
        "parts": parts,
        "shapes": shapes
    }



# ===========================================================
#  SCENE 4 — LAKE (ko‘l bo‘yi + quyosh + bulut)
# ===========================================================
def scene_lake():
    uid = str(uuid.uuid4())[:8]
    img_path = os.path.join(TEMP_DIR, f"scene_{uid}.png")

    img, draw = _new_image()

    parts = {
        "quyosh": (450, 60, 550, 160),

        "bulut": [
            (100, 120, 200, 170),
            (150, 100, 260, 160),
        ],

        "tepalik": (0, 300, 600, 520),

        "gul": [
            (70, 500, 110, 540),
            (120, 530, 160, 570)
        ],

        "zamin": (0, 520, 600, 600)
    }

    shapes = {
        "quyosh": "ellipse",
        "bulut": "multi_ellipse",
        "tepalik": "ellipse",
        "gul": "multi_ellipse",
        "tanasi": "multi_rect",
        "barglar": "multi_ellipse",
        "zamin": "rect",
    }

    draw.ellipse(parts["quyosh"], outline="black", width=5)
    for c in parts["bulut"]:
        draw.ellipse(c, outline="black", width=5)
    draw.ellipse(parts["tepalik"], outline="black", width=5)
    for c in parts["gul"]:
        draw.ellipse(c, outline="black", width=5)
    draw.rectangle(parts["zamin"], outline="black", width=5)

    img.save(img_path)

    return {
        "id": uid,
        "image": img_path,
        "segments": list(shapes.keys()),
        "parts": parts,
        "shapes": shapes
    }



# ===========================================================
#  RANDOM SCENE SELECTOR
# ===========================================================
def generate_scene():
    scenes = [scene_forest, scene_meadow, scene_hills, scene_lake]
    return random.choice(scenes)()


#scene_generator.py

# import os
# import uuid
# from PIL import Image, ImageDraw
# from config import TEMP_DIR

# if not os.path.exists(TEMP_DIR):
#     os.makedirs(TEMP_DIR, exist_ok=True)

# def generate_scene():
#     uid = str(uuid.uuid4())[:8]
#     img_path = os.path.join(TEMP_DIR, f"scene_{uid}.png")

#     W, H = 600, 600
#     img = Image.new("RGB", (W, H), "white")
#     draw = ImageDraw.Draw(img)

#     # ==============================
#     #       O‘RMON CHEGARASI
#     # ==============================
#     parts = {
#         "quyosh": (430, 40, 530, 140),
#         "bulut": [
#             (150, 90, 230, 150),
#             (200, 70, 320, 140),
#             (260, 90, 360, 150),
#         ],
#         # 2 daraxt uchun umumiy segmentlar
#         "tanasi": [
#             (80, 350, 130, 520),    # tree 1
#             (450, 360, 500, 520),   # tree 2
#         ],
#         "barglar": [
#             (40, 250, 170, 360),    # tree 1
#             (410, 260, 540, 370),   # tree 2
#         ],
#         "tepalik": (0, 400, 600, 580),
#         "gul_markaz": (270, 500, 330, 560),
#         "gul_barglari": [
#             (260, 490, 290, 520),
#             (310, 490, 340, 520),
#             (260, 530, 290, 560),
#             (310, 530, 340, 560),
#         ],
#         "zamin": (0, 520, W, H)
#     }

#     # Shakl turlari
#     shapes = {
#         "quyosh": "ellipse",
#         "bulut": "multi_ellipse",
#         "tanasi": "multi_rect",
#         "barglar": "multi_ellipse",
#         "tepalik": "ellipse",
#         "gul_markaz": "ellipse",
#         "gul_barglari": "multi_ellipse",
#         "zamin": "rect",
#     }

#     # ==============================
#     #           CHIZISH
#     # ==============================

#     # Quyosh + nurlar
#     draw.ellipse(parts["quyosh"], outline="black", width=5)
#     import math
#     cx = (430 + 530) // 2
#     cy = (40 + 140) // 2
#     for i in range(10):
#         angle = (math.pi * 2 / 10) * i
#         x1 = cx + 45 * math.cos(angle)
#         y1 = cy + 45 * math.sin(angle)
#         x2 = cx + 80 * math.cos(angle)
#         y2 = cy + 80 * math.sin(angle)
#         draw.line((x1, y1, x2, y2), fill="black", width=4)

#     # Bulut
#     for c in parts["bulut"]:
#         draw.ellipse(c, outline="black", width=5)

#     # 2 daraxt — tanasi
#     for c in parts["tanasi"]:
#         draw.rectangle(c, outline="black", width=5)

#     # 2 daraxt — barglar
#     for c in parts["barglar"]:
#         draw.ellipse(c, outline="black", width=5)

#     # Tepalik
#     draw.ellipse(parts["tepalik"], outline="black", width=5)

#     # Gul markazi
#     draw.ellipse(parts["gul_markaz"], outline="black", width=4)

#     # Gul barglari
#     for c in parts["gul_barglari"]:
#         draw.ellipse(c, outline="black", width=4)

#     # Zamin
#     draw.rectangle(parts["zamin"], outline="black", width=5)

#     img.save(img_path)

#     # Segmentlar (bo‘yash nomlari)
#     segments = [
#         "quyosh",
#         "bulut",
#         "tanasi",
#         "barglar",
#         "tepalik",
#         "gul_markaz",
#         "gul_barglari",
#         "zamin"
#     ]

#     return {
#         "id": uid,
#         "image": img_path,
#         "segments": segments,
#         "parts": parts,
#         "shapes": shapes
#     }
