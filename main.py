import logging
import time

from aiogram import Bot, Dispatcher, executor, types
import serial
from aiogram.dispatcher.filters import CommandStart
BOT_TOKEN='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
try:
    arduino = serial.Serial('COM24',9600)
except:
    print('error connected')
def sendmessage(data:str):
    count=0
    # while (count<1):
    try:
        arduino.write(data.encode())
        time.sleep(5)
        return data
    except:
        return "Controller error"

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    answer=sendmessage('starting')
    await message.answer(answer)


if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)