from animals import Animal 
from animals import Identifiable
from animals.movements import Walking

class Pueo(Animal, Walking, Identifiable):

    def __init__(self, species, age):
        Animal.__init__(self, species, age)
        Walking.__init__(self)
        Identifiable.__init__(self)
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
