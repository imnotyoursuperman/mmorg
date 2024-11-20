from pyrogram.types import CallbackQuery
from templates.keyboards import get_customization_keyboard
from utils.database import save_character_data

def character_creation_flow(client, callback_query: CallbackQuery):
    step = callback_query.data.split(":")[1]  # Example: "race", "class"
    user_id = callback_query.from_user.id

    if step == "race":
        callback_query.message.edit_text("Choose your race:", reply_markup=get_customization_keyboard("race"))
    elif step == "class":
        callback_query.message.edit_text("Choose your class:", reply_markup=get_customization_keyboard("class"))
    elif step == "save":
        save_character_data(user_id, callback_query.data)
        callback_query.message.edit_text("Character saved!")
