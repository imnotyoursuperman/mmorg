# Initializes the templates package
from .keyboards import get_customization_keyboard
from .messages import WELCOME_MESSAGE, PLAYER_INFO_TEMPLATE

__all__ = ["get_customization_keyboard", "WELCOME_MESSAGE", "PLAYER_INFO_TEMPLATE"]
