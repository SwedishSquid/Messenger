import abc


class RegisterScreenControllerInterface(abc.ABC):
    @abc.abstractmethod
    def on_username_entered(self):
        pass

    @abc.abstractmethod
    def on_password_entered(self):
        pass

    @abc.abstractmethod
    def on_submit_button(self):
        pass

    @abc.abstractmethod
    def on_login_button(self):
        pass

    @abc.abstractmethod
    def get_typed_username(self):
        pass

    @abc.abstractmethod
    def get_typed_password(self):
        pass
    pass
