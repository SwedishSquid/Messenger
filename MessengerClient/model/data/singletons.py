"""
when importing variables or functions from here, do not do

from ....singletons import ....

cause this will import original functions or variables
instead do

from .... import singletons

and just use vars from it
"""


def get_screen_changer():
    print('if you see this -> screen_changer singleton is broken')
    pass


def get_model():
    print('this should not been shown. if you see this => model singleton is broken')
    pass
