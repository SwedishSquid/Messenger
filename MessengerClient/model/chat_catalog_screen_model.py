from model.data.singletons import Singletons
from model.objects.chat_info import ChatInfo
from utility import screen_names


class ChatCatalogModel:
    @property
    def chat_source(self):
        return Singletons.get_model().get_source_manager().get_chat_source()

    def on_load_button(self):
        print('update_pressed')
        Singletons.get_controller().get_chat_catalog_controller().set_chat_info(
            self.chat_source.get_all()
        )
        Singletons.get_controller().get_chat_catalog_controller()
        pass

    def on_chat_nameplate(self, chat_info: ChatInfo):
        Singletons.get_model().get_source_manager().set_chat_to(chat_info)
        Singletons.get_screen_changer().goto_screen(screen_names.chat_screen_name)
        pass
    pass
