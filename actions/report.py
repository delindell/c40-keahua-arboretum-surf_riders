import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    input("\n\nPress any key to continue...")