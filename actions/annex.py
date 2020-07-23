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

    if choice == "1":
        river = River('River')
        arboretum.rivers.append(river)
    elif choice == "2":
        swamp = Swamp('Swamp')
        arboretum.swamps.append(swamp)
    elif choice == "3":
        coastline = Coastline('Coastline')
        arboretum.coastlines.append(coastline)
    elif choice == "4":
        grassland = Grassland('Grassland')
        arboretum.grasslands.append(grassland)
    elif choice == "5":
        mountain = Mountain('Mountain')
        arboretum.mountains.append(mountain)
    elif choice == "6":
        forest = Forest('Forest')
        arboretum.forests.append(forest)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
