from . import Biome

class Mountain(Biome):
    def __init__(self, name):
        super().__init__(name, 6, 4)
        self.high_elevation = True
