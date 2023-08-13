import abc


class ModelInterface(abc.ABC):
    @property
    @abc.abstractmethod
    def login_model(self):
        pass

    @property
    @abc.abstractmethod
    def chat_model(self):
        pass

    @property
    @abc.abstractmethod
    def chat_catalog_model(self):
        pass

    @property
    @abc.abstractmethod
    def register_model(self):
        pass
