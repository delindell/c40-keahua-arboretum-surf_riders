from animals import Animal
from animals import Identifiable

class HappyFaceSpider(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Happy Face Spider", 0.5)
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
