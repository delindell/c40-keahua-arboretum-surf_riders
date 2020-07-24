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
        habitats = ['River', 'Coastline']
        biome1 = arboretum.habitats["rivers"] + arboretum.habitats["coastlines"]
    elif choice == "2":
        animal = GoldDustDayGecko()
        habitats = ['Forest']
        biome1 = arboretum.habitats["forests"]
    elif choice == "3":
        animal = NeneGoose()
        habitats = ['Grassland']
        biome1 = arboretum.habitats["grasslands"]
    elif choice == "4":
        animal = Kikakapu()
        habitats = ['Swamp', 'River']
        biome1 = arboretum.habitats["swamps"] + arboretum.habitats["rivers"]
    elif choice == "5":
        animal = Pueo()
        habitats = ['Grassland', 'Forest']
        biome1 = arboretum.habitats["grasslands"] + arboretum.habitats["forests"]
    elif choice == "6":
        animal = Ulae()
        habitats = ['Coastline']
        biome1 = arboretum.habitats["coastlines"]
    elif choice == "7":
        animal = Opeapea()
        habitats = ['Forest', 'Mountain']
        biome1 = arboretum.habitats["forests"] + arboretum.habitats["mountains"]
    elif choice == "8":
        animal = HappyFaceSpider()
        habitats = ['Swamp']
        biome1 = arboretum.habitats["swamps"]
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
        
    finding_which_biome(biome1, choice, animal, arboretum, habitats)


def finding_which_biome(biome1, choice, animal, arboretum, habitats):
    os.system('cls' if os.name == 'nt' else 'clear')
    checking_for_habitats = 0
    checking_max_population = 0
    arr_of_max_biomes = list()

    list_disponible = list()

    for index, value in enumerate(biome1):
        if len(value.animal_population) == value.capacity_animal:
            checking_max_population += 1
            arr_of_max_biomes.append(value)
        elif len(value.animal_population) < value.capacity_animal:
            list_disponible.append(value)
            checking_for_habitats += 1
    for bio in list_disponible:
        print(f'{list_disponible.index(bio)+1}. {bio.name} [{bio.id}] ({len(bio.animal_population)} animals)')

    biome1 = list_disponible

    if checking_for_habitats == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        if checking_max_population > 0:
            for value in arr_of_max_biomes:
                print(f'The {value.name} biome is full. Please create another for the {animal.species}')
        elif len(habitats) > 1:
                print(f'No biomes available. \nThese are the available biomes to create for the {animal.species}:\n')
                for habitat in habitats:
                    print(f'{habitat}')
        else:
            print(f'No biomes available.\nPlease create a {habitats[0]} biome for the {animal.species}')
        input("\n\nPress any key to continue...")
        return
                    
        
    print(f'\nWhere would you like to release the {animal.species}?')
    choice = input("> ")

    try:
        animal_habitat = list_disponible[int(choice) - 1].name.lower() + 's'
        for index, val in enumerate(arboretum.habitats[animal_habitat]):
            if list_disponible[int(choice) - 1].id == val.id:
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
        