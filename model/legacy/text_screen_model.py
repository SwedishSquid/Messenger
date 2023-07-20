from model.data import singletons
import requests

_common_url = 'https://swedishsquid.github.io/MyWebPage/messengerTest/'
_file_names = ['text0.html', 'text1.html', 'text2.html', 'text3.html', 'text4.html', 'text5.html', 'text6.html', 'text7.html', ]
_file_num = 0


def _load_text():
    url = _common_url + _file_names[_file_num]
    try:
        r = requests.get(url)
        text = r.text
    except requests.RequestException as e:
        text = str(e)  # 'no internet found :D'
        print(text)
    return text


def on_next_screen_button_action():
    singletons.get_screen_changer().goto_image_screen()
    pass


def on_next_text_button_action():
    global _file_num
    _file_num = (_file_num + 1) % len(_file_names)
    return _load_text()


def on_previous_text_button_action():
    global _file_num
    _file_num = (_file_num - 1) % len(_file_names)
    return _load_text()
