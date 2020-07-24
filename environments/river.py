from . import Biome
class River(Biome):

    def __init__(self, name):
        super().__init__(name, 3, 6)
        self.fresh_water = True