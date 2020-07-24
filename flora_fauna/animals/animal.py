from .identifiable import Identifiable

class Animal(Identifiable):

    def __init__(self, species, age):
        Identifiable.__init__(self)
        self.species = species
        self.release_age = age

