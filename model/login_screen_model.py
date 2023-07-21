from model.data import singletons

from model.data.user_secure_data import UserSecureData


class LoginModel:
    def on_username_entered(self, username):
        print(f'entered username = {username}')
        pass

    def on_password_entered(self, password):
        print(f'entered password ={"*" * len(password)}')
        pass

    def on_submit_button_pressed(self, username, password):
        print('submitting login info')
        UserSecureData.username = username
        UserSecureData.sessionKey = self._get_session_key(username, password)
        print(UserSecureData.sessionKey)
        singletons.get_screen_changer().goto_chat_screen()
        pass

    def _get_session_key(self, username, password):
        return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
