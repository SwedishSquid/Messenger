from model.data import singletons


def to_messenger_button_action():
    singletons.get_screen_changer().goto_login_screen()
    pass


def next_screen_button_action():
    singletons.get_screen_changer().goto_test_screen()
    pass
