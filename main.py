import telebot

from parsing import *
from word_cloud import *
from bot_token import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def category(message):
    bot.send_message(message.chat.id, 'Введите ссылку на товар с Wildberries/SberMegaMarket')

@bot.message_handler(content_types=['text'])
def message_reply(message):
    init(message.text)
    make_word_cloud()
    photo = open('wordcloud.png', 'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling()

# if __name__ == '__main__':
#     pass
