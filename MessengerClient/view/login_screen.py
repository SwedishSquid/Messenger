from kivymd.uix.screen import Screen
from utility import screen_names
from model.data.singletons import Singletons

from kivymd.uix.boxlayout import MDBoxLayout

from assets import colors

from kivy.lang import Builder

login_input_id = 'login_input_main'
password_input_id = 'password_input_main'
submit_button_id = 'submit_button_main'
register_button_id = 'register_button'

center = {'center_x': 0.5, 'center_y': 0.5}

markdown_str = f"""
<LoginScreenLayout>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)
    
    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
    
        MDTextField:
            id: {login_input_id}
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
            text: "отправить"
            font_size: sp(30) # what is sp? https://stackoverflow.com/questions/2025282/what-is-the-difference-between-px-dip-dp-and-sp
            pos_hint: {center}
    
    MDAnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        
        MDTextButton:
            id: {register_button_id}
            text: 'зарегистрироваться'
            color: {colors.strange_color}
"""

Builder.load_string(markdown_str)


class LoginScreen(Screen):
    def __init__(self, **kw):

        self.name = screen_names.login_screen_name
        super().__init__(**kw)

        box_layout = LoginScreenLayout()
        self.main_layout = box_layout
        box_layout.ids[login_input_id].on_text_validate = self._on_username_entered
        box_layout.ids[password_input_id].on_text_validate = self._on_password_entered
        box_layout.ids[submit_button_id].on_release = self._on_submit_button_release
        box_layout.ids[register_button_id].on_release = self._on_register_button_release
        self.add_widget(box_layout)

    def _on_username_entered(self):
        Singletons.get_controller().get_login_controller().on_username_entered()
        pass

    def _on_password_entered(self):
        Singletons.get_controller().get_login_controller().on_password_entered()
        pass

    def _on_submit_button_release(self):
        Singletons.get_controller().get_login_controller().on_submit_button()
        pass

    def _on_register_button_release(self):
        Singletons.get_controller().get_login_controller().on_register_button()
        pass

    def get_typed_username(self):
        return self.main_layout.ids[login_input_id].text

    def get_typed_password(self):
        return self.main_layout.ids[password_input_id].text


# create custom layout
# Builder applies rules in strings to every copy of specific <widget>
class LoginScreenLayout(MDBoxLayout):
    pass
