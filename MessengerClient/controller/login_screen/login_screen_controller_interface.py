import abc


class LoginScreenControllerInterface(abc.ABC):
    # region on_buttons_events
    @abc.abstractmethod
    def on_submit_button(self):
        pass

    @abc.abstractmethod
    def on_register_button(self):
        pass
    # endregion

    # region getters
    @abc.abstractmethod
    def get_typed_username(self):
        pass

    @abc.abstractmethod
    def get_typed_password(self):
        pass
    # endregion

    # region events
    @abc.abstractmethod
    def on_username_entered(self):
        pass

    @abc.abstractmethod
    def on_password_entered(self):
        pass
    # endregion
    pass
