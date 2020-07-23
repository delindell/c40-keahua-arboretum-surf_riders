import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for river in arboretum.rivers:
        print(f'\nRiver [{river.id}]')
        for index, animal in enumerate(river.animals):
            print(f'  {index + 1}. {animal.species}')

    input("\n\nPress any key to continue...")