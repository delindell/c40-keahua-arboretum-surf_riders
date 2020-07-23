import os


def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    for key, value in arboretum.habitats.items():
        print(key, value)
        for item in value:
            for index, animal in enumerate(item.animal_population):
                print(f'  {index + 1}. {animal.species}')
            

    # for river in arboretum.rivers:
    #     print(f'\n{river.name} [{river.id}]') # missing id value
    #     for index, animal in enumerate(river.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    # for swamp in arboretum.swamps:
    #     print(f'\n{swamp.name} [{swamp.id}]') # missing id value
    #     for index, animal in enumerate(swamp.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    # for coastline in arboretum.coastlines:
    #     print(f'\n{coastline.name} [{coastline.id}]') # missing id value
    #     for index, animal in enumerate(coastline.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    # for forest in arboretum.forests:
    #     print(f'\n{forest.name} [{forest.id}]') # missing id value
    #     for index, animal in enumerate(forest.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    # for grassland in arboretum.grasslands:
    #     print(f'\n{grassland.name} [{grassland.id}]') # missing id value
    #     for index, animal in enumerate(grassland.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    # for mountain in arboretum.mountains:
    #     print(f'\n{mountain.name} [{mountain.id}]') # missing id value
    #     for index, animal in enumerate(mountain.animal_population):
    #         print(f'  {index + 1}. {animal.species}')

    input("\n\nPress any key to continue...")
