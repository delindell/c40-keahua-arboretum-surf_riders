from .aquatic import Aquatic

class StagnantFreshWater(Aquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypertonic"
