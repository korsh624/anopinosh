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
                         '\n/intLighton - включает внутренее освещение'
                         '\n/intLightoff - выключает внутренее освещение'
                         '\n/ExtLighton - внешнее освещение '
                         '\n/ExtLightoff - внешнее освещение '
                         '\n/OpenDoor - открывание двери(ворот)'
                         '\n/CloseDoor - закрывание двери(ворот)'
                         '\n/CloseWindow - закрывание окон'
                         '\n/OpenWindow - открывание окон'
                         '\n/backlighton - режим автовключения подсветки вкл'
                         '\n/backlightoff - режим автовключения подсветки выкл'
                         '\n/autoLightMotionon - режим автовключения света от движения вкл'
                         '\n/autoLightMotionoff - режим автовключения света от движения выкл'
                         '\n/TurnVenton - включить вентеляцию '
                         '\n/TurnVenton - выключить вентеляцию '
                         '\n/AlarmSystemon - сигнализация вкл'
                         '\n/AlarmSystemoff - сигнализация выкл')


@dp.message_handler(commands='setPin13on')
async def testpinon(message: types.Message):
    answer = sendmessage('setPin13on')
    await message.answer(answer)
    await message.answer('Вы включили тестоый пин')

@dp.message_handler(commands='setPin13off')
async def testpinoff(message: types.Message):
    answer = sendmessage('setPin13off')
    await message.answer(answer)
    await message.answer('Вы выключили тестоый пин')



@dp.message_handler(commands=['ExtLighton'])
async def testpinoff(message: types.Message):
    answer = sendmessage('ExtLighton')
    await message.answer(answer)
    await message.answer('Вы включили внешнее освещение')

@dp.message_handler(commands=['ExtLightoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('ExtLightoff')
    await message.answer(answer)
    await message.answer('Вы выключили внешнее освещение')





if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)