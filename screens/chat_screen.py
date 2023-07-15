from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager
import helpers.screen_names as screen_names

class ChatScreen(Screen):
    def __init__(self, sm: ScreenManager, **kw):
        self.name = screen_names.chat_screen_name
        self.sm = sm
        super().__init__(**kw)

        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=30,
            orientation='vertical',
        )

        back_button = Button(
            text='<-- go back',
            on_press=self._on_back_button_pressed
        )

    def _on_back_button_pressed(self, instance):
        self.sm.current = screen_names.initial_screen_name
