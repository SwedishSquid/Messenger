from kivy.lang.builder import Builder


from kivymd.uix.recycleview import MDRecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.effects.dampedscroll import DampedScrollEffect


from assets.colors import transparent_light_gray

# region Constants
# center = {'center_x': 0.5, 'center_y': 0.5}
bg_color = transparent_light_gray
# endregion


markdown_str = f"""
#:import Window kivy.core.window.Window
<ChatWidget>:
    viewclass: 'MessageStandard'
    # id: rv
    bar_width: dp(10)
    scroll_type: ["bars", "content"]
    
    RecycleBoxLayout:
        spacing: dp(10)
        #padding: dp(100)
        default_size: None, None
        default_size_hint: None, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

<MessageStandard>:
    id: ms
    user: "standard user"
    text: "Lorem ipsum"
    time: "before christ"
    orientation: 'vertical'
    size_hint: (None, None)
    height: main_label.height + username_label.height + time_label.height
    width: 500 if Window.width > 625 else Window.width * 0.8
    # md_bg_color: (1, 0, 1, 0.3)
    # ripple_behavior: True
    md_bg_color: {bg_color}
    
    
    MDLabel:
        id: username_label
        text: ms.user
        adaptive_size: True
        size_hint_x: None
        width: ms.width
        color: "blue"
    
    MDLabel:
        id: main_label
        adaptive_size: True
        text: ms.text
        size_hint_x: None
        width: ms.width
    
    MDLabel:
        id: time_label
        text: ms.time
        adaptive_size: True
        size_hint_x: None
        width: ms.width
        color: "gray"
        halign: 'right'
"""


_initiated = False


def init_chat_widget():
    global _initiated
    if not _initiated:
        Builder.load_string(markdown_str)
        _initiated = True
        print('string loaded')
    pass


class ChatWidget(MDRecycleView):
    def __init__(self, **kw):
        init_chat_widget()  # this MUST be before super().__init__()
        super().__init__(**kw)
        pass

    pass


class MessageStandard(RecycleDataViewBehavior, MDCard):
    # def refresh_view_attrs(self, rv, index, data):
    #     pass
    pass


# class MyScrollEffect(DampedScrollEffect):
#     def on_overscroll(self, *args):
#         super().on_overscroll(self, *args)
#         print('overscroll')
#     pass
