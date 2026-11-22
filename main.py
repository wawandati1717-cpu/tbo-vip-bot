import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo bos! Bot TBO VIP sudah jalan ✅\nKetik /menu untuk lihat menu.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("MENU TBO VIP:\n1. Cek VIP\n2. Info\n3. Bantuan")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    print("Bot jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
