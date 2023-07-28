from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.properties import ListProperty
from assets import colors

from kivy.uix.button import ButtonBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.behaviors.elevation import CommonElevationBehavior

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard


center = {'center_x': 0.5, 'center_y': 0.5}


markdown_str = f"""
<ChatListWidget>:
    id: clw
    orientation: 'vertical'
    data: []
    md_bg_color: {colors.transparent_light_gray}
    
    MDTextField:
        
    MDRecycleView:
        viewclass: 'ChatNameplate'
        id: rv
        bar_width: dp(10)
        scroll_type: ["bars", "content"]
        data: clw.data
        
        RecycleBoxLayout:
            spacing: dp(10)
            padding: dp(10)
            default_size: None, None
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            

<ChatNameplate>:
    id: cnp
    type: 'typeless'
    name: 'nameless'
    ripple_behavior: True
    padding: [10, 0, 0, 0]
    spacing: dp(10)
        
    MDLabel:
        text: cnp.type
        color: (1, 0, 0)
        adaptive_size: True
        pos_hint: {center}
            
    
    MDLabel:
        text: cnp.name
"""


_initiated = False


def init_chatlist_widget():
    global _initiated
    if not _initiated:
        Builder.load_string(markdown_str)
        _initiated = True
        print('charlist markdown str loaded')
    pass


class ChatListWidget(MDBoxLayout):
    data: ListProperty

    def __init__(self, data=None, **kw):
        init_chatlist_widget()
        super().__init__(**kw)
        if data is not None:
            self.data = data
        pass
    pass


class ChatNameplate(MDCard, ButtonBehavior):  # , RecycleDataViewBehavior):
    def on_press(self):
        print('press')
        pass

    def on_release(self):
        print('release')
        pass
    pass
