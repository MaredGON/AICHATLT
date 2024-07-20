import openai
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import bot, dp

storage = MemoryStorage()

# Определение состояний
class Survey(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()

# Стартовое сообщение
@dp.message(Command("start"))
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(Survey.q1)
    keyboard = InlineKeyboardBuilder()
    options = [
        "О Хакатоне deliver.latoken.com/hackathon",
        "О Латокен deliver.latoken.com/about",
        "Большая часть из #nackedmanagement coda.io/@latoken/latoken-talent/nakedmanagement-88"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Какие из этих материалов вы прочитали? (множественный выбор)", reply_markup=keyboard.as_markup())

# Вопрос 1
@dp.callback_query(Survey.q1)
async def process_q1(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if 'q1' not in data:
            data['q1'] = []
        if callback_query.data in data['q1']:
            data['q1'].remove(callback_query.data)
        else:
            data['q1'].append(callback_query.data)
    await callback_query.answer()

@dp.message(Survey.q1)
async def ask_q2(message: Message, state: FSMContext):
    await state.set_state(Survey.q2)
    keyboard = InlineKeyboardBuilder()
    options = [
        "25,000 Опционов",
        "100,000 Опционов или 10,000 LA",
        "Только бесценный опыт"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Какой призовой фонд на Хакатоне? (единственный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q2)
async def process_q2(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['q2'] = callback_query.data
    await state.set_state(Survey.q3)
    await ask_q3(callback_query.message, state)

# Вопрос 3
async def ask_q3(message: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    options = [
        "Показать мои способности узнавать новые технологии",
        "Показать работающий сервис",
        "Продемонстрировать навыки коммуникации и командной работы"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Что от вас ожидают на хакатоне в первую очередь? (единственный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q3)
async def process_q3(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['q3'] = callback_query.data
    await state.set_state(Survey.q4)
    await ask_q4(callback_query.message, state)

# Вопрос 4
async def ask_q4(message: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    options = [
        "Быстрый рост через решение нетривиальных задач",
        "Передовые технологии AIxWEB3",
        "Глобальный рынок, клиенты в 200+ странах",
        "Возможность совмещать с другой работой и хобби",
        "Самая успешная компания из СНГ в WEB3",
        "Удаленная работа, но без давншифтинга",
        "Оплата в твердой валюте, без привязки к банкам",
        "Опционы с \"откешиванием\" криптолетом",
        "Комфортная среда для свободы творчества"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Что из этого является преимуществом работы в Латокен? (множественный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q4)
async def process_q4(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if 'q4' not in data:
            data['q4'] = []
        if callback_query.data in data['q4']:
            data['q4'].remove(callback_query.data)
        else:
            data['q4'].append(callback_query.data)
    await callback_query.answer()

# Вопрос 5
@dp.message(Survey.q4)
async def ask_q5(message: Message, state: FSMContext):
    await state.set_state(Survey.q5)
    await message.answer("Каковы Ваши зарплатные ожидания в USD? (свободный ответ)")

@dp.message(Survey.q5)
async def process_q5(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['q5'] = message.text
    await state.set_state(Survey.q6)
    await ask_q6(message, state)

# Вопрос 6
async def ask_q6(message: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    options = [
        "Пятница: 18:00 Разбор задач. Суббота: 18:00 Демо результатов, 19-00 объявление победителей, интервью и офферы",
        "Суббота: 12:00 Презентация компании, 18:00 Презентации результатов проектов"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Какое расписание Хакатона корректнее? (единственный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q6)
async def process_q6(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['q6'] = callback_query.data
    await state.set_state(Survey.q7)
    await ask_q7(callback_query.message, state)

# Вопрос 7
async def ask_q7(message: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    options = [
        "Сосредотачивается на общей картине и дает сотрудникам принимать детальные решения на общей картине и дает команде возможность принимать детальные решения",
        "Употребляет ненормативную лексику, кричит, редко говорит спокойным тоном",
        "Терпит отклонения от плана, если они связаны с усилиями и творчеством",
        "Не терпит отклонений от плана",
        "Обучает своих сотрудников для обеспечения их удовлетворенности и карьерного развития",
        "Тренерует сотрудников, так чтобы им не прострелили зад на поле боя"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Каковы признаки \"Wartime CEO\" согласно крупнейшему венчурному фонду a16z? (множественный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q7)
async def process_q7(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if 'q7' not in data:
            data['q7'] = []
        if callback_query.data in data['q7']:
            data['q7'].remove(callback_query.data)
        else:
            data['q7'].append(callback_query.data)
    await callback_query.answer()

# Вопрос 8
@dp.message(Survey.q7)
async def ask_q8(message: Message, state: FSMContext):
    await state.set_state(Survey.q8)
    keyboard = InlineKeyboardBuilder()
    options = [
        "Спокойной работы без излишнего стресса",
        "Вникания в блокеры вне основного стека, чтобы довести свою задачу до прода",
        "Тестирование продукта",
        "Субординацию, и не вмешательство чужие дела",
        "Вежливость и корректность в коммуникации",
        "Измерение результатов",
        "Демонстрацию результатов в проде каждую неделю"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Что Латокен ждет от каждого члена команды? (множественный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q8)
async def process_q8(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if 'q8' not in data:
            data['q8'] = []
        if callback_query.data in data['q8']:
            data['q8'].remove(callback_query.data)
        else:
            data['q8'].append(callback_query.data)
    await callback_query.answer()

# Вопрос 9
@dp.message(Survey.q8)
async def ask_q9(message: Message, state: FSMContext):
    await state.set_state(Survey.q9)
    keyboard = InlineKeyboardBuilder()
    options = [
        "Да",
        "Да, но если преподаватель точно не увидит",
        "Да, но только если мне тоже помогут",
        "Нет",
        "Нет, если мне не дадут посмотреть эти ответы",
        "Нет, если это может мне повредить"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Представьте вы на выпускном экзамене. Ваш сосед слева просит вас передать ответы от соседа справа. Вы поможете? (единственный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q9)
async def process_q9(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['q9'] = callback_query.data
    await state.set_state(Survey.q10)
    await ask_q10(callback_query.message, state)

# Вопрос 10
async def ask_q10(message: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    options = [
        "1 кг",
        "1.5 кг",
        "2 кг",
        "3 кг"
    ]
    for option in options:
        keyboard.add(InlineKeyboardButton(text=option, callback_data=option))
    await message.answer("Кирпич весит килограмм и еще пол-кирпича. Сколько весит кирпич? (единственный выбор)", reply_markup=keyboard.as_markup())

@dp.callback_query(Survey.q10)
async def process_q10(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['q10'] = callback_query.data
    await state.set_state(Survey.q11)
    await ask_q11(callback_query.message, state)

# Вопрос 11
async def ask_q11(message: Message, state: FSMContext):
    await state.set_state(Survey.q11)
    await message.answer("Напишите ваши \"за\" и \"против\" работы в Латокен? Чем подробнее, тем лучше - мы читаем. (свободный ответ)")

@dp.message(Survey.q11)
async def process_q11(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['q11'] = message.text
    # Закончить анкетирование
    await message.answer("Спасибо за ваши ответы!")
    await state.clear()
