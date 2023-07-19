from model import text_screen_model
from view import text_screen


def init():
    text_screen.on_next_button_action = text_screen_model.on_next_button_action
    pass
