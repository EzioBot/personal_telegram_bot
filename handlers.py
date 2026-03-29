from telegram import Update
from telegram.ext import ContextTypes
import logging

from db import insert_message

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    user = update.effective_user
    logging.info(f"User {user.id} ({user.username}) started the bot.")
    await update.message.reply_html(
        f"Hi {user.mention_html()}! Welcome to your Telegram bot. "
        "Send me any message, and I'll save it and echo it back."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /help command."""
    user = update.effective_user
    logging.info(f"User {user.id} ({user.username}) requested help.")
    await update.message.reply_text(
        "I can store your messages and respond to certain keywords.\n\n"
        "Try sending 'hello' or any other message to see how I respond."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles incoming text messages, stores them, and provides a response."""
    user = update.effective_user
    message_text = update.message.text

    logging.info(f"Received message from {user.id} ({user.username}): {message_text}")

    # Store the message in the database
    if insert_message(user.id, user.username, message_text):
        response_text = "Message saved! "
    else:
        response_text = "Could not save your message. "

    # Basic processing logic
    if message_text.lower() == "hello":
        response_text += "Hi there!"
    else:
        response_text += f"You said: '{message_text}'"

    await update.message.reply_text(response_text)
