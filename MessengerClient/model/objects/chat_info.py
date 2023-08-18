class ChatInfo:
    def __init__(self, chat_id: str, chat_type=None, chat_name=None,
                 clickable=True):
        self.chat_id = chat_id
        self.clickable = clickable

        self.chat_type = chat_type
        self.chat_name = chat_name
        pass
    pass
