from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from templates.messages import WELCOME_MESSAGE
from config import WELCOME_IMAGE_URL

def start_command(client, message):
    user = message.from_user
    welcome_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Start Character Creation", callback_data="start_character_creation")]
    ])

    client.send_photo(
        chat_id=user.id,
        photo=WELCOME_IMAGE_URL,
        caption=WELCOME_MESSAGE.format(name=user.first_name),
        reply_markup=welcome_keyboard
    )
