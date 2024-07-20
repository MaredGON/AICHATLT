import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from openai import OpenAI


GPT_TOKEN = "sk-proj-8f2n9OhSdDhYcKoWEkiBT3BlbkFJTye8GS9wRoQC2pbDkA9I"

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



assistant = client.beta.assistants.create(
    name="Ты AI ассистент компании LATOKEN",
    description="Ты AI ассистент, который берет информацию о компании из datalatoken.txt, информацию о хакатоне из datahackathon.txt, информацию о культуре из dataculture.txt. Ты нужен кандидатам чтобы отвечать на вопросы: о компании, культуре, хакатоне. ",
    model="gpt-4o",
    tools=[{"type": "file_search"}],
    tool_resources={"code_interpreter": {"file_ids": [file1.id, file2.id, file3.id]}},
)
