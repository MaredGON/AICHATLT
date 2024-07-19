from openai import AsyncOpenAI

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# bot
TOKEN = "6440161421:AAEiJX0-Q75h0mv4tBT5dJ0gfD_jXraRUQY"
GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# chat gpt
latoken_info = "https://coda.io/@latoken/latoken-talent/latoken-161"
latoken_hackathon = "https://deliver.latoken.com/hackathon"
latoken_culture = "https://coda.io/@latoken/latoken-talent/culture-139"
client = AsyncOpenAI(
    api_key=GPT_TOKEN,
)

START_PROMT = (
    "Смотри, теперь ты AI ассистент в компании LATOKEN. Проанализируй эти три ссылке: "
    f"{latoken_info} {latoken_hackathon} {latoken_culture}. Используй эту инфромацию при генерации ответа, "
    "а так же для каждого ответа в конце указывай - Более подробную информацию вы можете получить по ссылке *тут нужная ссылка*."
)