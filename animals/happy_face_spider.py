from animals import Animal
from animals import Identifiable
from animals.movements import Walking

class HappyFaceSpider(Animal, Walking, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Happy Face Spider", age)
        Walking.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Crickets", "Worms", "Mosquitos", "Maggots" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The spider devoured the {prey}.')
        else:
            print(f'The spider did not enjoy the {prey}.')


    def __str__(self):
        return f'Spider {self.id}.'
