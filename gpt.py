from typing import Tuple, List
import re

from config import client, Promts


async def request_for_response(user_message: str) -> str:
    """
    Отправляет запрос к API OpenAI и возвращает ответ.

    :param promt: Текст запроса.
    :return: Ответ от API OpenAI.
    """

    response = ""
    stream = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": Promts.user_message_promt(user_message)},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        stream=True,
    )
    async for chunk in stream:
        response += chunk.choices[0].delta.content or ""

    return response


async def request_for_response_quiz(text: str) -> tuple[str, list[str], int]:
    """
    Отправляет запрос к API OpenAI и возвращает ответ.

    :param promt: Текст запроса.
    :return: Ответ от API OpenAI.
    """
    try:
        response = ""
        stream = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f'{Promts.quiz_promt()}{text}'},
            ],
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            stream=True,
        )
        async for chunk in stream:
            response += chunk.choices[0].delta.content or ""

        parts = response.split(":")
        question = parts[0].strip()
        answers = parts[1].strip().split(" ")
        nice_answer = parts[2].strip()
        match = re.search(r'\d+', nice_answer)
        nice_answer = int(match.group())
        return question, answers, nice_answer
    except:
        ...