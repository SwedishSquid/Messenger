from kivymd.uix.screenmanager import ScreenManager

from view.chat_screen import ChatScreen
from view.legacy.text_screen import TextScreen
from view.legacy.image_screen import ImageScreen
from view.legacy.initial_screen import InitialScreen
from view.login_screen import LoginScreen
from view.legacy.test_screen import TestScreen
from view.chat_list_screen import ChatListScreen

from utility import screen_names

from model.data import singletons


class ScreenChanger(ScreenManager):
    login_screen: LoginScreen
    chat_screen: ChatScreen

    def __init__(self, **kw):
        super().__init__(**kw)

        singletons.get_screen_changer = self.get_screen_changer

        self.text_screen = TextScreen()
        self.chat_screen = ChatScreen()
        self.initial_screen = InitialScreen()
        self.image_screen = ImageScreen()
        self.login_screen = LoginScreen()
        self.test_screen = TestScreen()
        self.chat_list_screen = ChatListScreen()

        self.add_widget(self.initial_screen)
        self.add_widget(self.text_screen)
        self.add_widget(self.image_screen)
        self.add_widget(self.chat_screen)
        self.add_widget(self.login_screen)
        self.add_widget(self.test_screen)
        self.add_widget(self.chat_list_screen)

        pass

    def goto_initial_screen(self):
        self.current = screen_names.initial_screen_name
        pass

    def goto_test_screen(self):
        self.current = screen_names.test_screen_name
        pass

    def goto_text_screen(self):
        self.current = screen_names.text_screen_name
        pass

    def goto_image_screen(self):
        self.current = screen_names.image_screen_name
        pass

    def goto_chat_screen(self):
        self.current = screen_names.chat_screen_name
        pass

    def goto_login_screen(self):
        self.current = screen_names.login_screen_name
        pass

    def goto_screen(self, name):
        self.current = name
        pass

    def get_screen_changer(self):
        return self
