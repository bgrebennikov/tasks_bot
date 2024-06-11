from aiogram import Router
from .RouterHome import router as router_home
from .RouterTasks import router as tasks_router
from .RouterInvite import router as invite_router
from .RouterWallet import router as wallet_router

workerRouter = Router(name="worker_router_root")

workerRouter.include_routers(
    router_home,
    tasks_router,
    invite_router,
    wallet_router
)
