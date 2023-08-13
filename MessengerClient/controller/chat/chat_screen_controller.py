from controller.chat.chat_screen_controller_interface import ChatScreenControllerInterface
from model.chat_screen_model import ChatModel
from view.chat_screen import ChatScreen


class ChatScreenController(ChatScreenControllerInterface):
    def __init__(self, chat_model: ChatModel, chat_screen: ChatScreen):
        self.chat_model: ChatModel = chat_model
        self.chat_screen: ChatScreen = chat_screen
        pass

    def on_submit(self):
        self.chat_model.on_submit()
        pass

    def on_back_button(self):
        self.chat_model.on_back_button_action()
        pass

    def on_load_button(self):
        self.chat_model.on_load_data()
        pass

    def get_data(self):
        return self.chat_screen.get_data()

    def get_typed_message(self):
        return self.chat_screen.get_typed_message()
