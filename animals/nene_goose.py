from animals import Animal
from animals import Identifiable
from animals.movements import Flying

class NeneGoose(Animal, Flying, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Nene Goose", age)
        Flying.__init__(self)
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
