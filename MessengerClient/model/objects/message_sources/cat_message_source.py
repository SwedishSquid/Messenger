from model.objects.message_sources.message_source import MessageSource


class CatMessageSource(MessageSource):
    data = [
        {'user': 'cat', 'text': 'mew neew mau', 'time': 'cat o`clock'},
        # {'user': '', 'text': '', 'time': 'cat o`clock'}
        {'user': 'big cat', 'text': 'miieeeeewww', 'time': 'cat o`clock'}
    ]

    def get_all(self):
        return self.data

    def add(self, ms_data):
        self.data.append(ms_data)
        pass
