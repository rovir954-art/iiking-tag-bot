from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = 8579054278:AAGsjZMeV7gFQXXgsaGS2ea-X1GGqVu8SEw

users = set()

async def track_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user:
        users.add(update.effective_user.id)

async def tagall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mentions = [f"[user](tg://user?id={uid})" for uid in users]

    if mentions:
        await update.message.reply_text(" ".join(mentions[:50]), parse_mode="Markdown")
    else:
        await update.message.reply_text("Koi user save nahi hua hai.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot active hai in group!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tagall", tagall))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_user))

app.run_polling()
