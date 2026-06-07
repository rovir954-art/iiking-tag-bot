from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = 8579054278:AAGsjZMeV7gFQXXgsaGS2ea-X1GGqVu8SEw

users = set()

async def save_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user:
        users.add(update.effective_user.id)

async def tagall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mentions = []
    for user_id in users:
        mentions.append(f"[user](tg://user?id={user_id})")

    if mentions:
        await update.message.reply_text(" ".join(mentions[:50]), parse_mode="Markdown")
    else:
        await update.message.reply_text("Koi user save nahi hai.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot active hai.")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tagall", tagall))
app.add_handler(CommandHandler("save", save_user))

app.run_polling()
