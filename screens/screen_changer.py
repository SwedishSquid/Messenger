from kivy.uix.screenmanager import ScreenManager

from screens.text_screen import TextScreen
from screens.initial_screen import InitialScreen
from screens.image_screen import ImageScreen
from screens.chat_screen import ChatScreen


class ScreenChanger(ScreenManager):
    something = None
    def __init__(self, **kw):
        super().__init__(**kw)
        self.text_screen = TextScreen()
        self.chat_screen = ChatScreen()
        self.initial_screen = InitialScreen()
        self.image_screen = ImageScreen()

        self.add_widget(self.initial_screen)
        self.add_widget(self.text_screen)
        self.add_widget(self.image_screen)
        self.add_widget(self.chat_screen)

        global instance
        instance = self
        pass

    def goto_initial_screen(self):
        self.current = self.initial_screen.name
        pass

    def goto_text_screen(self):
        self.current = self.text_screen.name
        pass

    def goto_image_screen(self):
        self.current = self.image_screen.name
        pass

    def goto_chat_screen(self):
        self.current = self.chat_screen.name


# singleton
instance: ScreenChanger
