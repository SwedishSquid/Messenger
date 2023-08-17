from model.login_screen_model import LoginModel
from model.chat_screen_model import ChatModel
from model.register_model import RegisterModel
from model.chat_catalog_screen_model import ChatCatalogModel

from model.data.singletons import Singletons
from model.model_interface import ModelInterface


class Model(ModelInterface):
    _login_model: LoginModel
    _chat_model: ChatModel
    _chat_catalog_model: ChatCatalogModel
    _register_model: RegisterModel

    @property
    def login_model(self):
        return self._login_model

    @property
    def chat_model(self):
        return self._chat_model

    @property
    def chat_catalog_model(self):
        return self._chat_catalog_model

    @property
    def register_model(self):
        return self._register_model

    def __init__(self):
        Singletons._set_model(self)

        self._login_model = LoginModel()
        self._chat_model = ChatModel()
        self._register_model = RegisterModel()
        self._chat_catalog_model = ChatCatalogModel()
        pass

    def get_model(self):
        return self
