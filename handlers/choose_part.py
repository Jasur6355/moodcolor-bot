from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

router = Router()

# Emoji nomlar
NOMLAR = {
    "quyosh": "☀️ Quyosh",
    "bulut": "☁️ Bulut",
    "daraxt1_tanasi": "🌳 Daraxt 1 tanasi",
    "daraxt1_barglari": "🍃 Daraxt 1 barglari",
    "daraxt2_tanasi": "🌳 Daraxt 2 tanasi",
    "daraxt2_barglari": "🍃 Daraxt 2 barglari",
    "tepalik": "⛰ Tepalik",
    "gul": "🌼 Gul",
    "zamin": "🟫 Zamin"
}

async def ask_parts(context, state: FSMContext):
    data = await state.get_data()
    scene = data.get("selected_scene")
    colors = data.get("colors", {})

    # bo‘yalganlarni olib tashlaymiz
    all_parts = scene.get("segments", [])
    remaining = [p for p in all_parts if p not in colors]

    kb = InlineKeyboardMarkup(inline_keyboard=[])

    for p in remaining:
        kb.inline_keyboard.append([
            InlineKeyboardButton(
                text=NOMLAR.get(p, p),
                callback_data=f"part_{p}"
            )
        ])

    # Agar hech narsa qolmasa — faqat tugatish tugmasi
    kb.inline_keyboard.append([
        InlineKeyboardButton(text="✅ Tugatish", callback_data="finish")
    ])

    await (context.reply if isinstance(context, types.Message) else context.message.answer)(
        "Bo‘yamoqchi bo‘lgan qismni tanlang:",
        reply_markup=kb
    )


@router.callback_query(F.data.startswith("part_"))
async def on_pick_part(callback: types.CallbackQuery, state: FSMContext):
    part = callback.data.replace("part_", "")
    await state.update_data(current_part=part)

    from keyboards.color_kb import make_color_kb
    kb = make_color_kb()

    await callback.message.answer(
        f"<b>{NOMLAR.get(part, part)}</b> uchun rangni tanlang:",
        reply_markup=kb
    )
    await callback.answer()
