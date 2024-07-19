import os
import asyncio
from openai import AsyncOpenAI

# Убедитесь, что ваш API ключ установлен
GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"
client = AsyncOpenAI(
    api_key=GPT_TOKEN,
)
latoken_info = "https://coda.io/@latoken/latoken-talent/latoken-161"
latoken_hackathon = "https://deliver.latoken.com/hackathon"
latoken_culture = "https://coda.io/@latoken/latoken-talent/culture-139"
promt = f"Смотри, теперь ты AI ассистент в компании LATOKEN. Ты будешь отвечать на вопросы про компанию LATOKEN. Проанализируй эти три ссылке: {latoken_info} {latoken_hackathon} {latoken_culture}. Используй эту инфромацию при дальнейших запросов, а так же для каждого ответа в конце указывай - Более подробную информацию вы можете получить по ссылке *тут нужная ссылка если* "
promt1 = f"какое место занимает Latoken среди криптобирж? "


async def request_for_response():
    stream = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": promt}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(request_for_response())
