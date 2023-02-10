from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint


token1 = "6219208718:AAHyatt1K0m06BTdEZhrbUZtqs9c1H6JZe0"

bot = Bot(token="6219208718:AAHyatt1K0m06BTdEZhrbUZtqs9c1H6JZe0")
updater = Updater(token=token1)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет Настька! Напиши мне сообщение, а я удалю из него все слова, в которых есть 'абв'! ")

def del_words (update, contex):
    text = update.message.text.split()
    answer = list(filter(lambda x: not "абв" in x, text))
    answer = ' '.join(answer)
    contex.bot.send_message(update.effective_chat.id, answer)
    


start_handler = CommandHandler('start', start)
del_handler = MessageHandler(Filters.text, del_words)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(del_handler)

updater.start_polling()
updater.idle()


# from telegram import Bot, Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
# from random import randint as rd


# bot = Bot(token='5897211710:AAG0910uozqzP44r1OGkgyEzGf_fDBBTiQs')
# updater = Updater(token='5897211710:AAG0910uozqzP44r1OGkgyEzGf_fDBBTiQs')
# dispatcher = updater.dispatcher


# A = 0
# B = 1


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, 'РџСЂРёРІРµС‚\nРљР°Рє С‚РІРѕРё РґРµР»Р°?')
#     return A

# 

# def rand(update, context):
#     context.bot.send_message(update.effective_chat.id, f'{randint(1, 100)}')

# def default(update, contex):
#     contex.bot.send_message(update.effective_chat.id, "Я не умею разговаривать")

# def howareyou(update, context):
#     text = update.message.text
#     if 'С…РѕСЂ' in text.lower():
#         context.bot.send_message(update.effective_chat.id, 'РЇ СЂР°Рґ, С‡С‚Рѕ Сѓ С‚РµР±СЏ РІСЃРµ С…РѕСЂРѕС€Рѕ')
#     else:
#         context.bot.send_message(update.effective_chat.id, 'РќРµ РіСЂСѓСЃС‚Рё, РІСЃРµ Р±СѓРґРµС‚ РѕС‚Р»РёС‡РЅРѕ')
#     context.bot.send_message(update.effective_chat.id, 'РљР°Рє РїРѕРіРѕРґР°?')
#     return B

# def weather(update, context):
#     text = update.message.text
#     context.bot.send_message(update.effective_chat.id, 'РќСѓ РѕРє, Сѓ РјРµРЅСЏ С‚РѕР¶Рµ СЃРµРіРѕРґРЅСЏ С…РѕСЂРѕС€Р°СЏ РїРѕРіРѕРґР°')

#     return ConversationHandler.END


# def cancel(update, context):
#     context.bot.send_message(update.effective_chat.id, 'РџСЂРѕС‰Р°Р№!!!')


# start_handler = CommandHandler('start', start)
# howareyou_handler = MessageHandler(Filters.text, howareyou)
# weather_handler = MessageHandler(Filters.text, weather)
# cancel_handler = CommandHandler('cancel', cancel)
# # message_handler = MessageHandler(Filters.text, voice)
# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                     states={A: [howareyou_handler],
#                                     B: [weather_handler]},
#                                     fallbacks=[cancel_handler])

# start_handler = CommandHandler('start', start)
# random_handler = CommandHandler('random', rand)
# default_handler = MessageHandler(Filters.voice, default)

# dispatcher.add_handler(conv_handler)

# updater.start_polling()
# updater.idle() 