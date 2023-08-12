from model.login_screen_model import LoginModel
from model.chat_screen_model import ChatModel

from model.data.singletons import Singletons


class Model:
    login_model: LoginModel
    chat_model: ChatModel

    def __init__(self):
        Singletons.get_model = self.get_model

        self.login_model = LoginModel()
        self.chat_model = ChatModel()
        pass

    def get_model(self):
        return self
    pass
