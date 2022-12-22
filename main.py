import logging
from aiogram import Dispatcher, types, Bot, executor
from bot import TOKKEN
import wikipedia
wikipedia.set_lang('uz')


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKKEN)
md = Dispatcher(bot)


@md.message_handler(commands=["start"])
async def boshlash(message: types.Message):
    odi = message.from_user.first_name
    await message.answer(f"Assallom alaykum {odi} men sizga maqolalar topib berish uchun yaratilganman")


@md.message_handler()
async def maqola(message: types.Message):
    try:
        keldi = wikipedia.summary(message.text)
        await message.reply(keldi)
    except:
        await message.reply(f"siz yuborgan ''  {message.text} '' buyuruqa mos maqola topilmadi")

if __name__ == '__main__':
    executor.start_polling(md, skip_updates=True)