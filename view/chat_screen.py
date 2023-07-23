from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.textfield.textfield import MDTextField

import utility.screen_names as screen_names
from view.custom_widgets.chat_widget import ChatWidget
from assets.strings import lorem_ipsum
from kivy.properties import ListProperty

from kivy.core.window import Window


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
        self.on_back_button()
        pass

    def _on_send_message(self):
        message_text = self.text_input.text
        if message_text != '':
            self.submit(message_text)
            self.text_input.text = ''
        pass

    def _load_data(self, data, **kwargs):
        self.load_data(data, **kwargs)
        pass

    # override in controller
    # this is for view -> model communication
    @staticmethod
    def on_back_button():
        print('connection fail with chat_screen_model method on_back_button')
        pass

    @staticmethod
    def submit(message: str):
        print('connection fail with chat_screen_model method submit')
        pass

    @staticmethod
    def load_data(data, **kwargs):
        print('connection fail with chat_screen_model method load_data')
        pass

    # this is for model -> view communication
    def get_data(self):
        print('hahjahjha')
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


# class ChatTopPanel(Button):
#     def on_release(self):
#         print('please go back')
#         pass
#     pass


# may be useful to subclass TextInput and customize
# see for example https://stackoverflow.com/questions/12037379/tab-enter-and-other-keystrokes-handling-in-kivys-textinput-widgets
class ChatInputField(MDBoxLayout):
    pass
