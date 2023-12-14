from script.get_news import get_news

token = "6884364191:AAE0WBA4Sf7bkpE52_88Jsh6uAYQAwfGlCQ"

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update, ForceReply
from telegram.error import BadRequest


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news = get_news()
    for new in news:
        try:
            await update.message.reply_html(
                rf"{new}",
                reply_markup=ForceReply(selective=True),
            )
        except BadRequest:
            print("жопа")


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
