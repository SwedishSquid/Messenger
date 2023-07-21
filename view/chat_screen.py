from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout



import utility.screen_names as screen_names
from view.custom_widgets.chat_widget import ChatWidget
from assets.strings import lorem_ipsum





# center = {'center_x': 0.5, 'center_y': 0.5}


markdown_str = f"""

"""

Builder.load_string(markdown_str)


class ChatScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.chat_screen_name
        super().__init__(**kw)
        chat = ChatWidget()
        chat.data = [{'text': lorem_ipsum} for x in range(111)]
        layout = ChatScreenLayout()
        layout.add_widget(chat)
        self.add_widget(layout)
        pass

    def _on_back_button_pressed(self, instance):
        self.on_back_button()
        pass

    # may be useful to subclass TextInput and customize
    # see for example https://stackoverflow.com/questions/12037379/tab-enter-and-other-keystrokes-handling-in-kivys-textinput-widgets
    def _make_text_input_bar(self):
        # def _on_enter(instance):
        #     self.send_message()
        #     pass
        # publish_button = Button(
        #     size_hint=(.1, .2),
        #     text='>',
        #     font_size=26,
        #     color=(1, 1, 0),
        #     on_release=self._on_publish_button_release,
        #     background_color=(1, 1, 0, 1),
        # )
        # self.text_input_field = TextInput(
        #     size_hint=(1, .2),
        #     readonly=False,
        #     # focus=True, # this thing stops me from writing in textbox
        #     multiline=False,
        #     on_text_validate=_on_enter,
        #     font_size=20
        # )
        # box_layout = BoxLayout()
        # box_layout.add_widget(self.text_input_field)
        # box_layout.add_widget(publish_button)
        # return box_layout
        pass

    def send_message(self):
        # text = self.text_input_field.text
        # self.submit(text)  # all other interaction should be done in model
        # self._add_message()
        # self.text_input_field.text = ''
        # # works only for button sent message
        # self.text_input_field.focus = True  # better make custom TextInput
        pass

    def _on_publish_button_release(self, instance):
        self.send_message()
        pass

    # override in controller
    @staticmethod
    def on_back_button():
        pass

    @staticmethod
    def submit(message: str):
        pass


class ChatScreenLayout(MDBoxLayout):
    pass
