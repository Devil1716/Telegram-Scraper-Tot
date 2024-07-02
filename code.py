import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, UpdateQueue

# Telegram Bot API Token
TELEGRAM_API_TOKEN: str = '7019121527:AAGFl5Xy5FEkgLmfP4gAN4dwMPwV5UYMz1E'
BOT_name  = 'drk17_bot'

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) :
    await update.message.reply_text('Hello! Send me a URL and I will scrape its title.')
# Function to handle messages
async def echo(update: Update, context: CallbackContext) :
    url = update.message.text.strip()

    # Check if the message is a valid URL
    if not url.startswith('http'):
        update.message.reply_text('Please send a valid URL.')
        return

    # Perform web scraping
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()

        update.message.reply_text(f'Title of the webpage: {title}')
    except Exception as e:
        update.message.reply_text(f'Error fetching title: {str(e)}')

# Main function to start the bot
def main() :

    app = Application.builder().token(TELEGRAM_API_TOKEN).build()


    # Define a command handler for the /start command
    app.add_handler(CommandHandler("start", start))

    # Define a message handler for all text messages (excluding commands)
    app.add_handler(MessageHandler(filters.Text ,filters.Command, echo))

    # Start polling updates from Telegram

    # Run the bot until you press Ctrl-C
if __name__ == '__main__':
    main()
