from kivy.uix.screenmanager import Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import screens.screen_changer as screen_changer


class InitialScreen(Screen):
    def __init__(self, **kw):
        self.name = 'initial_screen'
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
            on_press=screen_changer.instance.goto_text_screen
        )
        main_layout.add_widget(button)
        self.add_widget(main_layout)
        pass

    def get_rickroll(self):
        return AsyncImage(
            anim_delay=0.04,
            source='assets/rickroll-roll.zip',
        )
