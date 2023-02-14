from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from models import calc, string_to_list

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Добро пожаловать в калькулятор! Введи через пробелы выражение, которое хочешь посчитать: ")

def get_message(update, context):
    text = update.message.text
    answer = calc(string_to_list(text))
    context.bot.send_message(update.effective_chat.id, f'результат вычислений: {answer}')

