from model.data.singletons import Singletons
from utility import screen_names

from model.data.user_secure_data import UserSecureData


class RegisterModel:
    @property
    def my_controller(self):
        return Singletons.get_controller().get_register_controller()

    def on_username_entered(self):
        username = self.my_controller.get_typed_username()
        print(f'entered username = {username}')
        pass

    def on_password_entered(self):
        password = self.my_controller.get_typed_password()
        print(f'entered password ={"*" * len(password)}')
        pass

    def on_submit_button(self):
        print('submitting right now')
        print('currently you can not register ;)')
        pass

    def on_login_button(self):
        Singletons.get_screen_changer().goto_screen(screen_names.login_screen_name)
        pass
