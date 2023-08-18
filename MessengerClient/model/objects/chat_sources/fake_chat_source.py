from model.objects.chat_source import ChatSource
from model.objects.chat_info import ChatInfo


class FakeChatSource(ChatSource):
    def get_all(self):
        return [
            ChatInfo('fakeChatId', 'sometype', 'somename'),
            ChatInfo('catChatId', 'cat', 'mew'),
            ChatInfo('exceptionChatID', 'exceptionMaker',
                     'this is a chat nameplate for non-existing chat')
        ]
