from model.data.singletons import Singletons
from model.objects.chat_source import ChatSource
from model.objects.chat_sources.not_loaded_chat_source import NotLoadedChatSource
from model.objects.chat_sources.fake_chat_source import FakeChatSource
from model.objects.chat_info import ChatInfo


class ChatCatalogModel:
    source: ChatSource

    def __init__(self, chat_source: ChatSource = None):
        if chat_source is None:
            chat_source = FakeChatSource()
        self.source = chat_source
        pass

    def on_load_button(self):
        print('update_pressed')
        Singletons.get_controller().get_chat_catalog_controller().set_chat_info(
            self.source.get_all()
        )
        Singletons.get_controller().get_chat_catalog_controller()
        pass

    def on_chat_nameplate(self, chat_info: ChatInfo):
        print(chat_info.chat_id)
        pass
    pass
