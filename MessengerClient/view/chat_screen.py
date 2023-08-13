from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

import utility.screen_names as screen_names
from assets.strings import lorem_ipsum
from kivy.properties import ListProperty

from model.data.singletons import Singletons


markdown_str = f"""
#:import ChatWidget view.custom_widgets.chat_widget.ChatWidget
#:import Window kivy.core.window.Window
<ChatScreenLayout>:
    orientation: 'vertical'
    data: chat.data
    padding: (10, 0, 10, 0)
    
    MDBoxLayout:
        id: top_panel
        size_hint_y: None
        height: self.minimum_height
        spacing: dp(10)
        
        Button:
            id: back_button
            text: 'go back'
            on_release: root.on_back_button()
        
        MDRoundFlatButton:
            id: load_all
            text: 'load all'
            on_release: root.load_data(root.data)
            
        # MDRoundFlatButton:
        #     id: load_bottom
        #     text: 'load at bottom'
        
    
    ChatWidget:
        id: chat
    
    MDBoxLayout:
        id: input_wrapper
        size_hint_y: None
        height: self.minimum_height
        
        MDTextField:
            id: input
            multiline: False
            on_text_validate: root.on_send_message()
        
        Button:
            size_hint_x: None
            width: 50
            on_release: root.on_send_message()
    
    MDBoxLayout:
        size_hint_y: None
        height: Window.keyboard_height
"""

Builder.load_string(markdown_str)


class ChatScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.chat_screen_name
        super().__init__(**kw)

        self.layout = ChatScreenLayout(self._on_send_message, self._load_data, self._on_back_button)
        chat = self.layout.ids.chat
        chat.data.append({'user': 'me', 'text': 'this chat is fake, but a long one, to load more realistic one press button at the top-right corner', 'time': 'i have to go now'})
        for x in range(100):
            chat.data.append({'user': 'you`d better not', 'text': lorem_ipsum, 'time': 'this is time, not a bear'})
        self.text_input = self.layout.ids.input
        self.add_widget(self.layout)
        pass

    def _on_back_button(self):
        Singletons.get_controller().get_chat_controller().on_back_button()
        pass

    def _on_send_message(self):
        # message_text = self.text_input.text
        # if message_text != '':
        #     self.submit(message_text)
        #     self.text_input.text = ''
        Singletons.get_controller().get_chat_controller().on_submit()
        pass

    def _load_data(self, data, **kwargs):
        Singletons.get_controller().get_chat_controller().on_load_button()
        pass

    def get_typed_message(self):
        return self.text_input.text

    def get_data(self):
        return self.layout.data


class ChatScreenLayout(MDBoxLayout):
    data: ListProperty

    def __init__(self, on_send_message, load_data, on_back_button, **kw):
        super().__init__(**kw)
        self.on_send_message = on_send_message
        self.load_data = load_data
        self.on_back_button = on_back_button
        pass
    pass
