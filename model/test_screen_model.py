from model.data import singletons


def on_next_button_action():
    singletons.get_screen_changer().goto_text_screen()
    pass
