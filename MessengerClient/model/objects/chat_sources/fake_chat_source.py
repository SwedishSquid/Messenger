from model.objects.chat_source import ChatSource
from model.objects.chat_info import ChatInfo


class FakeChatSource(ChatSource):
    def get_all(self):
        return [ChatInfo('someChatId', 'sometype', 'somename'), ChatInfo('catChatId', 'cat', 'mew')]
