from .plant import Plant
from .sunlight import Shade
from .resistance import LowResistance
from ..characteristics import Forest

class RainbowTree(Plant, Shade, LowResistance, Forest):

    def __init__(self):
        Plant.__init__(self, 'Rainbow Eucalyptus Tree', 'fall', 8)
        Shade.__init__(self)
        LowResistance.__init__(self)
        Forest.__init__(self)