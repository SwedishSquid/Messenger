from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.scrollview import ScrollView

from kivy.uix.screenmanager import ScreenManager
import helpers.screen_names as screen_names

from kivy.uix.textinput import TextInput

from custom_widgets.message import TextMessage

from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label


class ChatScreen(Screen):
    def __init__(self, sm: ScreenManager, **kw):
        self.name = screen_names.chat_screen_name
        self.sm = sm
        super().__init__(**kw)

        main_layout = BoxLayout(
            padding=[0, 0, 0, 0],
            spacing=30,
            orientation='vertical',
        )

        back_button = Button(
            size_hint=(1, .1),
            text='<--   go back',
            on_press=self._on_back_button_pressed
        )
        main_layout.add_widget(back_button)

        scroll_view = ScrollView(
            size_hint=(1, 1)
        )

        # label_text = Label(
        #     text="hahahah",
        #     color=(1, 1, 0, 1),
        # )
        # scroll_view.add_widget(label_text)

        # self.messages_layout = GridLayout(
        #     #padding=[0, 0, 0, 0],
        #     spacing=30,
        #     row_default_height=30,
        #     row_force_default=30,
        #     cols=1,
        #     size_hint_x=1,
        #     size_hint_y=None,
        # )

        self.messages = Label(
            size_hint_x=1,
            size_hint_y=None,
        )

        main_layout.add_widget(scroll_view)

        scroll_view.add_widget(self.messages)

        main_layout.add_widget(self._make_text_input_bar())
        self.add_widget(main_layout)

    def _on_back_button_pressed(self, instance):
        self.sm.current = screen_names.initial_screen_name
        pass

    # may be useful to subclass TextInput and customize
    # see for example https://stackoverflow.com/questions/12037379/tab-enter-and-other-keystrokes-handling-in-kivys-textinput-widgets
    def _make_text_input_bar(self):
        def _on_enter(instance):
            self.send_message()
            pass
        publish_button = Button(
            size_hint=(.1, .2),
            text='>',
            font_size=26,
            color=(1, 1, 0),
            on_release=self._on_publish_button_release,
            background_color=(1, 1, 0, 1),
        )
        self.text_input_field = TextInput(
            size_hint=(1, .2),
            readonly=False,
            # focus=True, # this thing stops me from writing in textbox
            multiline=False,
            on_text_validate=_on_enter,
            font_size=20
        )
        box_layout = BoxLayout()
        box_layout.add_widget(self.text_input_field)
        box_layout.add_widget(publish_button)
        return box_layout

    def send_message(self):
        text = self.text_input_field.text
        print(f'enter pressed, printed: {text}')
        self._add_message()
        self.text_input_field.text = ''
        # works only for button sent message
        self.text_input_field.focus = True  # better make custom TextInput
        pass

    def _on_publish_button_release(self, instance):
        self.send_message()
        pass

    def _add_message(self):
        user = 'standard user'
        text = self.text_input_field.text
        #self.messages_layout.add_widget(TextMessage(user, text))
        #self.sv.add_widget(TextMessage(user, text))
        self.messages.text += f'[[{user}]]\n\r>>>{text}\n\r'
