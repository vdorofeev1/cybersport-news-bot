import os

from telegram import Update, ForceReply
from telegram.error import BadRequest
from telegram.ext import Application, CommandHandler

from script.get_news import get_news

token = os.getenv("CYBER_TOKEN")


async def start(update: Update) -> None:
    news = get_news()
    for new in news:
        try:
            await update.message.reply_html(
                rf"{new}",
                reply_markup=ForceReply(selective=True),
            )
        except BadRequest:
            print(len(new))
            print("жопа")


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
