import abc
from abc import ABC
from controller.chat.chat_screen_controller_interface import ChatScreenControllerInterface
from controller.login_screen.login_screen_controller_interface import LoginScreenControllerInterface
from controller.register_screen.register_screen_controller_interface import RegisterScreenControllerInterface


class ControllerInterface(ABC):
    _chat_controller: ChatScreenControllerInterface
    _login_controller: LoginScreenControllerInterface
    _register_controller: RegisterScreenControllerInterface
    _chat_catalog_controller = None

    def get_chat_controller(self):
        return self._chat_controller

    def get_chat_list_controller(self):

        pass

    def get_login_controller(self):
        return self._login_controller

    def get_register_controller(self):
        return self._register_controller
    pass
