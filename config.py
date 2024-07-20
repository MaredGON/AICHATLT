from collections import defaultdict

from openai import AsyncOpenAI

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# bot
TOKEN = "6440161421:AAEiJX0-Q75h0mv4tBT5dJ0gfD_jXraRUQY"
GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"
user_message_times = defaultdict(lambda: 0)
TIME_LIMIT = 5
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# chat gpt
client = AsyncOpenAI(
    api_key=GPT_TOKEN,
)


class Promts:
    company_info = "./datainfo/datalatoken.txt"
    hackathon_info = "./datainfo/datahackathon.txt"
    culture_info = "./datainfo/dataculture.txt"
    answer_example = "./datainfo/answer_example.txt"

    @staticmethod
    def get_company_info():
        with open(Promts.company_info, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def get_hackathon_info():
        with open(Promts.hackathon_info, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def get_culture_info():
        with open(Promts.culture_info, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def get_answer_example():
        with open(Promts.answer_example, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def default_promt():
        return f"""
        Ты - полезный ассистент, помогающий пользователям с вопросами по компании LATOKEN биржа.
        Тебя создали на Хакатоне.
        Используй имя запросившего в ответе на запрос.
        Вот информация о компании LATOKEN биржа:
        Основная ифнормация: {Promts.get_company_info()}
        Информация о хакатоне: {Promts.get_hackathon_info()}
        Информация о культуре: {Promts.get_culture_info()}
        
        При ответе пользователю ты не должен выдавать весь текст файла, ты должен генерировать данные на основе файлов.
        Ты должен отвечать только на вопросы. Твои ответы должны быть приведены в человекоподобный вид.
        Так, чтобы живому человеку было удобно их читать.
        Не рассказывай сразу суть задачи, расскажи только в случае если спросят конкретно.
        В ответ на каждое сообщение присылай в конце ссылку, спросили про компанию - присылай ссылку о LATOKEN, спросили про хакатон - присылай ссылку на хакатон, спросили о культуре - присылай ссылку о культуре
        Не говори привет.
        
        Не используй выделение форматиррование текста. Например: **Какой-то текст**. Так делать не надо.
        """

    @staticmethod
    def user_message_promt(user_message):
        return f"""
        {Promts.default_promt()}

        Вопрос пользователя: {user_message}
        """
