from utility.screen_changer import ScreenChanger
from utility.singleton_behaviour import SingletonBehaviour

from model.model_main import Model
from model.data import singletons
from model.data.singletons import Singletons

from controller.controller_interface import ControllerInterface
from controller.chat.chat_screen_controller import ChatScreenController
from controller.chat.chat_screen_controller_interface import ChatScreenControllerInterface


class Controller(SingletonBehaviour, ControllerInterface):
    def __init__(self):
        # singletons.get_controller = self.get_instance
        Singletons._set_controller(self)

        self.chat_controller: ChatScreenControllerInterface \
            = ChatScreenController(Singletons.get_model().chat_model,
                                   Singletons.get_screen_changer().chat_screen)

        scrChanger: ScreenChanger = Singletons.get_screen_changer()
        modelInst: Model = Singletons.get_model()

        loginModel = modelInst.login_model
        loginScr = scrChanger.login_screen
        loginScr.on_username_entered = loginModel.on_username_entered
        loginScr.on_password_entered = loginModel.on_password_entered
        loginScr.on_submit_button_pressed = loginModel.on_submit_button_pressed

        chatModel = modelInst.chat_model
        chatScr = scrChanger.chat_screen
        # chatScr.submit = chatModel.submit
        # chatScr.on_back_button = chatModel.on_back_button_action
        # chatScr.load_data = chatModel.load_data
        # chatModel.get_data = chatScr.get_data
        pass

    def get_chat_controller(self):
        return self.chat_controller

    def get_chat_list_controller(self):
        pass
