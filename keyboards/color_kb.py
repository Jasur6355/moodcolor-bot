from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

COLOR_OPTIONS = {
    "🔴": (255, 0, 0),
    "🟢": (0, 255, 0),
    "🔵": (0, 0, 255),
    "🟡": (255, 255, 0),
    "🟠": (255, 140, 0),
    "🟣": (140, 0, 255)
}

def make_color_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[])

    for emoji in COLOR_OPTIONS.keys():
        kb.inline_keyboard.append([
            InlineKeyboardButton(text=emoji, callback_data=f"color_{emoji}")
        ])

    kb.inline_keyboard.append([
        InlineKeyboardButton(text="✅ Tugatish", callback_data="finish")
    ])

    return kb
