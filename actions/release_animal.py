import os
from flora_fauna import RiverDolphin
from flora_fauna import GoldDustDayGecko
from flora_fauna import NeneGoose
from flora_fauna import Kikakapu
from flora_fauna import Pueo
from flora_fauna import Ulae
from flora_fauna import Opeapea
from flora_fauna import HappyFaceSpider

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
        biome1 = arboretum.habitats["rivers"]
        biome2 = arboretum.habitats["coastlines"]
    elif choice == "2":
        animal = GoldDustDayGecko()
        biome1 = arboretum.habitats["forests"]
    elif choice == "3":
        animal = NeneGoose()
        biome1 = arboretum.habitats["grasslands"]
    elif choice == "4":
        animal = Kikakapu()
        biome1 = arboretum.habitats["swamps"] + arboretum.habitats["rivers"]
    elif choice == "5":
        animal = Pueo()
        biome1 = arboretum.habitats["grasslands"] + arboretum.habitats["forests"]
    elif choice == "6":
        animal = Ulae()
        biome1 = arboretum.habitats["coastlines"]
    elif choice == "7":
        animal = Opeapea()
        biome1 = arboretum.habitats["forests"] + arboretum.habitats["mountains"]
    elif choice == "8":
        animal = HappyFaceSpider()
        biome1 = arboretum.habitats["swamps"]
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    # replace 'River' with dynamic variable)

    for index, value in enumerate(biome1):
        print(f'{index + 1}. {value.name} ({len(value.animal_population)} animals)')
    if biome2:
        for index, value in enumerate(biome2):
            print(f'{i+2}. {value.name} ({len(value.animal_population)} animals)')
        
        
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    if int(choice) > len(biome1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    animal_habitat = biome1[int(choice) - 1].name.lower() + 's'
    arboretum.habitats[animal_habitat][int(choice) - 1].addAnimal(animal)