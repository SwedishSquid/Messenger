from kivymd.uix.screen import Screen

from kivymd.uix.screenmanager import ScreenManager
from utility import screen_names

from kivymd.uix.boxlayout import MDBoxLayout


from kivy.lang import Builder

login_input_id = 'login_input_main'
password_input_id = 'password_input_main'
submit_button_id = 'submit_button_main'

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
        self.add_widget(box_layout)

    def _on_username_entered(self):
        self.on_username_entered(self.main_layout.ids[login_input_id].text)
        pass

    def _on_password_entered(self):
        self.on_password_entered(self.main_layout.ids[password_input_id].text)
        pass

    def _on_submit_button_release(self):
        self.on_submit_button_pressed(self.main_layout.ids[login_input_id].text,
                                      self.main_layout.ids[password_input_id].text)
        pass

    # override these funcs to get information
    # done in login_screen_controller
    @staticmethod
    def on_username_entered(username):
        pass

    @staticmethod
    def on_password_entered(password):
        pass

    @staticmethod
    def on_submit_button_pressed(username, password):
        pass


# create custom layout
# Builder applies rules in strings to every copy of specific <widget>
class LoginScreenLayout(MDBoxLayout):
    pass
