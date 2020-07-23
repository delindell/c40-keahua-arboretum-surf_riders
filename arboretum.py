class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.habitats = {
            "rivers": [],
            "grasslands": [],
            "coastlines": [],
            "forests": [],
            "swamps": [],
            "mountains": [],
        }
