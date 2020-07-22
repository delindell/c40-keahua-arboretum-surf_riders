from .animal import Animal
from animals import Identifiable
from animals.movements import Walking

class GoldDustDayGecko(Animal, Walking, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Gold Dust Day Gecko", age)
        Walking.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Crickets", "Worms", "Mosquitos", "Maggots" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gecko ate {prey} for a meal.')
        else:
            print(f'The gecko rejects the {prey}')

    def __str__(self):
        return f'Gecko {self.id} is in the house.'
