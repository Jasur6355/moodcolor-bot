import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Render will read this

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

