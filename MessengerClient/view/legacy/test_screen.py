from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from utility import screen_names
from kivymd.uix.label import MDLabel

from kivy.lang import Builder

from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton

from assets import colors


center_dict = {'center_x': 0.5, 'center_y': 0.5}


# string f"" - formatted string

kv_str = f"""
<TestScreenLayout>
    
    md_bg_color: {colors.strange_color}
    
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)
    
    MDAnchorLayout:
        pos_hint: {center_dict}
        md_bg_color: (.5, .5, .5, .3)
        
        MDLabel:
            size_hint: (.5, .5)
            halign: 'center'
            md_bg_color: (.5, .5, 0, .3)
            text: "this is test screen"
            text_color: (0, 0, 0)
    
    MDAnchorLayout:
        md_bg_color: (.5, .5, .5, .3)
    
        MDRectangleFlatButton:
            # size_hint_y: 1
            # size_hint_x: 1
            id: next_button
            text: "button next"
            pos_hint: {center_dict}
"""

Builder.load_string(kv_str)


class TestScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.test_screen_name
        super().__init__(**kw)

        box = TestScreenLayout()
        # it is a way to access created by Builder widgets
        box.ids.next_button.on_release = self._on_button_release
        self.add_widget(box)
        pass

    def _on_button_release(self):
        on_next_screen_button()
        pass


class TestScreenLayout(MDBoxLayout):
    pass


def on_next_screen_button():
    pass
