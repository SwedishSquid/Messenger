from kivy.app import App




class MainApp(App):
    def build(self):
        self.title = "fishenger"
        self.icon = 'fish_icon.png'
        import screens.screen_changer as screen_changer
        screen_changer.ScreenChanger()
        return screen_changer.instance
    #
    # def _on_nextscene_from_initial(self, instance):
    #     sm.current = self.text_screen.name
    #     pass
    #
    # def _on_nextscene_from_text(self, instance):
    #     sm.current = self.image_screen.name
    #     pass
    #
    # def _on_nextscene_from_image(self, instance):
    #     sm.current = self.initial_screen.name
    #     pass



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