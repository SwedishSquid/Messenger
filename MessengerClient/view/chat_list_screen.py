from kivymd.uix.screen import Screen

from utility import screen_names

from kivymd.uix.boxlayout import MDBoxLayout


from kivy.lang import Builder

# region Constants
chat_list_widget_id = 'clw'
# endregion


markdown_str = f"""
<ChatListLayout>:
    data: {chat_list_widget_id}.data
    
    Button:
        text: update
        on_release: root.on_update_button(root.data)
    
    ChatListWidget:
        id: {chat_list_widget_id}
"""

Builder.load_string(markdown_str)


class ChatListScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.chat_list_screen_name
        super().__init__(**kw)
        box_layout = ChatListLayout()
        self.set_data = box_layout.ids[chat_list_widget_id].set_data
        self.add_widget(box_layout)
        pass

    def _on_update_button(self):
        # this will not work. 100%
        pass

    def get(self):
        pass
    pass


class ChatListLayout(MDBoxLayout):
    def __init__(self, on_update_button, **kw):
        super().__init__(**kw)
        self.on_update_button = on_update_button
        pass
    pass
