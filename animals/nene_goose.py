from animals import Animal
from animals import Identifiable

class NeneGoose(Animal, Identifiable):

    def __init__(self, species, age):
        Animal.__init__(self, species, age)
        Identifiable.__init__(self)
        self.__prey = { "Silversword", "Grass", "Blue Jade Vine",
        "Eucalyptus" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Nene Goose enjoyed delicious {prey}')
        else:
            print(f'The Nene Goose hated the {prey}')


    def __str__(self):
        return f'Nene Goose {self.id}. HONK HONK!'
