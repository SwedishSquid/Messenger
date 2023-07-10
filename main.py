from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.text_screen import TextScreen
from screens.initial_screen import InitialScreen
from screens.image_screen import ImageScreen

sm = ScreenManager()


class MainApp(App):
    def build(self):
        self.title = "test application"
        self.icon = 'fish_icon.png'

        self.initial_screen = InitialScreen(self._on_nextscene_from_initial)
        sm.add_widget(self.initial_screen)
        self.text_screen = TextScreen(self._on_nextscene_from_text)
        sm.add_widget(self.text_screen)
        self.image_screen = ImageScreen(self._on_nextscene_from_image)
        sm.add_widget(self.image_screen)
        return sm

    def _on_nextscene_from_initial(self, instance):
        sm.current = self.text_screen.name
        pass

    def _on_nextscene_from_text(self, instance):
        sm.current = self.image_screen.name
        pass

    def _on_nextscene_from_image(self, instance):
        sm.current = self.initial_screen.name
        pass



    pass


if __name__ == '__main__':
    app = MainApp()
    app.run()
