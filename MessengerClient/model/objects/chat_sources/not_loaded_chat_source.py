from model.objects.chat_info import ChatInfo
from model.objects.chat_source import ChatSource


class NotLoadedChatSource(ChatSource):
    def get_all(self) -> list[ChatInfo]:
        return []
