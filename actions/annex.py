import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest

def annex_habitat(arboretum):
    biomes = ['River', 'Swamp', 'Coastline', 'Grassland', 'Mountain', 'Forest']
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, biome in enumerate(biomes):
        print(f'{i + 1}. {biome}')

    print('\nChoose what you want to annex.')
    choice = input("> ")
    choosing_habitat(arboretum, choice)

def choosing_habitat(arboretum, choice):
    if choice == "1":
        river = River('River')
        arboretum.habitats['rivers'].append(river)
    elif choice == "2":
        swamp = Swamp('Swamp')
        arboretum.habitats['swamps'].append(swamp)
    elif choice == "3":
        coastline = Coastline('Coastline')
        arboretum.habitats['coastlines'].append(coastline)
    elif choice == "4":
        grassland = Grassland('Grassland')
        arboretum.habitats['grasslands'].append(grassland)
    elif choice == "5":
        mountain = Mountain('Mountain')
        arboretum.habitats['mountains'].append(mountain)
    elif choice == "6":
        forest = Forest('Forest')
        arboretum.habitats['forests'].append(forest)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
