import telebot

from parsing import *
from word_cloud import *
from bot_token import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

errors = {1: 'Некорретная ссылка', 2: 'Некорректная ссылка, введите полную ссылку на товар с Wildberries',
          3: 'Некорректная ссылка, введите полную ссылку на товар с Sbermegamarket'}


@bot.message_handler(commands=['start'])
def category(message):
    bot.send_message(message.chat.id, 'Введите полную ссылку на товар с Wildberries или SberMegaMarket')

@bot.message_handler(content_types=['text'])
def message_reply(message):

    bot.send_message(message.chat.id, 'Начинаем изучать комментарии')

    error = init(message.text)
    if error != 0:
        bot.send_message(message.chat.id, errors[error])
    else:
        bot.send_message(message.chat.id, 'Сбор комментариев завершен, готовим результаты')
        make_word_cloud()
        photo = open('wordcloud.png', 'rb')
        bot.send_photo(message.chat.id, photo)

bot.polling()

# if __name__ == '__main__':
#     pass
