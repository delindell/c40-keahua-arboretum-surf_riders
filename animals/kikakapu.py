from animals import Animal
from animals import Identifiable
from animals.movements import Swimming
from animals.characteristics import StagnantFreshWater, Freshwater

class Kikakapu(Animal, StagnantFreshWater, Freshwater, Identifiable):

    def __init__(self, species, age):
        Animal.__init__(self, species, age)
        Freshwater.__init__(self)
        StagnantFreshWater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kikakapu devoured the {prey}')
        else:
            print(f'The Kikakapu hated the {prey}')
