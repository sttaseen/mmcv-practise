from resnet import MODELS

resnet = MODELS.build(dict(type='Resnet'))

MODELS.build(dict(type='foo', a=1))