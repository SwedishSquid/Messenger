from model.objects.message_sources.message_source import MessageSource


class FakeMessageSource(MessageSource):
    data = [{'user': 'system', 'text': 'hello there', 'time': 'seven eleven'},
            {'user': 'hacker', 'text': 'yes sir', 'time': 'time'},
            {'user': 'system', 'text': 'no mam', 'time': 'time2'},
            {'user': 'tim', 'text': 'my name is tim. i love eat a lot. like, a lot. i can`t stop thinking about food. food food food ... yesterday i ate whole watermelon', 'time': '11:08'},
            {'user': 'tim the eater', 'text': 'what is your favourite food?', 'time': '"^_^"'},
            {'user': 'tim the eater', 'text': 'people', 'time': '24:16'},
            {'user': 'toooooom', 'text': 'i eat only sunshine', 'time': '07:56'},
            {'user': 'tim the eater', 'text': 'are you from africa? i heard you people have watermelon oil', 'time': 'no time left'},
            {'user': 'toooooom', 'text': 'what', 'time': 'help should have come'},
            {'user': 'system', 'text': 'twin detected', 'time': '2 days ago'},
            {'user': 'tim the eater', 'text': 'too late, fool. HaHaHaHa', 'time': 'oh no. tim is here'},
            ]

    def get_all(self):
        return self.data

    def add(self, ms_data):
        self.data.append(ms_data)
