from telebot import TeleBot
import bypass

bot = TeleBot('6682279482:AAHyfXCzAYIgrPDNfq9y6gU4_oTDfDk-i8Q')


@bot.message_handler(commands=['start'])
def generator(message):
    bot.reply_to(message, "Silahkan Kirim Linknya")
@bot.message_handler(content_types="text")
def generator(message):
    data = bypass.ouo_bypass(message.text)
    try:
        bot.reply_to(message, text=f'<code>{data}</code>', parse_mode="HTML")
    except:
        print(data)
        bot.reply_to(message, "Error")


bot.polling()