from .builder import CONVERTERS
from .converter1 import Converter1


@CONVERTERS.register_module()
def converer2(a, b):
    return Converter1(a, b)
