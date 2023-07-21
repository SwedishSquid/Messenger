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

        #self.screen_changer.goto_chat_screen()
        pass

    def build(self):
        self.title = "fishenger"
        self.icon = 'fish_icon.png'
        return self.screen_changer

if __name__ == '__main__':
    app = MainApp()
    app.run()
