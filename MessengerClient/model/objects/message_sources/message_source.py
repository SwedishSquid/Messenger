import abc


class MessageSource(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def add(self, ms_data):
        pass
