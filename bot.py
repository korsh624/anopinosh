import logging
import time

from aiogram import Bot, Dispatcher, types, executor
import serial
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.INFO)
bot=Bot(token='6162590332:AAFhxYHT_MaRLcZBdvU1hXfELk9zsl2Kc9s')
dp=Dispatcher(bot)
try:
    arduino = serial.Serial('COM3',9600)
except:
    print('error connected')

keyboard=InlineKeyboardMarkup()
btn=InlineKeyboardButton(text='Text')
keyboard.add(btn)


def sendmessage(data:str):
    try:
        arduino.write(data.encode())
        time.sleep(5)
        return data
    except:
        return "Controller error"




@dp.message_handler(commands=['start'])
async def strart(message: types.Message):
    await message.answer('Привет, я бот из робоквантума,'
                         'я управляю умным домом.'
                         '\nНапиши /help что бы узнать команды')

@dp.message_handler(commands=['help'])
async def strart(message: types.Message):
    await message.answer('/setPin13on - включает тестовый пин'
                         '\n/setPin13off - выключает тестовый пин'
                         '\n/intLight - внутренее освещение'
                         '\n/ExtLight - внешнее освещение '
                         '\n/OpenDoor - открывание двери(ворот)'
                         '\n/OpenWindow - открывание окон'
                         '\n/backlight - режим автовключения подсветки'
                         '\n/autoLightMotion - режим автовключения света от движения'
                         '\n/TurnVent - включить вентеляцию '
                         '\n/AlarmSystem - сигнализация')

@dp.message_handler(commands='setPin13on')
async def testpinoff(message: types.Message):
    answer = sendmessage('setPin13on')
    await message.answer(answer)
    await message.answer('Вы включили тестоый пин')





@dp.message_handler(commands='intLight:0')
async def testpinoff(message: types.Message):
    await message.answer('Вы включили внешнее освещение')




if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)