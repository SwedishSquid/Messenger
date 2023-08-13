from kivymd.uix.screenmanager import ScreenManager
from utility.screen_changer_interface import ScreenChangerInterface

from view.chat_screen import ChatScreen
from view.login_screen import LoginScreen
from view.chat_list_screen import ChatListScreen
from view.register_screen import RegisterScreen

from utility import screen_names

from model.data.singletons import Singletons


class ScreenChanger(ScreenManager, ScreenChangerInterface):
    login_screen: LoginScreen
    chat_screen: ChatScreen

    def __init__(self, **kw):
        super().__init__(**kw)

        Singletons._set_screen_changer(self)

        self.chat_screen = ChatScreen()
        self.login_screen = LoginScreen()
        # self.chat_list_screen = ChatListScreen()
        self.register_screen = RegisterScreen()

        self.add_widget(self.chat_screen)
        self.add_widget(self.login_screen)
        self.add_widget(self.register_screen)

        # self.add_widget(self.chat_list_screen)
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
