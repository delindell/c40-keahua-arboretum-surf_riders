from .animal import Animal
from ..characteristics import Swamp, River

class Kikakapu(Animal, Swamp, River):

    def __init__(self):
        Animal.__init__(self, "Kikakapu", 1)
        Swamp.__init__(self)
        River.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }
        self.habitats = ['Swamp', 'River']

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kikakapu devoured the {prey}')
        else:
            print(f'The Kikakapu hated the {prey}')

    def __str__(self):
        return f'Kikakapu {self.id}. Razorrr sharp teeth!'
