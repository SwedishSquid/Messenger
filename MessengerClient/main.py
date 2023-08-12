from kivymd.app import MDApp

from controller import controller_main
from utility.screen_changer import ScreenChanger
from model.model_main import Model

from kivy.core.window import Window
from utility import screen_names


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        Window.softinput_mode = 'below_target'
        self.screen_changer = ScreenChanger()
        self.app_model = Model()
        self.controller = controller_main.Controller()

        self.screen_changer.goto_screen(screen_names.login_screen_name)
        pass

    def build(self):
        self.title = "fishenger"
        self.icon = 'fish_icon.png'
        return self.screen_changer


if __name__ == '__main__':
    app = MainApp()
    app.run()
