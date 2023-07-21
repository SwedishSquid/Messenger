from kivy.lang.builder import Builder




from kivymd.uix.recycleview import MDRecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd.uix.boxlayout import MDBoxLayout


# region Constants
# center = {'center_x': 0.5, 'center_y': 0.5}
# endregion


markdown_str = f"""
#:import Window kivy.core.window.Window
<ChatWidget>:
    viewclass: 'MessageStandard'
    id: rv
    
    RecycleBoxLayout:
        spacing: dp(10)
        default_size: None, None
        default_size_hint: None, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

<MessageStandard>:
    id: ms
    text: "some_string and Lorem ipsum sgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddassgdfhsjdfsjhgashjklddas"
    orientation: 'vertical'
    size_hint: (None, None)
    height: main_label.height
    width: 500 if Window.width > 625 else Window.width * 0.8
    md_bg_color: (1, 0, 1, 0.3)
    
    MDLabel:
        id: main_label
        adaptive_size: True
        text: ms.text
        size_hint_x: None
        width: ms.width
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
        self.data = [{} for x in range(111)]
        pass

    pass


class MessageStandard(RecycleDataViewBehavior, MDBoxLayout):
    pass
