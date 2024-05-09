from aiogram import F , Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3
import re
import validators

from app.data_base import take_url, create_db, add_to_db, delete_arcticle
import app.keyboard as kb


router = Router()

start_text = ('Привет! Я бот, который поможет не забыть прочитать статьи, найденные тобой в интернете :))'
+'\n- Чтобы я запомнил статью, достаточно передать мне ссылку на нее. К примеру https://example.com'  
+'\n- Чтобы получить случайную статью, достаточно передать мне команду /get_article.'
+'\nНо помни! Отдавая статью тебе на прочтение, она больше не хранится в моей базе. Так что тебе точно нужно ее изучить!!!')

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(start_text, reply_markup=kb.main)
    create_db()


@router.message(Command('get_article'))
async def cmd_save_meny(message: Message):
    url = take_url()
    if url!= False:
        await message.answer('Вы хотели прочитать:'+ str(url) + '\n Самое время это сделать!!!!', reply_markup=kb.main) 
        delete_arcticle(str(url))
    else:
        await message.answer('Вы пока не сохранили ни одной статьи :CC Если нашли что-то стоящее, я жду!', reply_markup=kb.main) 
    
    
@router.message()
async def save_article(message: Message):
    article_url = message.text
    if validators.url(article_url) == True:
        status = add_to_db(article_url)
        if status == True:
            await message.answer('Упссссс, вы уже это сохраняли XD  ', reply_markup=kb.main) 
        else:
            await message.answer('Сохранил, спасибо!!!', reply_markup=kb.main) 
    else:
        await message.answer('Что-то не похоже на ссылку! Введите корректно!!!', reply_markup=kb.main) 
        
    
