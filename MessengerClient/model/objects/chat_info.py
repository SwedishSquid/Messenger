class ChatInfo:
    chat_type: str
    chat_name: str

    def __init__(self, chat_id: str, chat_type=None, chat_name=None):
        self.chat_id = chat_id

        self.chat_type = chat_type
        self.chat_name = chat_name
        pass
    pass
