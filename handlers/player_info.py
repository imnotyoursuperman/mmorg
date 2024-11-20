from pyrogram.types import Message
from utils.database import get_character_data
from templates.messages import PLAYER_INFO_TEMPLATE

def player_info_command(client, message: Message):
    user_id = message.from_user.id
    character_data = get_character_data(user_id)

    if character_data:
        info_message = PLAYER_INFO_TEMPLATE.format(
            name=character_data["name"],
            race=character_data["race"],
            class=character_data["class"],
            stats=character_data["stats"],
            nickname=character_data["nickname"],
            level=character_data["level"]
        )
        message.reply(info_message)
    else:
        message.reply("No character data found. Please create a character first.")
