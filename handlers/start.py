from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from generator.scene_generator import generate_scene
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text.in_({"/start", "start"}))
async def start(message: types.Message, state: FSMContext):
    await state.clear()

    scene = generate_scene()

    await state.update_data(
        selected_scene=scene,
        colors={}
    )

    await message.answer_photo(
        photo=FSInputFile(scene["image"]),
        caption="Salom! Bu rasmni bo'yashni boshlaymiz!\nQaysi qismni tanlaysiz?"
    )

    from handlers.choose_part import ask_parts
    await ask_parts(message, state)
