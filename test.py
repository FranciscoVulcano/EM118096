
from EM118090.EM118090 import EM118090
from EM118090 import parameters


meter = EM118090(port='COM5')
print(meter.get_value(value=parameters.InstantaneousParameters.voltage, device_id=1))