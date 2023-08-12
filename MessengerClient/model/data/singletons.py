"""
when importing variables or functions from here, do not do

from ....singletons import ....

cause this will import original functions or variables
instead do

from .... import singletons

and just use vars from it
"""

from controller.controller_interface import ControllerInterface

class Singletons:
    @classmethod
    def get_screen_changer(cls):
        print('if you see this -> screen_changer singleton is broken')
        pass

    @classmethod
    def get_model(cls):
        print('this should not been shown. if you see this => model singleton is broken')
        pass

    _controller: ControllerInterface

    @classmethod
    def get_controller(cls):
        return cls._controller

    @classmethod
    def _set_controller(cls, controller: ControllerInterface):
        cls._controller = controller
        pass
