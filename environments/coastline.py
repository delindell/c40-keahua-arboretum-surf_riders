from . import Biome

class Coastline(Biome):
    def __init__(self, name):
        super().__init__(name, 15, 3)
        self.salty_water = True