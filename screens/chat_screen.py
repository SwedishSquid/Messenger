from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import screens.screen_changer as screen_changer

class ChatScreen(Screen):
    def __init__(self, **kw):
        self.name = 'chat_screen'
        super().__init__(**kw)

        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=30,
            orientation='vertical',
        )

        back_button = Button(
            text='<-- go back',
            on_press=screen_changer.instance.goto_initial_screen()
        )
