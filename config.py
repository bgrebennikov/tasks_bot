from aiogram import Dispatcher, Router
from aiogram.utils.i18n import I18n
from aiogram_tonconnect.handlers import AiogramTonConnectHandlers
from aiogram_tonconnect.middleware import AiogramTonConnectMiddleware
from aiogram_tonconnect.tonconnect.storage.base import ATCMemoryStorage
from aiogram_tonconnect.utils.qrcode import QRUrlProvider

from middleware.BotI18nMiddleware import BotI18nMiddleware
from middleware.JoinMiddleware import JoinMiddleware
from routes.worker import workerRouter

i18n = I18n(path="locales", default_locale="ru", domain="messages")

dp = Dispatcher()

dp.include_router(workerRouter)

dp.message.middleware(JoinMiddleware())
dp.update.outer_middleware(BotI18nMiddleware(i18n))
dp.update.middleware.register(
    AiogramTonConnectMiddleware(
        storage=ATCMemoryStorage(),
        manifest_url="https://raw.githubusercontent.com/nessshon/aiogram-tonconnect/main/tonconnect-manifest.json",
        exclude_wallets=[],
        qrcode_provider=QRUrlProvider()
    )
)
AiogramTonConnectHandlers().register(dp)