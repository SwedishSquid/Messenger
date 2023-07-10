from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage, Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import urllib.request
from urllib.error import URLError

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



'''from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def on_start(self):
        print('on_start')
        pass

    def on_stop(self):
        print('on stop')
        pass

    def on_pause(self):
        print('on pause')
        pass

    def on_resume(self):
        print('on_resume')
        pass

    def build(self):
        self.title = 'calculator'
        self.icon = 'fish_icon.png'

        self.operators = ['/', '*', '+', '-']
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55)
        main_layout.add_widget((self.solution))
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        pass

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(text))
            self.solution.text = solution
        pass

if __name__ == "__main__":
    app = MainApp()
    app.run()'''