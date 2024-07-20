from config import TOKEN, client, START_PROMT, Promts


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
        stream=True,
    )
    async for chunk in stream:
        response += chunk.choices[0].delta.content or ""

    return response
