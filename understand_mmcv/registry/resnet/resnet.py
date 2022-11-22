from builder import MODELS

@MODELS.register_module()
class Resnet():
    pass

@MODELS.register_module()
def foo(a):
    print(a)

