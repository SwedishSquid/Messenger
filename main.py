from kivymd.app import MDApp

from kivymd.uix.screenmanager import ScreenManager

from view.text_screen import TextScreen
from view.initial_screen import InitialScreen
from view.image_screen import ImageScreen
from view.chat_screen import ChatScreen


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.screen_manager = ScreenManager()
        pass

    def build(self):
        self.title = "fishenger"
        self.icon = 'fish_icon.png'
        self.set_screens(self.screen_manager)
        return self.screen_manager

    def set_screens(self, sm: ScreenManager):
        self.text_screen = TextScreen(sm)
        self.chat_screen = ChatScreen(sm)
        self.initial_screen = InitialScreen(sm)
        self.image_screen = ImageScreen(sm)

        sm.add_widget(self.initial_screen)
        sm.add_widget(self.text_screen)
        sm.add_widget(self.image_screen)
        sm.add_widget(self.chat_screen)
        pass


if __name__ == '__main__':
    app = MainApp()
    app.run()
