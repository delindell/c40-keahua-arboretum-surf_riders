from .aquatic import Aquatic

class Saltwater(Aquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypotonic"
