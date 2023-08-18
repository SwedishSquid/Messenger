from model.objects.chat_source import ChatSource
from model.objects.message_sources.message_source import MessageSource
from model.objects.chat_sources.not_loaded_chat_source import NotLoadedChatSource
from model.objects.message_sources.not_loaded_message_source import NotLoadedMessageSource
from model.objects.chat_info import ChatInfo


from model.objects.chat_sources.fake_chat_source import FakeChatSource
from model.objects.message_sources.fake_message_source import FakeMessageSource
from model.objects.message_sources.cat_message_source import CatMessageSource

class SourceManager:
    _chat_source: ChatSource | None = None

    @property
    def chat_source(self):
        if self._chat_source is None:
            return self._chat_source_not_loaded
        return self._chat_source

    _message_source: MessageSource | None = None

    @property
    def message_source(self):
        if self._message_source is None:
            return self._message_source_not_loaded
        return self._message_source

    def __init__(self):
        self._chat_source_not_loaded = NotLoadedChatSource()
        self._message_source_not_loaded = NotLoadedMessageSource()

        self._chat_source = FakeChatSource()

        # dictionary is temporary
        self._message_sources_dict = {
            'fakeChatId': FakeMessageSource(),
            'catChatId': CatMessageSource(),
            }
        pass

    def get_chat_source(self):
        return self.chat_source

    def get_message_source(self):
        return self.message_source

    def set_chat_to(self, chat_info: ChatInfo):
        id = chat_info.chat_id
        if id in self._message_sources_dict:
            self._message_source = self._message_sources_dict[id]
        else:
            self._message_source = None
        pass

    pass
