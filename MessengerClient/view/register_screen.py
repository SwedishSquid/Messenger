from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen

from utility import screen_names
from assets import colors

from model.data.singletons import Singletons

from kivy.lang import Builder

username_input_id = 'username_input_main'
password_input_id = 'password_input_main'
submit_button_id = 'submit_button_main'
login_button_id = 'login_button'

center = {'center_x': 0.5, 'center_y': 0.5}

markdown_str = f"""
<RegisterScreenLayout>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        MDTextField:
            id: {username_input_id}
            hint_text: "Enter username"
            helper_text: "and press enter"
            helper_text_mode: "on_focus"
            icon_left: "account-box"
            icon_left_color: app.theme_cls.primary_color
            pos_hint: {center}
            size_hint_x: None
            width: 300
            multiline: False

    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        MDTextField:
            id: {password_input_id}
            hint_text: "password"
            helper_text: "and press enter"
            helper_text_mode: "on_focus"
            icon_left: "account-box"
            icon_left_color: app.theme_cls.primary_color
            pos_hint: {center}
            size_hint_x: None
            width: 300
            multiline: False

    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        MDRectangleFlatButton:
            id: {submit_button_id}
            # size_hint_y: 1
            # size_hint_x: 1
            text: "зарегистрироваться"
            font_size: sp(30) # what is sp? https://stackoverflow.com/questions/2025282/what-is-the-difference-between-px-dip-dp-and-sp
            pos_hint: {center}

    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        MDTextButton:
            id: {login_button_id}
            text: 'уже зареган, войти в аккаунт'
            color: {colors.strange_color}
"""

Builder.load_string(markdown_str)


class RegisterScreen(Screen):
    def __init__(self, **kw):
        self.name = screen_names.register_screen_name
        super().__init__(**kw)

        self.layout = RegisterScreenLayout()

        self.layout.ids[username_input_id].on_text_validate = self._on_username_entered
        self.layout.ids[password_input_id].on_text_validate = self._on_password_entered
        self.layout.ids[submit_button_id].on_release = self._on_submit_button
        self.layout.ids[login_button_id].on_release = self._on_login_button

        self.add_widget(self.layout)
        pass

    @property
    def my_controller(self):
        return Singletons.get_controller().get_register_controller()

    def _on_username_entered(self):
        self.my_controller.on_username_entered()
        pass

    def _on_password_entered(self):
        self.my_controller.on_password_entered()
        pass

    def _on_submit_button(self):
        self.my_controller.on_submit_button()
        pass

    def _on_login_button(self):
        self.my_controller.on_login_button()
        pass

    def get_typed_username(self):
        return self.layout.ids[username_input_id].text

    def get_typed_password(self):
        return self.layout.ids[password_input_id].text


class RegisterScreenLayout(MDBoxLayout):
    pass
