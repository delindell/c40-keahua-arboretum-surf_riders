from .animal import Animal
from .identifiable import Identifiable
from ..characteristics import River, Coastline

class RiverDolphin(Animal, River, Coastline, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River Dolphin", 13)
        Identifiable.__init__(self)
        River.__init__(self)
        Coastline.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
