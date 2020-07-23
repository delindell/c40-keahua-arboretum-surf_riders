from .animal import Animal
from .identifiable import Identifiable

class Opeapea(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Opeapea", 5)
        Identifiable.__init__(self)
        self.__prey = { "Crickets", "Worms", "Mosquitos", "Maggots" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey}')
        else:
            print(f'The Opeapea rejects the {prey}')

    def __str__(self):
        return f'Opeapea {self.id}'
