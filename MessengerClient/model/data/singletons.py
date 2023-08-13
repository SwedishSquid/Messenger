from controller.controller_interface import ControllerInterface
from utility.screen_changer_interface import ScreenChangerInterface
from model.model_interface import ModelInterface


class Singletons:
    _screen_changer: ScreenChangerInterface

    @classmethod
    def get_screen_changer(cls):
        return cls._screen_changer

    @classmethod
    def _set_screen_changer(cls, scr_changer):
        cls._screen_changer = scr_changer
        pass

    _model: ModelInterface

    @classmethod
    def get_model(cls):
        return cls._model

    @classmethod
    def _set_model(cls, model: ModelInterface):
        cls._model = model
        pass

    _controller: ControllerInterface

    @classmethod
    def get_controller(cls):
        return cls._controller

    @classmethod
    def _set_controller(cls, controller: ControllerInterface):
        cls._controller = controller
        pass
