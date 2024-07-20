import asyncio
import logging
import sys

from aiogram.filters import CommandStart
from aiogram.types import Message

from config import bot, dp
from gpt import request_for_response

async def rate_limit(user_id):
    current_time = asyncio.get_event_loop().time()
    last_message_time = user_message_times[user_id]
    if current_time - last_message_time < TIME_LIMIT:
        return False
    user_message_times[user_id] = current_time
    return True

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start.
    """
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я уникальный AI ассистент LATOKEN. Я нужен для подбора участников на хакатон!\n"
        f"Задайте вопрос который хотите."
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    print('сообщение получено')
    try:
        await bot.send_chat_action(message.chat.id, action="typing")
        text = await request_for_response(f'{message.text} Имя запросившего:{message.from_user.full_name}')
        await message.reply(text)
    except TypeError:
        await message.answer("Nice try!")





async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
