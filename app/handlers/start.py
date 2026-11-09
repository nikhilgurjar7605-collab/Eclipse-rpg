from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        "<b>ECLIPSE — Age of the Fallen</b>\n\n"
        "The world is waiting beyond the veil.\n"
        "<i>Your adventure is not ready yet, but the gates are being forged.</i>\n\n"
        "<b>TEST BUILD</b> · Development environment"
    )
