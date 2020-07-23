from . import Biome
# from animals.


class Swamp(Biome):
    def __init__(self, name):
        super().__init__(name, 8, 12)
        self.stagnant_fresh_water = True