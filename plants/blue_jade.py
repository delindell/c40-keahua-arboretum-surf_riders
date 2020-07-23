from .plant import Plant
from .sunlight import Partial
from .resistance import MediumResistance

class BlueJadeVine(Plant, Partial, MediumResistance):

    def __init__(self):
        Plant.__init__(self, 'Blue Jade Vine', 'year-round', 0)
        Partial.__init__(self)
        MediumResistance.__init__(self)
