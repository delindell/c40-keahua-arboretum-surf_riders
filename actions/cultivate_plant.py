import os
from flora_fauna import MountainTree
from flora_fauna import Silversword
from flora_fauna import RainbowTree
from flora_fauna import BlueJadeVine

def cultivate_plant(arboretum):
    plant = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print('\nChoose plant to cultivate.')
    choice = input("> ")

    elif choice == "1":
        plant = MountainTree()
    elif choice == "2":
        plant = Silversword()
        biome1 = arboretum.grasslands
    elif choice == "3":
        plant = RainbowTree()
    elif choice == "4":
        plant = BlueJadeVine()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    
    for index, value in enumerate(biome1):
        print(f'{index + 1}. {value.name} ({len(value.plants)})')

    print(f'\nWhere would you like to cultivate the {plant.species}?')
    choice = input("> ")

    # make this dynamic by changing up arboretum class
    arboretum.grasslands[int(choice) - 1].add_plant(animal)