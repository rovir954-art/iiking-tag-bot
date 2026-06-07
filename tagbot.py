from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = 8579054278:AAGsjZMeV7gFQXXgsaGS2ea-X1GGqVu8SEw

group_users = {}

async def track_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_user or not update.effective_chat:
        return

    if update.effective_chat.type not in ["group", "supergroup"]:
        return

    chat_id = update.effective_chat.id
    user = update.effective_user

    if chat_id not in group_users:
        group_users[chat_id] = {}

    group_users[chat_id][user.id] = user.first_name or "user"

async def tagall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if chat_id not in group_users or not group_users[chat_id]:
        await update.message.reply_text("No users yet.")
        return

    mentions = [
        f"[{name}](tg://user?id={uid})"
        for uid, name in group_users[chat_id].items()
    ]

    await update.message.reply_text(
        "👥 Tagging group members:\n" + " ".join(mentions[:50]),
        parse_mode="Markdown"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot active!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tagall", tagall))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_user))

app.run_polling()
