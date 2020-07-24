from . import Biome

class Mountain(Biome):
    def __init__(self, name):
        super().__init__(name, 3, 3)
        self.high_elevation = True
