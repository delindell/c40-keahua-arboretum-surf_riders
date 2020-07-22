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
    animal = None
    biome1 = None
    biome2 = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    print('Choose animal.')
    choice = input("> ")

    if choice == "1":
        animal = RiverDolphin()
        biome1 = arboretum.rivers
        # biome2 = arboretum.coastline
    # if choice == "2":
    #     animal = GoldDustDayGecko()
    #     biome1 = arboretum.forest
    # if choice == "3":
    #     animal = NeneGoose()
    #     biome1 = arboretum.grasslands
    # if choice == "4":
    #     animal = Kikakapu()
    #     biome1 = arboretum.swamps
    #     biome2 = arboretum.rivers
    # if choice == "5":
    #     animal = Pueo()
    #     biome1 = arboretum.grasslands
    #     biome2 = arboretum.forest
    # if choice == "6":
    #     animal = Ulae()
    #     biome1 = arboretum.coastline
    # if choice == "7":
    #     animal = OpeApeA()
    #     biome1 = arboretum.forests
    #     biome2 = arboretum.mountains
    # if choice == "8":
    #     animal = HappyFaceSpider()
    #     biome1 = arboretum.swamps


    os.system('cls' if os.name == 'nt' else 'clear')
    for index, value in enumerate(biome1):
        print(f'{index + 1}. River {value.id}')

    if biome2:
        for index, value in enumerate(biome1):
            print(f'{index + 1}. Coastline {value.id}')
        

    print(f'Where would you like to release the {animal.species}?')
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)
    # or should it be added with the add_animal method on the environment module? Replacing append with add_animal.
