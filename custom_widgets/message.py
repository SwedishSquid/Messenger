from kivy.uix.label import Label


class TextMessage(Label):
    def __init__(self, user_nickname: str, text: str, **kwargs):
        super().__init__(**kwargs)
        self.text = f'[[{user_nickname}]]\n\r>>>{text}'
