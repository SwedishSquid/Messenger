from model.objects.chat_info import ChatInfo
from model.objects.chat_source import ChatSource


class NotLoadedChatSource(ChatSource):
    def get_all(self) -> list[ChatInfo]:
        return [ChatInfo(chat_id='not_loaded_chat', chat_type='not_loaded',
                         chat_name='please reload', clickable=False)]
