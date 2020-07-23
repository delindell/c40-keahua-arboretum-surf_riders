import os
from plants import MountainTree
from plants import Silversword
from plants import RainbowTree
from plants import BlueJadeVine

def cultivate_plant(arboretum):
    plant = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    print('\nChoose plant to cultivate.')
    choice = input("> ")

    if choice == "1":
        plant = MountainTree()
    if choice == "2":
        plant = Silversword()
        biome1 = arboretum.grasslands
    if choice == "3":
        plant = RainbowTree()
    if choice == "4":
        plant = BlueJadeVine()

    os.system('cls' if os.name == 'nt' else 'clear')
    
    for index, value in enumerate(biome1):
        print(f'{index + 1}. Grassland ({len(value.plants)})')

    print(f'\nWhere would you like to cultivate the {plant.species}?')
    choice = input("> ")

    # make this dynamic by changing up arboretum class
    arboretum.grasslands[int(choice) - 1].add_plant(animal)