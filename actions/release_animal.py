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
        biome1 = arboretum.habitats["rivers"] + arboretum.habitats["coastlines"]
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
        
    finding_which_biome(biome1, choice, animal, arboretum)


def finding_which_biome(biome1, choice, animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    for index, value in enumerate(biome1):
        if len(value.animal_population) < value.capacity_animal:
            print(f'{index + 1}. {value.name} [{value.id}] ({len(value.animal_population)} animals)')
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    try:
        animal_habitat = biome1[int(choice) - 1].name.lower() + 's'
        for index, val in enumerate(arboretum.habitats[animal_habitat]):
            if biome1[int(choice) - 1].id == val.id:
                arboretum.habitats[animal_habitat][index].addAnimal(animal)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice was not a valid input.')
        input("\n\nPress any key to continue...")
        return
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice is not in the range of choices.')
        input("\n\nPress any key to continue...")
        return
        