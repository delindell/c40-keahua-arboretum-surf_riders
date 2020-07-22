import os
from animals import RiverDolphin
# from animals import GoldDustDayGecko
# from animals import NeneGoose
# from animals import Kikakapu
# from animals import Pueo
# from animals import Ulae
# from animals import OpeApeA
# from animals import HappyFaceSpider

def feed_animal(arboretum):
    animal = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to feed > ")

    if choice == "1":
        animal = RiverDolphin()
    # if choice == "2":
    #     animal = GoldDustDayGecko()
    # if choice == "3":
    #     animal = NeneGoose()
    # if choice == "4":
    #     animal = Kikakapu()
    # if choice == "5":
    #     animal = Pueo()
    # if choice == "6":
    #     animal = Ulae()
    # if choice == "7":
    #     animal = OpeApeA()
    # if choice == "8":
    #     animal = HappyFaceSpider()

    for index, value in enumerate(animal.prey):
      print(f'{index + 1}. {value}')

    print(f'What is on the menu for the {animal.species}')
    choice = input('> ')

    animal.feed()