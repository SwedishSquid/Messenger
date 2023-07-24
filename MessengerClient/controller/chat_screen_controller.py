from model import chat_screen_model
from view import chat_screen


def init():
    chat_screen.on_back_button = chat_screen_model.on_back_button_action
    chat_screen.submit = chat_screen_model.submit
    pass
