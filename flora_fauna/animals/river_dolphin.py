from .animal import Animal
from ..characteristics import River, Coastline

class RiverDolphin(Animal, River, Coastline):

    def __init__(self):
        Animal.__init__(self, "River Dolphin", 13)
        River.__init__(self)
        Coastline.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.habitats = ['River', 'Coastline']

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
