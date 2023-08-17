from utility.singleton_behaviour import SingletonBehaviour

from model.data.singletons import Singletons

from controller.chat.chat_screen_controller import ChatScreenController

from controller.login_screen.login_screen_controller import LoginScreenController

from controller.register_screen.register_screen_controller import RegisterScreenController

from controller.chat_catalog.chat_catalog_controller import ChatCatalogController


class Controller(SingletonBehaviour):
    _chat_controller: 'ChatScreenController'
    _login_controller: 'LoginScreenController'
    _register_controller: 'RegisterScreenController'
    _chat_catalog_controller: 'ChatCatalogController'

    def __init__(self):
        Singletons._set_controller(self)

        self._chat_controller \
            = ChatScreenController(Singletons.get_model().chat_model,
                                   Singletons.get_screen_changer().chat_screen)

        self._login_controller \
            = LoginScreenController(Singletons.get_model().login_model,
                                    Singletons.get_screen_changer().login_screen)

        self._register_controller \
            = RegisterScreenController(Singletons.get_model().register_model,
                                       Singletons.get_screen_changer().register_screen)

        self._chat_catalog_controller\
            = ChatCatalogController(Singletons.get_model().chat_catalog_model,
                                    Singletons.get_screen_changer().chat_catalog_screen)
        pass

    def get_chat_controller(self):
        return self._chat_controller

    def get_chat_catalog_controller(self):
        return self._chat_catalog_controller

    def get_login_controller(self):
        return self._login_controller

    def get_register_controller(self):
        return self._register_controller
