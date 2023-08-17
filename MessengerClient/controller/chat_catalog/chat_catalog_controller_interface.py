import abc
from model.objects.chat_info import ChatInfo


class ChatCatalogControllerInterface(abc.ABC):
    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def set_data(self, new_data):
        pass

    @abc.abstractmethod
    def set_chat_info(self, infos: list[ChatInfo]):
        pass

    @abc.abstractmethod
    def on_load_button(self):
        pass

    @abc.abstractmethod
    def on_chat_nameplate(self, chat_info: ChatInfo):
        pass
