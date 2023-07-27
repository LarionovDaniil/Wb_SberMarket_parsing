import telebot

from bot_token import BOT_TOKEN
from word_cloud import *
from parsing import *
from rating_calculation import *

bot = telebot.TeleBot(BOT_TOKEN)
first = 0
errors = {1: 'Некорретная ссылка', 2: 'Некорректная ссылка, введите полную ссылку на товар с Wildberries',
          3: 'Некорректная ссылка, введите полную ссылку на товар с Sbermegamarket'}


@bot.message_handler(commands=['start'])
def category(message):
    bot.send_message(message.chat.id, 'Введите полную ссылку на товар с Wildberries или SberMegaMarket')

@bot.message_handler(content_types=['text'])
def message_reply(message):
    global first
    bot.send_message(message.chat.id, 'Начинаем изучать комментарии')
    aspx = message.text.find('aspx')
    right_link = message.text[:aspx+4]
    error = init(right_link)
    if error != 0:
        bot.send_message(message.chat.id, errors[error])
    else:
        bot.send_message(message.chat.id, 'Сбор комментариев завершен, готовим результаты')
        reviews_kirill_only = kirill_list()
        make_word_cloud(reviews_kirill_only)
        photo = open('wordcloud.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        if first == 0:
            bot.send_message(message.chat.id, 'Перед вами облако слов — визуальное представление слов.'
                                          'Чем чаще слово встречается, тем больший размер принимает в облаке.')
        first = 1
        bot.send_message(message.chat.id, 'Нейросеть начинает анализировать отзывы')
        positive, negative, neutral, length = rating(reviews_kirill_only)
        rating_result = f'% позитивных - {positive/length:.1%}, ' \
                        f'отрицательных - {negative/length:.1%}, ' \
                        f'нейтральных - {neutral/length:.1%}'

        bot.send_message(message.chat.id, rating_result)


bot.polling()

# if __name__ == '__main__':
#     pass
