import asyncio
from os import getenv

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import MenuButtonWebApp, WebAppInfo

from config import dp

TOKEN = getenv("TOKEN")


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ))
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="WebApp", web_app=WebAppInfo(
                url="https://browser-info.ru/"
            )
        )
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
