from kivy.uix.screenmanager import Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


from kivy.uix.screenmanager import ScreenManager
import helpers.screen_names as screen_names


class InitialScreen(Screen):
    def __init__(self, sm: ScreenManager, **kw):
        self.name = screen_names.initial_screen_name
        self.sm = sm
        super().__init__(**kw)
        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=40,
            orientation='vertical',
        )
        main_layout.add_widget(self.get_rickroll())
        button = Button(
            text='next screen',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._on_next_screen_button,
        )

        button_layout = BoxLayout(
            spacing=40,
        )
        button_layout.add_widget(button)
        to_messenger_button = Button(
            text='to messenger',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._on_to_messanger_button,
        )
        button_layout.add_widget(to_messenger_button)

        main_layout.add_widget(button_layout)
        self.add_widget(main_layout)
        pass

    def get_rickroll(self):
        return AsyncImage(
            anim_delay=0.04,
            source='assets/rickroll-roll.zip',
        )

    def _on_next_screen_button(self, instance):
        self.sm.current = screen_names.text_screen_name

    def _on_to_messanger_button(self, instance):
        self.sm.current = screen_names.chat_screen_name
