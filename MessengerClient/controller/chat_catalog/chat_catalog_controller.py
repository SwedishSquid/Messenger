from controller.chat_catalog.chat_catalog_controller_interface import ChatCatalogControllerInterface
from model.chat_catalog_screen_model import ChatCatalogModel
from view.chat_catalog_screen import ChatCatalogScreen
from model.objects.chat_info import ChatInfo


class ChatCatalogController(ChatCatalogControllerInterface):
    def __init__(self, catalog_model: ChatCatalogModel, catalog_screen: ChatCatalogScreen):
        self.catalog_model = catalog_model
        self.catalog_screen = catalog_screen
        pass

    def get_data(self):
        return self.catalog_screen.get_data()

    def set_data(self, new_data):
        self.catalog_screen.set_data(new_data)
        pass

    def set_chat_info(self, infos: list[ChatInfo]):
        self.catalog_screen.set_chat_info(infos)
        pass

    def on_load_button(self):
        self.catalog_model.on_load_button()
        pass

    def on_chat_nameplate(self, chat_info: ChatInfo):
        self.catalog_model.on_chat_nameplate(chat_info)
        pass
