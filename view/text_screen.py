from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import requests

from kivy.uix.screenmanager import ScreenManager
import utility.screen_names as screen_names


class TextScreen(Screen):
    _common_url = 'https://swedishsquid.github.io/MyWebPage/messengerTest/'
    _file_names = ['text0.html', 'text1.html', 'text2.html', 'text3.html', 'text4.html', 'text5.html', 'text6.html', 'text7.html', ]

    def __init__(self, sm: ScreenManager, **kw):
        self.name = screen_names.text_screen_name
        self.sm = sm
        super().__init__(**kw)

        self._file_num = 0

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
        self._file_num = (self._file_num + 1) % len(self._file_names)
        self._load_text()
        pass

    def _on_back_pressed(self, instance):
        self._file_num = (self._file_num - 1) % len(self._file_names)
        self._load_text()
        pass

    def _load_text(self):
        url = self._common_url + self._file_names[self._file_num]
        try:
            r = requests.get(url)
            self.text_input.text = r.text
        except requests.RequestException as e:
            self.text_input.text = str(e) # 'no internet found :D'
        pass

    def _on_next_screen_button(self, instance):
        self.sm.current = screen_names.image_screen_name
