from aiogram import executor

from loader import dp
# import filters
import middlewares, handlers

from utils.notify_admins import on_startup_notify, on_shutdown_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


async def on_shutdown(disaptcher):
    await on_shutdown_notify(disaptcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
