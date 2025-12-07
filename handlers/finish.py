from aiogram import Router
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from painter.painter import paint_scene
from utils.mood import detect_mood_advanced   # YANGI FUNKSIYA

router = Router()

async def finish(callback, state: FSMContext):
    data = await state.get_data()
    scene = data.get("selected_scene")
    colors = data.get("colors", {})

    # Yakuniy rasmni bo'yash
    painted = paint_scene(scene, colors)

    # CHUQUR PSIXOLOGIK TAHLIL
    mood_text = detect_mood_advanced(colors)

    await callback.message.answer_photo(
        photo=FSInputFile(painted),
        caption=f"🎉 <b>Rasm tayyor!</b>\n\n{mood_text}"
    )

    await state.clear()
