import os
from arboretum import Arboretum
from environments import Mountain
from environments import River
from actions import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("")
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options
    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        pass

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()
