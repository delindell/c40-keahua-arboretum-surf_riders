from .plant import Plant
from .sunlight import Shade
from .resistance import LowResistance

class RainbowTree(Plant, Shade, LowResistance):

    def __init__(self):
        Plant.__init__(self, 'Rainbow Eucalyptus Tree', 'fall')
        Shade.__init__(self)
        LowResistance.__init__(self)
        self.seeds_produced = 8