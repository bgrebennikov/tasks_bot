from aiogram import Router
from aiogram.types import CallbackQuery, User
from aiogram_tonconnect import ATCManager
from aiogram_tonconnect.tonconnect.models import ConnectWalletCallbacks, AccountWallet, AppWallet

from utils.WorkerCallbackData import WorkerCallbackData

router = Router(name="worker_router_wallet")


async def before_callback(event_from_user: User, atc_manager: ATCManager, **_) -> None:
    await atc_manager._send_message("Preparing...")


async def connected_callback(atc_manager: ATCManager, app_wallet: AppWallet,
                             account_wallet: AccountWallet, **_
                             ) -> None:
    await atc_manager._send_message(f"""
        CONNECTED!\n\n
        Name: ${app_wallet.name}\n
        Address: ${account_wallet.address}
    """)


@router.callback_query(lambda call: call.data == WorkerCallbackData.WALLET.value)
async def wallet(call: CallbackQuery, atc_manager: ATCManager) -> None:
    await atc_manager.update_interfaces_language("ru")

    callbacks = ConnectWalletCallbacks(
        before_callback=before_callback,
        after_callback=connected_callback
    )

    await atc_manager.connect_wallet(callbacks)

    await call.answer()
