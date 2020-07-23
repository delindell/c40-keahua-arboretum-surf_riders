from .animal import Animal
from .identifiable import Identifiable
from ..characteristics import Coastline

class Ulae(Animal, Coastline, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae", 1)
        Identifiable.__init__(self)
        Coastline.__init__(self)
        self.__prey = { "Flounder", "Mino", "Goober Fish" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Ulae ate the incredibly tasty {prey}')
        else:
            print(f'The Ulae spat out the {prey}')

    
    def __str__(self):
        return f'Ulae {self.id}. Razzzzzzzzzzor sharp teeth.'
