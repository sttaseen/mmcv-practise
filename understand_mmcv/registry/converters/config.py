from .builder import CONVERTERS

converter1_cfg = dict(type='Converter1', a=a_value, b=b_value)
converter2_cfg = dict(type='converter2', a=a_value, b=b_value)
converter1 = CONVERTERS.build(converter1_cfg)
# returns the calling result
result = CONVERTERS.build(converter2_cfg)
