from model import login_screen_model
from view import login_screen


def init():
    login_screen.on_submit_button_pressed = login_screen_model.on_submit_button_pressed
    login_screen.on_password_entered = login_screen_model.on_password_entered
    login_screen.on_username_entered = login_screen_model.on_username_entered
    pass
