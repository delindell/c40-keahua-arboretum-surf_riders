import os
from environments import River
# from environments import Swamp
# from environments import Coastline
# from environments import Grassland
# from environments import Mountain
# from environments import Forest

def annex_habitat(arboretum):
    biomes = ['River', 'Swamp', 'Coastline', 'Grassland', 'Mountain', 'Forest']
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, biome in enumerate(biomes):
        print(f'{i + 1}. {biome}')

    print('\nChoose what you want to annex.')
    choice = input("> ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    # if choice == "2":
    #     swamp = Swamp()
    #     arboretum.swaps.append(swamp)
    # if choice == "3":
    #     coastline = Coastline()
    #     arboretum.coastline.append(coastline)
    # if choice == "4":
    #     grassland = Grassland()
    #     arboretum.grasslands.append(grasslands)
    # if choice == "5":
    #     mountain = Mountain()
    #     arboretum.mountains.append(mountain)
    # if choice == "6":
    #     forest = Forest()
    #     arboretum.forest.append(forest)
