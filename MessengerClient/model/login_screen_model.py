from model.data.singletons import Singletons
from utility import screen_names

from model.data.user_secure_data import UserSecureData


class LoginModel:
    @property
    def my_controller(self):
        return Singletons.get_controller().get_login_controller()

    def on_username_entered(self):
        username = self.my_controller.get_typed_username()
        print(f'entered username = {username}')
        pass

    def on_password_entered(self):
        password = self.my_controller.get_typed_password()
        print(f'entered password ={"*" * len(password)}')
        pass

    def on_submit_button_pressed(self):
        print('submitting login info')
        username = self.my_controller.get_typed_username()
        password = self.my_controller.get_typed_password()
        if username is None or username == '':
            UserSecureData.username = 'noname'
        else:
            UserSecureData.username = username
        UserSecureData.sessionKey = self._get_session_key(username, password)
        print(UserSecureData.sessionKey)
        Singletons.get_screen_changer().goto_chat_screen()
        pass

    def on_register_button(self):
        print('register yourself')
        Singletons.get_screen_changer().goto_screen(screen_names.register_screen_name)
        pass

    def _get_session_key(self, username, password):
        return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
