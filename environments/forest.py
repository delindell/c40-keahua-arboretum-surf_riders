import os
from . import Biome

class Forest(Biome):
    def __init__(self, name,):
        super().__init__(name, 20, 32)
        self.rainy = True
        self.shady = True

    def addAnimal(self, animal):
        try:
            if animal.forest:
                if len(self.animal_population) < self.capacity_animal:
                    self.animal_population.append(animal)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Animal added")
                    input("\n\nPress any key to continue...")
                else:
                    print(f"{self.name} is currently at full capacity. Please find another place")
        except AttributeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only forest animals can be added to a forest.")
            print(f'\nThe {animal.species} can be released in the types of biomes below:\n')
            for habitat in animal.habitats:
                    print(f'{habitat}')
            input("\n\nPress any key to continue...")

    def addPlants(self, plant):
        try:
            if plant.forest:
                if len(self.plant_population) < self.capacity_plant:
                    self.plant_population.append(plant)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Plant added")
                    input("\n\nPress any key to continue...")
                else:
                    print(f"{self.name} is currently at full capacity. Please find another place")
        except AttributeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only plants that need alot of shade can be added to a forest.")
            print(f'\nThe {plant.species} can be released in the types of biomes below:\n')
            for habitat in plant.habitats:
                    print(f'{habitat}')
            input("\n\nPress any key to continue...")
