from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from api.ApiClient import ApiClient
from api.data.responseDto.UserDto import UserDto
from aiogram.utils.i18n import gettext as _
from keyboards.BotKeyboard import welcomeKeyboard


class JoinMiddleware(BaseMiddleware):
    client = ApiClient()

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: Update,
                       data: Dict[str, Any]) -> Any:
        user = UserDto(
            user_id=event.chat.id,
            first_name=event.chat.first_name,
            last_name=event.chat.last_name,
            username=event.chat.username
        )

        upsert = self.client.initProfile(user)

        if not upsert:
            return await event.bot.send_message(
                chat_id=event.chat.id,
                text=_("""Привет друг!
Не упусти возможность заработать криптовалюту выполняя простые задания.

Drops - Это проект созданный для заработка и продвижения в Телеграм

Вы можете приобрести рекламу и продвижение своего канала, или заработать на несложных заданиях в качестве исполнителя.""")
            ,
                reply_markup=welcomeKeyboard()
            )

        return await handler(event, data)
