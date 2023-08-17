from utility.singleton_behaviour import SingletonBehaviour

from model.data.singletons import Singletons

from controller.controller_interface import ControllerInterface
from controller.chat.chat_screen_controller import ChatScreenController
from controller.chat.chat_screen_controller_interface import ChatScreenControllerInterface

from controller.login_screen.login_screen_controller_interface import LoginScreenControllerInterface
from controller.login_screen.login_screen_controller import LoginScreenController

from controller.register_screen.register_screen_controller import RegisterScreenController
from controller.register_screen.register_screen_controller_interface import RegisterScreenControllerInterface

from controller.chat_catalog.chat_catalog_controller import ChatCatalogController
from controller.chat_catalog.chat_catalog_controller_interface import ChatCatalogControllerInterface


class Controller(SingletonBehaviour, ControllerInterface):
    def __init__(self):
        Singletons._set_controller(self)

        self._chat_controller: ChatScreenControllerInterface \
            = ChatScreenController(Singletons.get_model().chat_model,
                                   Singletons.get_screen_changer().chat_screen)

        self._login_controller: LoginScreenControllerInterface\
            = LoginScreenController(Singletons.get_model().login_model,
                                    Singletons.get_screen_changer().login_screen)

        self._register_controller: RegisterScreenControllerInterface\
            = RegisterScreenController(Singletons.get_model().register_model,
                                       Singletons.get_screen_changer().register_screen)

        self._chat_catalog_controller: ChatCatalogControllerInterface\
            = ChatCatalogController(Singletons.get_model().chat_catalog_model,
                                    Singletons.get_screen_changer().chat_catalog_screen)
        pass
