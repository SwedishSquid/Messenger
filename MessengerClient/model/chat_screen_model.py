from model.data import singletons
from model.objects.message_source import MessageSource
from model.data.user_secure_data import UserSecureData
import time


class ChatModel:
    m_source: MessageSource = MessageSource()

    def submit(self, message: str):
        if self.m_source is None:
            print('message source not specified')
        else:
            m_data = {'user': UserSecureData.username, 'text': message, 'time': 'long time ago'}
            data = self.get_data()
            data.append(m_data)
            self.m_source.add(m_data)
        pass

    def on_back_button_action(self):
        singletons.get_screen_changer().goto_initial_screen()
        pass

    def load_data(self, data, mode: str = None):
        print('loading')
        if self.m_source is None:
            print('message source not specified')
        else:
            for m in range(len(data)):
                data.pop()
            for m in self.m_source.get_all():
                data.append(m)
        pass

    def get_data(self):
        print('view -> model connection failed')
        return None
