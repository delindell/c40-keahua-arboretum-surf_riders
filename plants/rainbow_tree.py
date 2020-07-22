from .plant import Plant
from .sunlight import Shade
from .resistance import LowResistance

class RainbowTree(Plant, Shade, LowResistance):

    def __init__(self):
        Plant.__init__(self, 'Rainbow Eucalyptus Tree', 'fall', 8)
        Shade.__init__(self)
        LowResistance.__init__(self)