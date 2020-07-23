from . import Biome

class Forest(Biome):
    def __init__(self, name,):
        super().__init__(name, 20, 32)
        self.rainy = True
        self.shady = True