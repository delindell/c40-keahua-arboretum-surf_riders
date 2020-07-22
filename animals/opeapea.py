from .animal import Animal
from .identifiable import Identifiable
from animals.movements import Flying

class Opeapea(Animal, Flying, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Opeapea", age)
        Flying.__init__(self)
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
