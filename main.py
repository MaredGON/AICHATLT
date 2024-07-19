import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from openai import AsyncOpenAI

TOKEN = "6440161421:AAEiJX0-Q75h0mv4tBT5dJ0gfD_jXraRUQY"
GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"
latoken_info = 'https://coda.io/@latoken/latoken-talent/latoken-161'
latoken_hackathon = 'https://deliver.latoken.com/hackathon'
latoken_culture = 'https://coda.io/@latoken/latoken-talent/culture-139'
START_PROMT = f"Смотри, теперь ты AI ассистент в компании LATOKEN. Проанализируй эти три ссылке: {latoken_info} {latoken_hackathon} {latoken_culture}. Используй эту инфромацию при генерации ответа, а так же для каждого ответа в конце указывай - Более подробную информацию вы можете получить по ссылке *тут нужная ссылка*."
client = AsyncOpenAI(
    api_key=GPT_TOKEN,
)
dp = Dispatcher()


async def request_for_response(promt):
    response = ''
    stream = await client.chat.completions.create(
        model="gpt-4o",
        messages= [{'role': 'user', 'content': promt}],
        stream=True,
    )
    async for chunk in stream:
        response += chunk.choices[0].delta.content or ""

    return response

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Привет, {message.from_user.full_name}! Я уникальный AI ассистент LATOKEN. Я нужен для подбора участников на хакатон!\n"
                         f"Задайте вопрос который хотите.")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        promt =
        text = await request_for_response(message.text)
        await message.answer(text)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    text = await request_for_response(START_PROMT)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())