if False:
    # to use intellisense and to not cause circular dependencies i use type hints
    # importing like this prevents actual import but gives the opportunity to
    # specify type
    # something like this https://stackoverflow.com/questions/33837918/type-hints-solve-circular-dependency
    from controller.controller_main import Controller
    from model.model_main import Model
    from utility.screen_changer import ScreenChanger


class Singletons:
    _screen_changer: 'ScreenChanger'

    @classmethod
    def get_screen_changer(cls):
        return cls._screen_changer

    @classmethod
    def _set_screen_changer(cls, scr_changer):
        cls._screen_changer = scr_changer
        pass

    _model: 'Model'

    @classmethod
    def get_model(cls):
        return cls._model

    @classmethod
    def _set_model(cls, model: 'Model'):
        cls._model = model
        pass

    _controller: 'Controller'

    @classmethod
    def get_controller(cls):
        return cls._controller

    @classmethod
    def _set_controller(cls, controller: 'Controller'):
        cls._controller = controller
        pass
