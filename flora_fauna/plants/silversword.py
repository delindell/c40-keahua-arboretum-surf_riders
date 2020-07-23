from .plant import Plant
from .sunlight import Full
from .resistance import HighResistance
from ..characteristics import Grassland

class Silversword(Plant, Full, HighResistance, Grassland):

    def __init__(self):
        Plant.__init__(self, 'Silversword', 'summer', 22)
        Full.__init__(self)
        HighResistance.__init__(self)
        Grassland.__init__(self)