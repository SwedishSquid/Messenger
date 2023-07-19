from model.data import singletons


def submit(message: str):
    print(f'enter pressed, printed: {message}')
    pass


def on_back_button_action():
    singletons.get_screen_changer().goto_initial_screen()
    pass
