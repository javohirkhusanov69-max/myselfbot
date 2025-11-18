from google import genai
import telebot

# AI API KEYNI KIRITING
AI_API_KEY="AIzaSyBi41_sStC1bEstO0wBEdZWQoHfpeIwSzs"

# BOT TOKENNI KIRITING
BOT_TOKEN="8580606403:AAG4BgDiZr2aK6ofRvEwFIZKTrwhwKYhrUA"

client = genai.Client(api_key=AI_API_KEY)
bot = telebot.TeleBot(BOT_TOKEN)

# START BOSILGANDA
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Welcome To ByTroX Ai!")


# HAR QANDAY MESSAGE KELGANDA
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message.text
        )

        if response.text:
            text = response.text.strip()
        else:
            text = "Answer Not Found."

        bot.reply_to(message, text)

    # XATOLIK YUZ BERGANDA
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

print("Bot is Working!")

# BOTNI ISHGA TUSHIRISH
bot.polling(none_stop=True)
