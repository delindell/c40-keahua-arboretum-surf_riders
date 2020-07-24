import os

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    for key, value in arboretum.habitats.items():
        print(key, value)
        for item in value:
            for index, animal in enumerate(item.animal_population):
                print(f'  {index + 1}. {animal.species}')
            for index, plant in enumerate(item.plant_population):
                print(f'  {index + 1}. {plant.species}')

    input("\n\nPress any key to continue...")
