from animals import Aquatic

class Freshwater(Aquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypertonic"
