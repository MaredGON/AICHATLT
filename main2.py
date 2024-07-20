import asyncio
import logging
import sys
from openai import OpenAI
from config import Promts

GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"
async def start_assistant():
    client = OpenAI(
        api_key=GPT_TOKEN,
    )
    files_to_upload = ["./datainfo/datalatoken.txt", "./datainfo/datahackathon.txt", "./datainfo/dataculture.txt"]
    file1 = client.files.create(
        file=open(files_to_upload[0], "rb"),
        purpose='assistants'
    )
    file2 = client.files.create(
        file=open(files_to_upload[1], "rb"),
        purpose='assistants'
    )
    file3 = client.files.create(
        file=open(files_to_upload[2], "rb"),
        purpose='assistants'
    )

    assistant = await client.beta.assistants.create(
        name="Ты AI ассистент компании LATOKEN",
        description="Ты AI ассистент, который берет информацию о компании из datalatoken.txt, информацию о хакатоне из datahackathon.txt, информацию о культуре из dataculture.txt. Ты нужен кандидатам чтобы отвечать на вопросы: о компании, культуре, хакатоне. ",
        model="gpt-4o",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"file_ids": [file1.id, file2.id, file3.id]}},
    )

    # Создание потока и начального сообщения
    thread = await client.beta.threads.create()
    message = await client.beta.threads.messages.create(
        thread_id=thread['id'],
        role="system",
        content=Promts.default_promt
    )

    # Запуск ассистента и опрос результатов
    run = await client.beta.threads.runs.create_and_poll(
        thread_id=thread['id'],
        assistant_id=assistant['id'],
        instructions="Вставляй в каждый вопрос ссылку где пользователь может посмотреть подробно о том что он спросил"
    )
    return thread.id


async def handle_incoming_messages(thread_id):
    while True:
        messages = await client.beta.threads.messages.list(thread_id=thread_id)
        for message in messages:
            if message['role'] == 'user':
                response = await client.beta.threads.messages.create(
                    thread_id=thread_id,
                    role="assistant",
                    content="Ваш обработанный ответ здесь"
                )
        await asyncio.sleep(1)

async def main():
    thread_id = await start_assistant()
    await handle_incoming_messages(thread_id=thread_id)

if __name__ == "__main__":
    asyncio.run(main())