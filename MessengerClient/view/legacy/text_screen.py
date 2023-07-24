from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import utility.screen_names as screen_names


class TextScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.text_screen_name
        super().__init__(**kw)

        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=40,
            orientation='vertical',
        )
        self.text_input = TextInput(
            readonly=True, halign='right', font_size=55
        )
        main_layout.add_widget(self.text_input)
        buttons = BoxLayout(
            size_hint=(1, .5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            spacing=70,
        )
        button_next = Button(
            text='next',
            on_press=self._on_next_pressed,
        )
        button_back = Button(
            text='back',
            on_press=self._on_back_pressed,
        )
        buttons.add_widget(button_back)
        buttons.add_widget(button_next)
        main_layout.add_widget(buttons)

        next_screen_button = Button(
            text='next screen',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._on_next_screen_button,
        )
        main_layout.add_widget(next_screen_button)
        self.add_widget(main_layout)
        pass

    def _on_next_pressed(self, instance):
        text = on_next_text_button()
        self._load_text(text)
        pass

    def _on_back_pressed(self, instance):
        text = on_previous_text_button()
        self._load_text(text)
        pass

    def _load_text(self, text):
        self.text_input.text = text
        pass

    def _on_next_screen_button(self, instance):
        on_next_screen_button_action()
        pass


def on_next_screen_button_action():
    pass


def on_next_text_button():
    pass


def on_previous_text_button():
    pass
