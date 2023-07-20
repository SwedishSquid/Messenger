from controller.legacy import image_screen_controller, \
    initial_screen_controller, test_screen_controller, text_screen_controller

from model.data import singletons
from utility.screen_changer import ScreenChanger
from model.model_main import Model


def init():
    # legacy
    initial_screen_controller.init()
    image_screen_controller.init()
    text_screen_controller.init()
    test_screen_controller.init()
    # legacy

    scrChanger: ScreenChanger = singletons.get_screen_changer()
    modelInst: Model = singletons.get_model()

    loginModel = modelInst.login_model
    loginScr = scrChanger.login_screen
    loginScr.on_username_entered = loginModel.on_username_entered
    loginScr.on_password_entered = loginModel.on_password_entered
    loginScr.on_submit_button_pressed = loginModel.on_submit_button_pressed

    chatModel = modelInst.chat_model
    chatScr = scrChanger.chat_screen
    chatScr.submit = chatModel.submit
    chatScr.on_back_button = chatModel.on_back_button_action
    pass
