from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_list, Bold, as_key_value, as_line
from aiogram.utils.i18n import gettext as _

from keyboards import BotKeyboard
from utils.WorkerCallbackData import WorkerCallbackData

router = Router(name="worker_router_home")


@router.callback_query(lambda query: query.data == WorkerCallbackData.HOME.value)
async def home_callback(call: CallbackQuery):
    await call.message.delete()
    await hello_world(call.message)


@router.message(CommandStart())
async def hello_world(message: Message):
    content = as_list(
        as_line(
            Bold(_("Главное меню")),
            "\n\n",
            as_key_value(_("Баланс"), "100 $NOT (2 USD)\n"),
            as_key_value(_("Доступно заданий"), 36),
            "\n\n",
            Bold(
                _('Что бы начать зарабатывать, нажмите кнопку “Получить задание"')
            )
        ),
        sep="\n\n"
    )

    await message.answer(**content.as_kwargs(), reply_markup=BotKeyboard.workerHomeKeyboard())