class Biome:
    
    def __init__(self, name, __capacity_animal=None, __capacity_plant=None):
        self.name = name
        self.__capacity_animal = __capacity_animal # it will be declared at sub classes
        self.__capacity_plant = __capacity_plant # it will be declared at sub classes
        self.__animal_population = list()
        self.__plant_population = list()


    # Add animals to the list
    def addAnimal(self, animal):
        if len(self.__animal_population) < self.__capacity_animal:
            self.__animal_population.append(animal)
            print("Animal added")
        else:
            print(f"{self.name} is currently at full capacity. Please find another place")


    # Add animals to the list
    def addPlants(self, plant):
        if len(self.__plant_population) < self.__capacity_plant:
            self.__animal_population.append(plant)
        else:
            print(f"{self.name} is currently at full capacity. Please find another place")


    # Capacity Population of Animals
    @property
    def capacity_animal(self):
        try:
            return self.__capacity_animal
        except AttributeError:
            return 'Animal Capacity is out'


    @capacity_animal.setter
    def capacity_animal(self):
        pass


    # Capacity Population of Plants
    @property
    def capacity_plant(self):
        try:
            return self.__capacity_plant
        except AttributeError:
            return 'Plant Capacity is out'

    @capacity_plant.setter
    def capacity_plant(self):
        pass
    

    # Animal Population
    @property
    def animal_population(self):
        try:
            return self.__animal_population
        except AttributeError:
            return 'Animal Population is out'

    @animal_population.setter
    def animal_population(self):
        pass
    

    # Plant Population
    @property
    def plant_population(self):
        try:
            return self.__plant_population
        except AttributeError:
            return 'Animal Population is out'

    @plant_population.setter
    def plant_population(self):
        pass