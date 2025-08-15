from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# تحميل التوكن من ملف البيئة
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"مرحباً بك يا {update.effective_user.first_name}! 👋")

# أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🛠️ الأوامر المتاحة:\n"
        "/start - بدء المحادثة 👋\n"
        "/help - عرض هذه القائمة 📜\n"
        "يمكنك إضافة أوامر أخرى هنا..."
    )
    await update.message.reply_text(help_text)

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()