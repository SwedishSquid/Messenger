from model.data import singletons

from model.data import user_secure_data as usd


def on_username_entered(username):
    print(f'entered username = {username}')
    pass


def on_password_entered(password):
    print(f'entered password ={"*"*len(password)}')
    pass


def on_submit_button_pressed(username, password):
    print('submitting login info')
    usd.username = username
    usd.password = password

    singletons.get_screen_changer().goto_chat_screen()
    pass
