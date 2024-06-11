from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from utils.WelcomeCallbackData import WelcomeCallbackData
from utils.WorkerCallbackData import WorkerCallbackData


def welcomeKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_("Я рекламодатель"),
        callback_data=WelcomeCallbackData.ADVERTISER
    )
    builder.button(
        text=_("Я исполнитель"),
        callback_data=WelcomeCallbackData.WORKER
    )

    return builder.as_markup()


def workerHomeKeyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text=_("Получить задание"),
        callback_data=WorkerCallbackData.GET_TASK.value
    )
    builder.button(
        text=_("Пригласить друга"),
        callback_data=WorkerCallbackData.INVITE.value
    )
    builder.button(
        text=_("Баланс"),
        callback_data=WorkerCallbackData.WALLET.value
    )
    builder.button(
        text=_("Поддержка"),
        callback_data=WorkerCallbackData.SUPPORT.value
    )
    builder.adjust(1)

    return builder.as_markup()


def workerTaskKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_("Подписаться"),
        url="https://google.com",
    )
    builder.button(
        text=_("Проверить"),
        callback_data=WorkerCallbackData.CHECK_TASK.value
    )
    builder.button(
        text=_("Вернуться назад"),
        callback_data=WorkerCallbackData.HOME.value
    )
    builder.adjust(1)

    return builder.as_markup()


def workerTaskDoneKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_("следующее задание"),
        callback_data=WorkerCallbackData.GET_TASK.value
    )
    builder.button(
        text=_("Главное меню"),
        callback_data=WorkerCallbackData.HOME.value
    )

    builder.adjust(1)

    return builder.as_markup()


def workerInviteKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_("Вернуться назад"),
        callback_data=WorkerCallbackData.HOME.value
    )

    return builder.as_markup()
