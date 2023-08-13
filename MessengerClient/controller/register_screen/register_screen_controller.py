from controller.register_screen.register_screen_controller_interface import RegisterScreenControllerInterface
from model.register_model import RegisterModel
from view.register_screen import RegisterScreen


class RegisterScreenController(RegisterScreenControllerInterface):
    def __init__(self, model: RegisterModel, screen: RegisterScreen):
        self.model = model
        self.screen = screen
        pass

    def on_username_entered(self):
        self.model.on_username_entered()
        pass

    def on_password_entered(self):
        self.model.on_password_entered()
        pass

    def on_submit_button(self):
        self.model.on_submit_button()
        pass

    def on_login_button(self):
        self.model.on_login_button()
        pass

    def get_typed_username(self):
        return self.screen.get_typed_username()

    def get_typed_password(self):
        return self.screen.get_typed_password()
