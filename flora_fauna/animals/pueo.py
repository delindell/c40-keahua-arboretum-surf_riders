from .animal import Animal
from ..characteristics import Grassland, Forest

class Pueo(Animal, Grassland, Forest):

    def __init__(self):
        Animal.__init__(self, "Pueo", 8)
        Grassland.__init__(self)
        Forest.__init__(self)
        self.__prey = { "Rat", "Mouse", "Squirrel", "Naked Mole Rat" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey} for a nice meal.')
        else:
            print(f'The Pueo threw the {prey} back at you.')


    def __str__(self):
        return f'Pueo {self.id}. Weird Noises.'
