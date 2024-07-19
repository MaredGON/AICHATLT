import asyncio
import logging
import sys

from aiogram.filters import CommandStart
from aiogram.types import Message

from config import START_PROMT, bot, dp
from gpt import request_for_response


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
    """
    Обработчик всех остальных сообщений.
    """
    try:
        await bot.send_chat_action(message.chat.id, action="typing")
        text = await request_for_response(message.text)
        await message.answer(text)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    text = await request_for_response(START_PROMT)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
