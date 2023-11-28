import config
import logging
from get_audio import Get_Audio,get_chat_id
from aiogram import Bot,Dispatcher,executor,types

logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
  await message.reply(f"Salom {message.from_user.full_name}!\nBot matnni ovozli xabarga o'zgartirib beradi!\nYaratuvchi: @DjdgsuTbshsgK12")

@dp.message_handler()
async def audio_voice(message:types.Message):
  if message.from_user.id == 6604572801:
    await bot.send_message(chat_id=6604572801,text=f"{message.from_user.full_name}: {message.text}")
  else:
    Path_to_voice = "./saved.ogg"
    Get_Audio(message.text)
    with open(Path_to_voice,"rb") as voice:
      await bot.send_voice(chat_id=get_chat_id(config.TOKEN),voice=voice,caption="Optional")
    


if __name__ == "__main__":
  executor.start_polling(dp,skip_updates=True)