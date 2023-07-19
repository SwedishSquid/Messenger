from view.test_screen import test_screen
from model import test_screen_model


def init():
    test_screen.on_next_screen_button = test_screen_model.on_next_button_action
    pass
