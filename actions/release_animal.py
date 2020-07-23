import os
from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFaceSpider

def release_animal(arboretum):
    available_animals = ["River Dolphin", "Gold Dust Day Gecko", "Nene Goose", "Kīkākapu", "Pueo", "'Ulae", "Ope'ape'a", "Happy-Face Spider"]

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, animal in enumerate(available_animals):
        print(f'{index + 1}. {animal}')

    print('\nChoose animal.')
    choice = input("> ")
    choosing_which_animal(arboretum, choice)

def choosing_which_animal(arboretum, choice):
    if choice == "1":
        animal = RiverDolphin()
        biome1 = arboretum.rivers + arboretum.coastlines
    elif choice == "2":
        animal = GoldDustDayGecko()
        biome1 = arboretum.forests
    elif choice == "3":
        animal = NeneGoose()
        biome1 = arboretum.grasslands
    elif choice == "4":
        animal = Kikakapu()
        biome1 = arboretum.swamps + arboretum.rivers
    elif choice == "5":
        animal = Pueo()
        biome1 = arboretum.grasslands + arboretum.forests
    elif choice == "6":
        animal = Ulae()
        biome1 = arboretum.coastlines
    elif choice == "7":
        animal = Opeapea()
        biome1 = arboretum.forests + arboretum.mountains
    elif choice == "8":
        animal = HappyFaceSpider()
        biome1 = arboretum.swamps
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    # replace 'River' with dynamic variable
    for index, value in enumerate(biome1):
        print(f'{index + 1}. {value.name} ({len(value.animal_population)} animals)')
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    if int(choice) > len(biome1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    animal_habitat = biome1[int(choice) - 1].name

    # add dynamically instead of this
    if animal_habitat == 'River':
        arboretum.rivers[int(choice) - 1].addAnimal(animal)
    elif animal_habitat == 'Coastline':
        arboretum.coastlines[int(choice) - 1].addAnimal(animal)
    elif animal_habitat == 'Swamp':
        arboretum.swamps[int(choice) - 1].addAnimal(animal)
    elif animal_habitat == 'Forest':
        arboretum.forests[int(choice) - 1].addAnimal(animal)
    elif animal_habitat == 'Mountain':
        arboretum.mountains[int(choice) - 1].addAnimal(animal)
    elif animal_habitat == 'Grassland':
        arboretum.grasslands[int(choice) - 1].addAnimal(animal)        
