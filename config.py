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



class Promts:
    company_info = "./datainfo/datalatoken.txt"
    hackathon_info = "./datainfo/datahackathon.txt"
    culture_info = "./datainfo/dataculture.txt"

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
    def default_promt():
        return f"""
        Ты - полезный ассистент, помогающий пользователям с вопросами по компании LATOKEN биржа.
        Вот информация о компании LATOKEN биржа:
        Основная ифнормация: {Promts.get_company_info()}
        Информация о хакатоне: {Promts.get_hackathon_info()}
        Информация о культуре: {Promts.get_culture_info()}
        
        При ответе пользователю ты не должен выдавать весь текст файла.
        Ты должен отвечать только на вопросы. Твои ответы должны быть приведены в человекоподобный вид.
        Так, чтобы живому человеку было удобно их читать.
        
        Не используй выделение форматиррование текста. Например: **Какой-то текст**. Так делать не надо.
        """

    @staticmethod
    def user_message_promt(user_message):
        return f"""
        {Promts.default_promt()}

        Вопрос пользователя: {user_message}
        """
