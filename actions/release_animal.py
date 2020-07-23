import os
from animals import RiverDolphin
# from animals import GoldDustDayGecko
# from animals import NeneGoose
# from animals import Kikakapu
# from animals import Pueo
# from animals import Ulae
# from animals import OpeApeA
# from animals import HappyFaceSpider

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
        biome1 = arboretum.rivers
        # biome1 = arboretum.rivers + arboretum.coastline
    # if choice == "2":
    #     animal = GoldDustDayGecko()
    #     biome1 = arboretum.forest
    # if choice == "3":
    #     animal = NeneGoose()
    #     biome1 = arboretum.grasslands
    # if choice == "4":
    #     animal = Kikakapu()
    #     biome1 = arboretum.swamps + arboretum.rivers
    # if choice == "5":
    #     animal = Pueo()
    #     biome1 = arboretum.grasslands + arboretum.forest
    # if choice == "6":
    #     animal = Ulae()
    #     biome1 = arboretum.coastline
    # if choice == "7":
    #     animal = OpeApeA()
    #     biome1 = arboretum.forests + arboretum.mountains
    # if choice == "8":
    #     animal = HappyFaceSpider()
    #     biome1 = arboretum.swamps

    os.system('cls' if os.name == 'nt' else 'clear')
    # replace 'River' and 'Coastline' with dynamic variable
    for index, value in enumerate(biome1):
        print(f'{index + 1}. River ({len(value.animals)} animals)')
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    animal_habitat = biome1[int(choice) - 1]

    # find a way to add dynamically

    # arboretum.rivers[int(choice) - 1].animals.append(animal)
    arboretum.rivers[int(choice) - 1].add_animal(animal)
