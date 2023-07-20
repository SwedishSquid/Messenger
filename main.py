from kivymd.app import MDApp

from controller import controller_main
from utility.screen_changer import ScreenChanger
from model.model_main import Model

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.screen_changer = ScreenChanger()
        self.app_model = Model()
        controller_main.init()
        pass

    def build(self):
        self.title = "fishenger"
        self.icon = 'fish_icon.png'
        # self.set_screens(self.screen_manager)
        return self.screen_changer

    # def set_screens(self, sm: ScreenManager):
    #     self.text_screen = TextScreen(sm)
    #     self.chat_screen = ChatScreen(sm)
    #     self.initial_screen = InitialScreen(sm)
    #     self.image_screen = ImageScreen(sm)
    #     self.login_screen = LoginScreen(sm)
    #     self.test_screen = TestScreen(sm)
    #
    #     sm.add_widget(self.initial_screen)
    #     sm.add_widget(self.text_screen)
    #     sm.add_widget(self.image_screen)
    #     sm.add_widget(self.chat_screen)
    #     sm.add_widget(self.login_screen)
    #     sm.add_widget(self.test_screen)
    #     pass


if __name__ == '__main__':
    app = MainApp()
    app.run()
