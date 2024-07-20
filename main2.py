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

files_to_upload = ['datalatoken.txt', 'datahackathon.txt','dataculture.txt']

uploaded_files = []
for file_name in files_to_upload:
    with open(file_name, "rb") as file:
        uploaded_file = client.files.create(
            file=file,
            purpose='assistants'
        )
        uploaded_files.append(uploaded_file)

assistant = client.beta.assistants.create(
  name="Ты AI ассистент компании LATOKEN",
  description="Ты AI ассистент, который берет информацию о компании из datalatoken.txt, информацию о хакатоне из datahackathon.txt, информацию о культуре из dataculture.txt. Ты нужен кандидатам чтобы отвечать на вопросы: о компании, культуре, хакатоне. ",
  model="gpt-4o",
  tools=[{"type": "retrieval"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [uploaded_files[0]]
    }
  }
)
