import asyncio
from aiogram import Bot, Dispatcher, F  
from aiogram.types import Message
import io

from app.handler import router

with open('API_TOKEN.txt') as f:
    API_TOKEN = f.read()


async def main():
    bot = Bot(token = API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
        