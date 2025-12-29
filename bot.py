import telebot
import yt_dlp
import time

api = "8234937237:AAGoG2M_LS94GDtfmhZV5dTsxwL0muFsGqM"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, "سلام فاطمه خوبی؟ لینک ویدیو رو بفرست")

@bot.message_handler(func=lambda message: True)
def handle_url(message):
    url = message.text.strip()

    if "https://" in url or "youtu.be" in url:
        bot.reply_to(message, "لینک معتبره، میرم برای دانلود...")

        try:
            output_file = f"{message.chat.id}_{int(time.time())}.mp4"

            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': output_file
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            with open(output_file, "rb") as video:
                bot.send_video(message.chat.id, video)

            bot.reply_to(message, "دانلود و ارسال کامل شد ✔")

        except Exception as error:
            bot.reply_to(message, f"❌ خطا هنگام دانلود: {error}")

    else:
        bot.reply_to(message, "❌ لینک معتبر نیست. لطفاً لینک یوتیوب بفرست.")

print("Bot is running...")
bot.infinity_polling()