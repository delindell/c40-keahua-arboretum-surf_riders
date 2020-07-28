import os
import time
from arboretum import Arboretum
from actions import annex_habitat
from actions.release import release
from actions.feed_animal import feed_animal
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
        release(keahua, 'animal')

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        release(keahua, 'plant')

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

time.sleep(1)
colorizer.colorize('\nJurassic Park, System Security Interface', '', '', '')
colorizer.colorize('Version 4.0.5, Alpha E', colors.text_colors['GREEN'], '', '')
print('\nReady...')
time.sleep(2)
loader.load('> access main program', 1, 1, '')
colorizer.colorize('access: PERMISSION DENIED.', colors.text_colors['FAIL'], '', '')
time.sleep(0.5)
loader.load('> access main security', 1, 1, '')
time.sleep(0.5)
colorizer.colorize('access: PERMISSION DENIED.', colors.text_colors['FAIL'], '', '')
time.sleep(0.5)
loader.load('> access main program grid', 1, 1, '')
time.sleep(0.5)
colorizer.colorize('access: PERMISSION DENIED....AND.....\n', colors.text_colors['FAIL'], '', '')
time.sleep(2)
colorizer.colorize('Redirecting to K.I.L.L.E.R Arboretum Management Interface\n', colors.text_colors['WARNING'], '', '')
time.sleep(2)
loader.load('#', 40, 0.05, '')
colorizer.colorize('\nLoading complete... Redirecting', colors.text_colors['GREEN'], '', '')
time.sleep(2)
main_menu()
