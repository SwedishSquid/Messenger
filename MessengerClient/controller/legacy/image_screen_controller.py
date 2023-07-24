from model.legacy import image_screen_model
from view.legacy import image_screen


def init():
    image_screen.get_next_image = image_screen_model.get_next_image
    image_screen.on_next_screen_button = image_screen_model.on_next_screen_button_action