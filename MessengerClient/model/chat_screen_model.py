from model.data.singletons import Singletons
from model.data.user_secure_data import UserSecureData
from model.objects.chat_info import ChatInfo
from utility import screen_names


class ChatModel:
    @property
    def m_source(self):
        return Singletons.get_model().get_source_manager().get_message_source()

    def _submit(self, message: str):
        if self.m_source is None:
            print('message source not specified')
        else:
            m_data = {'user': UserSecureData.username, 'text': message, 'time': 'long time ago'}
            data = self._get_data()
            data.append(m_data)
            self.m_source.add(m_data)
        pass

    def on_submit(self):
        text = Singletons.get_controller().get_chat_controller().get_typed_message()
        if text is not None and text != '':
            self._submit(text)
        pass

    def on_back_button_action(self):
        Singletons.get_screen_changer().goto_screen(screen_names.chat_list_screen_name)
        pass

    def on_load_data(self):
        print('loading')
        if self.m_source is None:
            print('message source not specified')
        else:
            data = self._get_data()
            for m in range(len(data)):
                data.pop()
            for m in self.m_source.get_all():
                data.append(m)
        pass

    def _get_data(self):
        return Singletons.get_controller().get_chat_controller().get_data()
