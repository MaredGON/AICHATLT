import asyncio
import logging
import sys

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums.poll_type import PollType

from config import bot, dp, TRIGGER_WORDS
from gpt import request_for_response, request_for_response_quiz

async def cmd_quiz(message: Message, text):
    try:
        question, answers, nice_answer = await request_for_response_quiz(text)
        print(answers)
        nice_answer_id = int(nice_answer)
        await bot.send_poll(
            chat_id=message.chat.id,
            question=question,
            options=answers,
            type=PollType.QUIZ,
            correct_option_id=nice_answer
        )
    except:
        ...


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
    await bot.send_chat_action(message.chat.id, action="typing")
    try:
        text = await request_for_response(f'{message.text} Имя запросившего:{message.from_user.full_name}')
        await message.reply(text)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
