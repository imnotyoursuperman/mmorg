from pyrogram import Client
from handlers import start, character_creation, player_info, stats_management, exploration
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize bot client
bot = Client("mmo_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers
bot.add_handler(start.start_command)
bot.add_handler(character_creation.character_creation_flow)
bot.add_handler(player_info.player_info_command)
bot.add_handler(stats_management.stats_command)
bot.add_handler(exploration.exploration_command)

# Run the bot
if __name__ == "__main__":
    print("Starting the MMO Telegram Bot...")
    bot.run()
