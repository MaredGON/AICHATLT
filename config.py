from collections import defaultdict
from dotenv import load_dotenv
import os

from openai import AsyncOpenAI

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# bot
load_dotenv()
TOKEN = os.getenv('TOKEN_BOT')
GPT_TOKEN = os.getenv('GPT_TOKEN_AI')
TRIGGER_WORDS = [
    "хакатоне",
    "компании",
    "культуре",
    "хакатон",
    "о себе",
    "себе",
    "культура",
    "культуре",
    "хакатоне компании",
    "хакатоне культуре",
    "хакатоне хакатон",
    "хакатоне о себе",
    "хакатоне себе",
    "хакатоне культура",
    "хакатоне культуре",
    "компании культуре",
    "компании хакатон",
    "компании о себе",
    "компании себе",
    "компании культура",
    "компании культуре",
    "культуре хакатон",
    "культуре о себе",
    "культуре себе",
    "культуре культура",
    "культуре культуре",
    "хакатон о себе",
    "хакатон себе",
    "хакатон культура",
    "хакатон культуре",
    "о себе себе",
    "о себе культура",
    "о себе культуре",
    "себе культура",
    "себе культуре",
    "культура культуре",
    "хакатоне компании культуре",
    "хакатоне компании хакатон",
    "хакатоне компании о себе",
    "хакатоне компании себе",
    "хакатоне компании культура",
    "хакатоне компании культуре",
    "хакатоне хакатон о себе",
    "хакатоне хакатон себе",
    "хакатоне хакатон культура",
    "хакатоне хакатон культуре",
    "хакатоне о себе себе",
    "хакатоне о себе культура",
    "хакатоне о себе культуре",
    "хакатоне себе культура",
    "хакатоне себе культуре",
    "хакатоне культура культуре",
    "компании хакатон о себе",
    "компании хакатон себе",
    "компании хакатон культура",
    "компании хакатон культуре",
    "компании о себе себе",
    "компании о себе культура",
    "компании о себе культуре",
    "компании себе культура",
    "компании себе культуре",
    "компании культура культуре",
    "культуре хакатон о себе",
    "культуре хакатон себе",
    "культуре хакатон культура",
    "культуре хакатон культуре",
    "культуре о себе себе",]
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
        Ты - полезный ассистент и тебя зовут Оля, помогающий пользователям с вопросами по компании LATOKEN биржа.
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
    def quiz_promt():
        return f"""
                Ты - полезный ассистент и тебя зоыут Оля, помогающий пользователям с вопросами по компании LATOKEN биржа.
                Тебя создали на Хакатоне.
                Используй имя запросившего в ответе на запрос.
                Вот информация о компании LATOKEN биржа:
                Основная ифнормация: {Promts.get_company_info()}
                Информация о хакатоне: {Promts.get_hackathon_info()}
                Информация о культуре: {Promts.get_culture_info()}

                Создай вопрос и 4 варианта ответа и правильный ответ. В ответе должно быть "тут вопрос":"тут 4 варианта ответа через пробел":"0 если первый вариант ответа, 1 если второй вариант ответа, 2 если третий вариант ответа, 3 если четвертый вариант ответа" .Отвечай только в таком формате. Текст для вопроса: 
                """
    @staticmethod
    def user_message_promt(user_message):
        return f"""
        {Promts.default_promt()}

        Вопрос пользователя: {user_message}
        """
