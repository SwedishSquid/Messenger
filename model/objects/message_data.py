

class MessageData:
    def __init__(self, username: str = None, text: str = None, time: str = None):
        self.username = 'noname' if username is None else username
        self.text = '' if text is None else text
        self.time = 'before christ' if time is None else time
        pass
    pass
