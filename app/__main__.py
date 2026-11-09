import asyncio
import logging
import sys

from aiogram.exceptions import TelegramAPIError
from aiogram.types import BotCommand
from supabase import create_client

from app.bot import create_bot, create_dispatcher
from app.config import get_settings
from app.handlers.start import router as start_router


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    logger = logging.getLogger("eclipse")

    settings = get_settings()
    # Validate that the configured Supabase credentials can create a client.
    # Database calls will be added with the player repository layer.
    supabase = create_client(
        settings.supabase_url,
        settings.supabase_service_role_key.get_secret_value(),
    )
    del supabase

    bot = create_bot(settings)
    dispatcher = create_dispatcher()
    dispatcher.include_router(start_router)

    try:
        me = await bot.get_me()
        await bot.set_my_commands([BotCommand(command="start", description="Begin your journey")])
        logger.info("Starting ECLIPSE %s as @%s", settings.app_env, me.username)
        await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())
    except TelegramAPIError:
        logger.exception("Telegram API error while starting or polling")
        raise
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
