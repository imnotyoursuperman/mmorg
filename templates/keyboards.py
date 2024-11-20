from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_customization_keyboard(category):
    if category == "race":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("Human", callback_data="race:human")],
            [InlineKeyboardButton("Elf", callback_data="race:elf")],
            [InlineKeyboardButton("Orc", callback_data="race:orc")],
            [InlineKeyboardButton("Goblin", callback_data="race:goblin")]
        ])
    elif category == "class":
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("Warrior", callback_data="class:warrior")],
            [InlineKeyboardButton("Mage", callback_data="class:mage")],
            [InlineKeyboardButton("Paladin", callback_data="class:paladin")]
        ])
