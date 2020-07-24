import os
from flora_fauna import MountainTree
from flora_fauna import Silversword
from flora_fauna import RainbowTree
from flora_fauna import BlueJadeVine

def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print('\nChoose plant to cultivate.')
    choice = input("> ")
    choose_plant(arboretum, choice)
    

def choose_plant(arboretum, choice):
    if choice == "1":
        plant = MountainTree()
        biome1 = arboretum.habitats['mountains']
    elif choice == "2":
        plant = Silversword()
        biome1 = arboretum.habitats['grasslands']
    elif choice == "3":
        plant = RainbowTree()
        biome1 = arboretum.habitats['forests']
    elif choice == "4":
        plant = BlueJadeVine()
        biome1 = arboretum.habitats['grasslands'] + arboretum.habitats['swamps']
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
    find_biome(biome1, choice, plant, arboretum)


def find_biome(biome1, choice, plant, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for index, value in enumerate(biome1):
        if len(value.plant_population) < value.capacity_plant:
            print(f'{index + 1}. {value.name} [{value.id}] ({len(value.plant_population)} plants)')

    print(f'\nWhere would you like to cultivate the {plant.species}?')
    choice = input("> ")

    try:
        plant_habitat = biome1[int(choice) - 1].name.lower() + 's'
        for index, val in enumerate(arboretum.habitats[plant_habitat]):
            if biome1[int(choice) - 1].id == val.id:
                arboretum.habitats[plant_habitat][index].addPlants(plant)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    # if choice == '' or int(choice) > len(biome1):
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print('Invalid Choice.')
    #     input("\n\nPress any key to continue...")
    #     return
    # else:
    #     plant_habitat = biome1[int(choice) - 1].name.lower() + 's'
    #     for index, val in enumerate(arboretum.habitats[plant_habitat]):
    #         if biome1[int(choice) - 1].id == val.id:
    #             arboretum.habitats[plant_habitat][index].addPlants(plant)