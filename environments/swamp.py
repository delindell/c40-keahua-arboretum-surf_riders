import os
from . import Biome

class Swamp(Biome):
    def __init__(self, name):
        super().__init__(name, 8, 12)
        self.stagnant_fresh_water = True

    def addAnimal(self, animal):
        try:
            if animal.swamp:
                if len(self.animal_population) < self.capacity_animal:
                    self.animal_population.append(animal)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Animal added!")
                    input("\n\nPress any key to continue...")
                else:
                    print(f"{self.name} is currently at full capacity. Please find another place")
        except AttributeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only swamp animals can be added to a swamp.")
            print(f'\nThe {animal.species} can be released in the types of biomes below:\n')
            for habitat in animal.habitats:
                    print(f'{habitat}')
            input("\n\nPress any key to continue...")

    def addPlants(self, plant):
        try:
            if plant.swamp:
                if len(self.plant_population) < self.capacity_plant:
                    self.plant_population.append(plant)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Plant added")
                    input("\n\nPress any key to continue...")
                else:
                    print(f"{self.name} is currently at full capacity. Please find another place")
        except AttributeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only plants that need partial sunlight can be added to a swamp.")
            print(f'\nThe {plant.species} can be released in the types of biomes below:\n')
            for habitat in plant.habitats:
                    print(f'{habitat}')
            input("\n\nPress any key to continue...")