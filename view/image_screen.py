from kivy.uix.screenmanager import Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import utility.screen_names as screen_names


class ImageScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.image_screen_name
        super().__init__(**kw)
        self._file_num = -1
        main_layout = BoxLayout(
            padding=[20, 20, 20, 20],
            spacing=40,
            orientation='vertical',
        )
        self.img = AsyncImage(
            source='fish_icon.png'
        )
        main_layout.add_widget(self.img)
        change_img_button = Button(
            text='change image',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._change_image
        )
        main_layout.add_widget(change_img_button)
        next_screen_button = Button(
            text='next screen',
            size_hint=(.5, .2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self._on_next_screen_button,
        )
        main_layout.add_widget(next_screen_button)
        self.add_widget(main_layout)

    def _change_image(self, instance):
        source = get_next_image()
        try:
            self.img.source = source
            self.img.reload()
        except Exception as e:  # too laizy to search for kivy-image-exception
            print(e)
        pass

    def _on_next_screen_button(self, instance):
        on_next_screen_button()
        pass


def on_next_screen_button():
    pass


def get_next_image():
    pass
