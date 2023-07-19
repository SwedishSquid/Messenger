from model import text_screen_model
from view import text_screen


def init():
    text_screen.on_next_screen_button_action = text_screen_model.on_next_screen_button_action
    text_screen.on_next_text_button = text_screen_model.on_next_text_button_action
    text_screen.on_previous_text_button = text_screen_model.on_previous_text_button_action
    pass
