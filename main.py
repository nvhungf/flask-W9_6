import os
import telebot
from flask import Flask, request
# secret = 'abcookkkkkk'
token = '6204857251:AAH6rSpTklODerCsdGWJ29P_sxE_8hkSV3Y'
url = 'https://flask-production-54e7.up.railway.app/' 
bot = telebot.TeleBot(token=token, threaded = False)
bot.remove_webhook()
bot.set_webhook(url=url)
app = Flask(__name__)
@app.route('/',methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK'
@bot.message_handler(content_types=['start'])
def start(message):
    bot.send_message(message.chat.id,'ok fen')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
