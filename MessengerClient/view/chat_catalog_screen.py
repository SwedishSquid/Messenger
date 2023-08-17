from kivymd.uix.screen import Screen

from utility import screen_names
from model.data.singletons import Singletons
from model.objects.chat_info import ChatInfo

from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.button import MDRectangleFlatButton


from kivy.lang import Builder

# region Constants
chat_catalog_widget_id = 'clw'
load_button_id = 'load_button_id'
center = {'center_x': 0.5, 'center_y': 0.5}
# endregion


markdown_str = f"""
#:import ChatCatalogWidget view.custom_widgets.chat_catalog_widget.ChatCatalogWidget
<ChatCatalogLayout>:
    #data: {chat_catalog_widget_id}.data
    orientation: 'vertical'
    
    MDRectangleFlatButton:
        id: {load_button_id}
        text: 'update'
        pos_hint: {center}
        adaptive_size: True
    
    ChatCatalogWidget:
        id: {chat_catalog_widget_id}
"""

Builder.load_string(markdown_str)


class ChatCatalogScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.chat_list_screen_name
        super().__init__(**kw)
        self.layout = ChatCatalogLayout()

        self.layout.ids[load_button_id].on_release = self._on_load_button

        self.add_widget(self.layout)
        pass

    def _on_load_button(self):
        Singletons.get_controller().get_chat_catalog_controller().on_load_button()
        pass

    def get_data(self):
        return self.layout.ids[chat_catalog_widget_id].data

    def set_data(self, new_data):
        # self.layout.ids[chat_catalog_widget_id].data = new_data\
        data = self.get_data()
        for x in range(len(data)):
            data.pop()
        for x in new_data:
            data.append(x)
        pass

    def set_chat_info(self, infos: list[ChatInfo]):
        new_data = [self._make_data_out_of_chat_info(i) for i in infos]
        self.set_data(new_data)
        pass

    def _make_data_out_of_chat_info(self, info: ChatInfo):
        return {'type': info.chat_type,
                'name': info.chat_name,
                'on_release': self._make_on_chat_nameplate(info)}
    pass

    def _make_on_chat_nameplate(self, chat_info: ChatInfo):
        return lambda: Singletons.get_controller().get_chat_catalog_controller().on_chat_nameplate(chat_info)


class ChatCatalogLayout(MDBoxLayout):
    pass
