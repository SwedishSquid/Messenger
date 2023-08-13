import abc


class ChatScreenControllerInterface(abc.ABC):
    @abc.abstractmethod
    def on_submit(self):
        pass

    @abc.abstractmethod
    def on_back_button(self):
        pass

    @abc.abstractmethod
    def on_load_button(self):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass

    # @abc.abstractmethod
    # def set_messages(self, messages):
    #     pass
    #
    # @abc.abstractmethod
    # def add_messages_down(self, messages):
    #     pass
    #
    # @abc.abstractmethod
    # def add_messages_up(self, messages):
    #     pass

    @abc.abstractmethod
    def get_typed_message(self):
        pass
