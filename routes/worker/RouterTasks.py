from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import as_list, as_line, as_key_value, Bold, as_numbered_section

from keyboards import BotKeyboard
from utils.WorkerCallbackData import WorkerCallbackData

from aiogram.utils.i18n import gettext as _

router = Router(name="worker_router_tasks")


@router.callback_query(lambda call: call.data == WorkerCallbackData.GET_TASK.value)
async def get_task(call: CallbackQuery):
    await call.message.edit_text(_("Подготавливаем для тебя задание..."))

    task_content = as_list(
        as_line(
            Bold(as_key_value(_("Задание №"), 563664))
        ),
        as_numbered_section(
            _("Выполните действия"),
            _("Подпишитесь на канал"),
            _("Нажмите кнопку \"Проверить\""),
        ),
        " ",
        as_line(
            as_key_value(_("Оплата"), "15 $NOT")
        ),
    )

    await call.message.edit_text(
        **task_content.as_kwargs(),
        reply_markup=BotKeyboard.workerTaskKeyboard()
    )


@router.callback_query(lambda call: call.data == WorkerCallbackData.CHECK_TASK.value)
async def check_task(call: CallbackQuery):
    check_task_content = as_list(
        as_line(_("Задание выполнено!")),
        as_line(_("{amount} $NOT зачисленны на ваш счет.".format(
            amount=15
        ))),
        as_line(
            as_key_value(_("Баланс"), "{amount} $NOT".format(
                amount=320
            ))
        )
    )

    await call.message.edit_text(**check_task_content.as_kwargs(),
                                 reply_markup=BotKeyboard.workerTaskDoneKeyboard())
