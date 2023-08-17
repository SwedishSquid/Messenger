from model.login_screen_model import LoginModel
from view.login_screen import LoginScreen


class LoginScreenController:
    def __init__(self, login_model: LoginModel, login_screen: LoginScreen):
        self.login_model: LoginModel = login_model
        self.login_screen: LoginScreen = login_screen
        pass

    def on_submit_button(self):
        self.login_model.on_submit_button_pressed()
        pass

    def on_register_button(self):
        self.login_model.on_register_button()
        pass

    def get_typed_username(self):
        return self.login_screen.get_typed_username()

    def get_typed_password(self):
        return self.login_screen.get_typed_password()

    def on_username_entered(self):
        self.login_model.on_username_entered()
        pass

    def on_password_entered(self):
        self.login_model.on_password_entered()
        pass
