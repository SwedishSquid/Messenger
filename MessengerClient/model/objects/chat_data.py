

class ChatData:
    def __init__(self, chat_type: str, name: str, last_message: str = None, not_read: int = None):
        self.chat_type = chat_type
        self.name = name
        self.last_message: str = last_message
        self.not_read: int = 0 if not_read is None else not_read
        pass
    pass
