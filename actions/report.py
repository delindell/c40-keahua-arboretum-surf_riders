import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    for key, habitats in arboretum.habitats.items():
        # print(key, habitats)
        for item in habitats:
            print(f'\n{item.name} [{item.id}]')
            for index, animal in enumerate(item.animal_population):
                print(f'  {index + 1}. {animal.species} ({animal.id})')
            for index, plant in enumerate(item.plant_population):
                print(f'  {index + 1}. {plant.species} ({plant.id})')

    input("\n\nPress any key to continue...")
