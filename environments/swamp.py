import sys
sys.path.append('../')

from environments.environment import Environment
from environments.stagnant import Stagnant
# from animals.


class Swamp(Environment):

    def __init__(self, name):
      self.name = name
      self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, Stagnant):
            raise TypeError(f"{item} is not of type Stagnant")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name
