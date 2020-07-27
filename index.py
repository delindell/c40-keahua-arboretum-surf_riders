import os
import time
from arboretum import Arboretum
from environments import Mountain
from environments import River
from actions import annex_habitat
from actions.release_animal import release_animal
from actions.feed_animal import feed_animal
from actions.cultivate_plant import cultivate_plant
from actions.report import build_facility_report
from actions import Colors
from actions import Colorizer
from actions import Loading

colors = Colors()
colorizer = Colorizer()
loader = Loading()

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+')
    print('|  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |')
    print('+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n')
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit\n")


def main_menu():
    """Show Keahua Action Options
    Arguments: None
    """
    build_menu()
    print('Choose a KILLER option.')
    choice = input("> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

print('Jurassic Arboretum, System Security Interface')
print('Version 4.0.5, Alpha E')
print('Ready...')
time.sleep(3)
loader.load('.', 15, )
main_menu()
