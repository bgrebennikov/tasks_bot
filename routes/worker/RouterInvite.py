from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import as_list, as_marked_section, as_line, Bold, Code, as_section, as_key_value
from aiogram.utils.i18n import gettext as _

from keyboards.BotKeyboard import workerInviteKeyboard
from utils.WorkerCallbackData import WorkerCallbackData

router = Router(name="worker_router_invite")


@router.callback_query(lambda query: query.data == WorkerCallbackData.INVITE.value)
async def invite_callback(call: CallbackQuery):
    invite_content = as_list(
        as_line(
            as_marked_section(
                as_line(
                    _("Пригласите друзей по специальной ссылке, и получите бонусы:")
                ),

                _("{amount} $NOT за каждого друга".format(amount=50)),
                _("{percents}% с их заработка".format(percents=25)),

                marker='• '

            )
        ),
        as_line(
            as_section(
                _("Ваша статистика:"),
                as_list(
                    as_key_value("Приглашено друзей", 12),
                    as_key_value("Вы заработали", "{amount} $NOT".format(amount=557))
                )
            )
        ),
        as_line(
            Bold(_("Ваша ссылка для приглашения:")),
            Code(
                "https://t.me/dropscryptobot?start=35135135"
            )
        )

    )

    await call.message.edit_text(**invite_content.as_kwargs(),
                                 reply_markup=workerInviteKeyboard()
                                 )
