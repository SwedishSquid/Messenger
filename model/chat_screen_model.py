from model.data import singletons


class ChatModel:
    def submit(self, message: str):
        print(f'enter pressed, printed: {message}')
        pass

    def on_back_button_action(self):
        singletons.get_screen_changer().goto_initial_screen()
        pass

# def submit(message: str):
#     print(f'enter pressed, printed: {message}')
#     pass
#
#
# def on_back_button_action():
#     singletons.get_screen_changer().goto_initial_screen()
#     pass
