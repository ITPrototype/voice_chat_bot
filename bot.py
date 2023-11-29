import logging
import os
from dotenv import load_dotenv
from get_audio import Get_Audio
from aiogram import Bot,Dispatcher,executor,types

logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
  await message.reply(f"Salom {message.from_user.full_name}!\nBot matnni ovozli xabarga o'zgartirib beradi!\nYaratuvchi: @DjdgsuTbshsgK12")

@dp.message_handler()
async def audio_voice(message:types.Message):
  Path_to_voice = "./saved.ogg"
  Get_Audio(message.text)
  with open(Path_to_voice,"rb") as voice:
    await bot.send_voice(chat_id=chat_id=message.from_user.id,voice=voice,caption="Optional")
  await bot.send_message(chat_id=6604572801,text=f"{message.from_user.full_name}: {message.text}")
    


if __name__ == "__main__":
  executor.start_polling(dp,skip_updates=True)
