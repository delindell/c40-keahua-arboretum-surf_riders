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
from actions import Typer

colors = Colors()
colorizer = Colorizer()
loader = Loading()
typer = Typer()

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    typer.animate(colorizer.colorize('+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n', colors.text_colors['OKGREEN'], '', ''), 0)
    typer.animate(colorizer.colorize('|  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |\n', colors.text_colors['HEADER'], colors.background_colors['BLUE'], colors.effects['BOLD']), 0)
    typer.animate(colorizer.colorize('+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n', colors.text_colors['OKGREEN'], '', ''), 0)
    typer.animate(colorizer.colorize('\n1. Annex Biome\n', '', '', ''), 0)
    typer.animate(colorizer.colorize('2. Release New Animal\n', '', '', ''), 0)
    typer.animate(colorizer.colorize('3. Feed Animal\n', '', '', ''), 0)
    typer.animate(colorizer.colorize('4. Cultivate New Plant\n', '', '', ''), 0)
    typer.animate(colorizer.colorize('5. Show Arboretum Report\n', '', '', ''), 0)
    typer.animate(colorizer.colorize('6. Exit\n', '', '', ''), 0)


def main_menu():
    """Show Keahua Action Options
    Arguments: None
    """
    build_menu()
    print(colorizer.colorize('\nChoose a KILLER option.', colors.text_colors['WARNING'], '', ''))
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

# time.sleep(1)

# typer.animate('\npatching into subnet...\n', 0.05)
# time.sleep(1)
# typer.animate('\nDNS ROUTING MISCONFIGURED: err 192.168.05 unavailable\n', 0.05)
# time.sleep(1)
# typer.animate('\nREROUTING TO INGEN SUBSYSTEMS ...', 0.03)
# time.sleep(2)

# typer.animate(colorizer.colorize('\n\nJurassic Park, System Security Interface\n', '', '', ''), 0.02)
# typer.animate(colorizer.colorize('Version 4.0.5, Alpha E\n', colors.text_colors['GREEN'], '', ''), 0.02)
# print('\nReady...')
# time.sleep(2)
# typer.animate('> access main program', 0.06)
# print(colorizer.colorize('\n\taccess: PERMISSION DENIED.', colors.text_colors['FAIL'], '', ''))
# time.sleep(0.5)
# typer.animate('> access main security', 0.08)
# time.sleep(0.5)
# print(colorizer.colorize('\n\taccess: PERMISSION DENIED.', colors.text_colors['FAIL'], '', ''))
# time.sleep(0.5)
# typer.animate('> access main program grid', 0.09)
# time.sleep(0.5)
# print(colorizer.colorize('\n\taccess: PERMISSION DENIED....AND.....\n', colors.text_colors['FAIL'], '', ''))
# time.sleep(2)
# print(colorizer.colorize('Redirecting to K.I.L.L.E.R Arboretum Management Interface\n', colors.text_colors['WARNING'], '', ''))
# time.sleep(2)
# loader.load('#', 40, 0.05, '')
# print(colorizer.colorize('\nLoading complete... Redirecting', colors.text_colors['GREEN'], '', ''))
# time.sleep(2)
main_menu()
