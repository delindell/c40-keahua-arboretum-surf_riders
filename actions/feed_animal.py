import os
from flora_fauna import RiverDolphin
from flora_fauna import GoldDustDayGecko
from flora_fauna import NeneGoose
from flora_fauna import Kikakapu
from flora_fauna import Pueo
from flora_fauna import Ulae
from flora_fauna import Opeapea
from flora_fauna import HappyFaceSpider

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    print('\nChoose animal to feed.')
    choice = input("> ")
    choosing_animal(arboretum, choice)


def choosing_animal(arboretum, choice):
    if choice == "1":
        animal = RiverDolphin()
    elif choice == "2":
        animal = GoldDustDayGecko()
    elif choice == "3":
        animal = NeneGoose()
    elif choice == "4":
        animal = Kikakapu()
    elif choice == "5":
        animal = Pueo()
    elif choice == "6":
        animal = Ulae()
    elif choice == "7":
        animal = Opeapea()
    elif choice == "8":
        animal = HappyFaceSpider()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
    feeding_time(arboretum, animal)


def feeding_time(arboretum, animal):
    os.system('cls' if os.name == 'nt' else 'clear')

    for index, value in enumerate(animal.prey):
      print(f'{index + 1}. {value}')

    print(f'\nWhat is on the menu for the {animal.species}?')
    choice = input('> ')
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        if int(choice) < len(animal.prey):
            prey = list(animal.prey)
            animal.feed(prey[int(choice) - 1])
            input("\n\nPress any key to continue...")
    except ValueError as ex:
        print('Invalid Choice.')
        input("\n\nPress any key to continue...")
        return
        