from .plant import Plant
from .sunlight import Partial
from .resistance import MediumResistance
from ..characteristics import Grassland, Swamp

class BlueJadeVine(Plant, Partial, MediumResistance, Grassland, Swamp):

    def __init__(self):
        Plant.__init__(self, 'Blue Jade Vine', 'year-round', 0)
        Partial.__init__(self)
        MediumResistance.__init__(self)
        Grassland.__init__(self)
        Swamp.__init__(self)
        self.habitats = ['Grassland', 'Swamp']
