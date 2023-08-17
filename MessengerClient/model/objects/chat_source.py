import abc
from model.objects.chat_info import ChatInfo


class ChatSource(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[ChatInfo]:
        pass
    pass
