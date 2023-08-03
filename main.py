import telebot
import atexit

from bot_token import BOT_TOKEN
from word_cloud import *
from parsing import *
from rating_calculation import *

bot = telebot.TeleBot(BOT_TOKEN)
first = 0
errors = {1: 'Некорретная ссылка', 2: 'Некорректная ссылка, введите полную ссылку на товар с Wildberries',
          3: 'Некорректная ссылка, введите полную ссылку на товар с Sbermegamarket'}

chat_id = 0
@bot.message_handler(commands=['start'])
def category(message):
    bot.send_message(message.chat.id, 'Введите полную ссылку на товар с Wildberries или SberMegaMarket')

@bot.message_handler(content_types=['text'])
def message_reply(message):
    global first
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Начинаем изучать комментарии')
    error = init(message.text)
    if error != 0:
        bot.send_message(chat_id, errors[error])
    else:
        bot.send_message(chat_id, 'Сбор комментариев завершен, готовим результаты')
        reviews_kirill_only, all_reviews = kirill_list()
        make_word_cloud(reviews_kirill_only)
        photo = open('wordcloud.png', 'rb')
        bot.send_photo(chat_id, photo)
        if first == 0:
            bot.send_message(chat_id, 'Перед вами облако слов — визуальное представление слов. '
                                          'Чем чаще слово встречается, тем больший размер оно принимает в облаке.')
        first = 1
        bot.send_message(chat_id, 'Нейросеть начинает анализировать отзывы, процесс может занять до 3 минут')
        positive, negative, neutral, length = rating(reviews_kirill_only)
        rating_result = f'% позитивных отзывов - {positive.size/length:.1%}, ' \
                        f'отрицательных - {negative.size/length:.1%}, ' \
                        f'нейтральных - {neutral.size/length:.1%}'

        bot.send_message(chat_id, rating_result)


        positive_rand = list(np.random.choice(positive, size=3, replace=False))
        negative_rand = list(np.random.choice(negative, size=3, replace=False))

        str_pos = '\n'.join(np.take(all_reviews, positive_rand))
        str_neg = '\n'.join(np.take(all_reviews, negative_rand))

        bot.send_message(chat_id, f'Случайные положительные отзывы: {str_pos}')
        bot.send_message(chat_id, f'Случайные отрицательные отзывы: {str_neg}')

@atexit.register
def goodbye():
    # отправляем сообщение о том, что бот выключен в чат с указанным идентификатором
    bot.send_message(chat_id, "Бот отключен")

bot.polling()


# распечатать пару плохих, хороших и нейтральных отзывов
# очередь/ответ, что процесс идет


