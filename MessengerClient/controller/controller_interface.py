import abc
from abc import ABC
from controller.chat.chat_screen_controller_interface import ChatScreenControllerInterface


class ControllerInterface(ABC):
    chat_controller: ChatScreenControllerInterface

    @abc.abstractmethod
    def get_chat_controller(self):
        return self.chat_controller

    @abc.abstractmethod
    def get_chat_list_controller(self):
        pass
    pass
