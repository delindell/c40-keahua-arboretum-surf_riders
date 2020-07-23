from .plant import Plant
from .sunlight import Full
from .resistance import HighResistance

class Silversword(Plant, Full, HighResistance):

    def __init__(self):
        Plant.__init__(self, 'Silversword', 'summer', 22)
        Full.__init__(self)
        HighResistance.__init__(self)