from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from keyboards.color_kb import COLOR_OPTIONS
from painter.painter import paint_scene

router = Router()

@router.callback_query(F.data.startswith("color_"))
async def on_pick_color(callback: CallbackQuery, state: FSMContext):
    emoji = callback.data.replace("color_", "")
    rgb = COLOR_OPTIONS.get(emoji)

    if not rgb:
        return await callback.answer("Noto‘g‘ri rang tanlandi.")

    data = await state.get_data()
    part = data.get("current_part")
    scene = data.get("selected_scene")
    colors = data.get("colors", {})

    if not part:
        return await callback.answer("Avval qism tanlang.")

    colors[part] = rgb
    await state.update_data(colors=colors)

    # Rasmni yangidan bo‘yash
    painted = paint_scene(scene, colors)

    await callback.message.answer_photo(
        photo=FSInputFile(painted),
        caption=f"{part} bo‘yaldi {emoji}"
    )

    # Yana qism tanlash
    from handlers.choose_part import ask_parts
    await ask_parts(callback, state)

    await callback.answer()

@router.callback_query(F.data == "finish")
async def on_finish(callback: CallbackQuery, state: FSMContext):
    from handlers.finish import finish
    await finish(callback, state)
    await callback.answer()
