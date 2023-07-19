from model import initial_screen_model
from view import initial_screen


def init():
    initial_screen.on_to_messenger_button = initial_screen_model.to_messenger_button_action
    initial_screen.on_next_screen_button = initial_screen_model.next_screen_button_action
    pass