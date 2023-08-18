from model.objects.message_sources.message_source import MessageSource


class NotLoadedMessageSource(MessageSource):

    def get_all(self):
        return [{'user': 'system', 'text': 'this screen not loaded yet. please wait or reload', 'time': 'unknown time'}]

    def add(self, ms_data):
        print('addition is meaningless')
        pass
