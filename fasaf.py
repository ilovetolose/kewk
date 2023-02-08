import asyncio
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6123767585:AAFct5eGVw2vZC_iJ_FhoQ17yObdw-nJbTI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("привет\nя всеволод бот)\nотправь мне любое сообщение, и может быть я отвечу")


@dp.message_handler(regexp='(^почему в фильме про пикачу нет команды р, они что расстрелялись?)')
async def cats(message: types.Message):
    with open('gun.jpg', 'rb') as photo:

        await message.reply_photo(photo, caption='да.')

@dp.message_handler(regexp=('ты знаешь формулу атмосферного давления?'))
async def formula(message: types.Message):
    await message.reply("мой айкью выше твоего")

@dp.message_handler(regexp=('кто самый сильный покемон?'))
async def poke(message: types.Message):
    with open('1place.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='это самый сильный аркеус')
    await asyncio.sleep(2)

    await types.ChatActions.upload_photo()

    media = types.MediaGroup()

    media.attach_photo(types.InputFile('2place.jpg'), 'а это второй по силе meowto^_^')


    await message.reply_media_group(media=media)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)