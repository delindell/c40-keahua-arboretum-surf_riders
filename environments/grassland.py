from . import Biome

class Grassland(Biome):
    def __init__(self, name,):
        super().__init__(name, 3, 3)
        self.no_shade = True
        self.little_rainfall = True
