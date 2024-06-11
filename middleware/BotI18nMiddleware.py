from typing import Dict, Any

from aiogram.types import TelegramObject, Update
from aiogram.utils.i18n import I18nMiddleware, I18n


class BotI18nMiddleware(I18nMiddleware):

    async def get_locale(self, event: Update, data: Dict[str, Any]) -> str:
        if 'ru' or 'ua' in event.message.from_user.language_code:
            return 'ru'
        return 'en'
