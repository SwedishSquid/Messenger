from model.data import singletons
from model.objects.chat_source import ChatSource


class ChatListModel:
    source: ChatSource

    def __init__(self, chat_source: ChatSource = None):
        if chat_source is None:
            raise NotImplementedError('chat source must be specified')
        self.source = chat_source
        pass

    def on_update_button(self):
        print('update_pressed')
        pass
    pass
