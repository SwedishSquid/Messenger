from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class TestWidget(Widget):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 30
        # https://kivy.org/doc/stable/api-kivy.graphics.html
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(size=(50, 50))