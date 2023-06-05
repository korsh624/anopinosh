import logging
import time
from aiogram import Bot, Dispatcher, types, executor
import serial
admins=[]
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.INFO)
bot=Bot(token='6162590332:AAFhxYHT_MaRLcZBdvU1hXfELk9zsl2Kc9s')
dp=Dispatcher(bot)
try:
    arduino = serial.Serial('COM4',9600)
except:
    print('error connected')

keyboard=InlineKeyboardMarkup()
btn=InlineKeyboardButton(text='Text')
keyboard.add(btn)


def sendmessage(data:str):
    try:
        arduino.write(data.encode())
        time.sleep(2)
        r=arduino.readline()
        return r.decode()

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
                         '\n/TurnVentoff - выключить вентеляцию '
                         '\n/AlarmSystemon - сигнализация вкл'
                         '\n/AlarmSystemoff - сигнализация выкл'
                         '\n/GetTemp - получить значение температуры ')


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



@dp.message_handler(commands=['intLighton'])
async def testpinoff(message: types.Message):
    answer = sendmessage('intLighton')
    await message.answer(answer)
    await message.answer('Вы включили внутренее освещение')

@dp.message_handler(commands=['intLightoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('intLightoff')
    await message.answer(answer)
    await message.answer('Вы выключили внутренее освещение')

@dp.message_handler(commands=['OpenDoor'])
async def testpinoff(message: types.Message):
    answer = sendmessage('OpenDoor')
    await message.answer(answer)
    await message.answer('Вы открыли дверь')

@dp.message_handler(commands=['CloseDoor'])
async def testpinoff(message: types.Message):
    answer = sendmessage('CloseDoor')
    await message.answer(answer)
    await message.answer('Вы закрыли дверь')


@dp.message_handler(commands=['CloseWindow'])
async def testpinoff(message: types.Message):
    answer = sendmessage('CloseWindow')
    await message.answer(answer)
    await message.answer('Вы закрыли окно ')

@dp.message_handler(commands=['OpenWindow'])
async def testpinoff(message: types.Message):
    answer = sendmessage('OpenWindow')
    await message.answer(answer)
    await message.answer('Вы открыли окно')


@dp.message_handler(commands=['backlighton'])
async def testpinoff(message: types.Message):
    answer = sendmessage('backlighton')
    await message.answer(answer)
    await message.answer('Вы включили режим автовключение подсветки ')


@dp.message_handler(commands=['backlightoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('backlightoff')
    await message.answer(answer)
    await message.answer('Вы выключили режим автовключения подсветки')

@dp.message_handler(commands=['autoLightMotionon'])
async def testpinoff(message: types.Message):
    answer = sendmessage('autoLightMotionon')
    await message.answer(answer)
    await message.answer('Вы включили режим автовключение света от движения ')

@dp.message_handler(commands=['autoLightMotionoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('autoLightMotionoff')
    await message.answer(answer)
    await message.answer('Вы выключили режим автовключения света от движения')

@dp.message_handler(commands=['TurnVenton'])
async def testpinoff(message: types.Message):
    answer = sendmessage('TurnVenton')
    await message.answer(answer)
    await message.answer('Вы открыли вентеляцию ')

@dp.message_handler(commands=['TurnVentoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('TurnVentoff')
    await message.answer(answer)
    await message.answer('Вы закрыли вентеляцию')

@dp.message_handler(commands=['AlarmSystemon'])
async def testpinoff(message: types.Message):
    answer = sendmessage('AlarmSystemon')
    await message.answer(answer)
    await message.answer('Вы включили сигнализацию ')

@dp.message_handler(commands=['AlarmSystemoff'])
async def testpinoff(message: types.Message):
    answer = sendmessage('AlarmSystemoff')
    await message.answer(answer)
    await message.answer('Вы выключили сигнализацию')


@dp.message_handler(commands=['GetTemp'])
async def testpinoff(message: types.Message):
    answer = sendmessage('GetTemp')
    await message.answer(answer)
    await message.answer('Вы получили значение температуры')

@dp.message_handler(text="password")
async def checkadmins(message: types.Message):
    if message.from_user.id not in admins:
        admins.append(message.from_user.id )
        await message.answer('Теперь вы администратор')



@dp.message_handler()
async def checkadmins(message: types.Message):
    if message.from_user.id not in admins:
        await message.answer('Введите пароль')


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)