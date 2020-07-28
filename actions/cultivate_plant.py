# import os
# from flora_fauna import MountainTree
# from flora_fauna import Silversword
# from flora_fauna import RainbowTree
# from flora_fauna import BlueJadeVine

# def cultivate_plant(arboretum):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("1. Mountain Apple Tree")
#     print("2. Silversword")
#     print("3. Rainbow Eucalyptus Tree")
#     print("4. Blue Jade Vine")

#     print('\nChoose plant to cultivate.')
#     choice = input("> ")
#     choose_plant(arboretum, choice)
    

# def choose_plant(arboretum, choice):
#     if choice == "1":
#         plant = MountainTree()
#         # habitats = ['Mountain']
#         # biome1 = arboretum.habitats['mountains']
#     elif choice == "2":
#         plant = Silversword()
#         # habitats = ['Grassland']
#         # biome1 = arboretum.habitats['grasslands']
#     elif choice == "3":
#         plant = RainbowTree()
#         # habitats = ['Forest']
#         # biome1 = arboretum.habitats['forests']
#     elif choice == "4":
#         plant = BlueJadeVine()
#         # habitats = ['Grassland', 'Swamp']
#         # biome1 = arboretum.habitats['grasslands'] + arboretum.habitats['swamps']
#     else:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Invalid Choice.')
#         input("\n\nPress any key to continue...")
#         return

#     biomes = []
#     biomes.extend(arboretum.habitats['grasslands'])
#     biomes.extend(arboretum.habitats['swamps'])
#     biomes.extend(arboretum.habitats['forests'])
#     biomes.extend(arboretum.habitats['mountains'])
#     find_biome(biomes, choice, plant, arboretum)

# def find_biome(biomes, choice, plant, arboretum):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     checking_for_habitats = 0
#     checking_max_population = 0
#     arr_of_max_biomes = list()

#     list_disponible = list()

#     for index, value in enumerate(biomes):
#         if len(value.plant_population) == value.capacity_plant:
#             checking_max_population += 1
#             arr_of_max_biomes.append(value)
#         elif len(value.plant_population) < value.capacity_plant:
#             list_disponible.append(value)
#             checking_for_habitats += 1
#     for bio in list_disponible:
#         print(f'{list_disponible.index(bio)+1}. {bio.name} [{bio.id}] ({len(bio.plant_population)} plants)')

#     biomes = list_disponible

#     if checking_for_habitats == 0:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         if checking_max_population > 0:
#             for value in arr_of_max_biomes:
#                 print(f'The {value.name} biome is full. Please create another for the {plant.species}')
#         elif len(plant.habitats) > 1:
#                 print(f'No biomes available. \nThese are the available biomes to create for the {plant.species}:\n')
#                 for habitat in plant.habitats:
#                     print(f'{habitat}')
#         else:
#             print(f'No biomes available.\nPlease create a {plant.habitats[0]} biome for the {plant.species}')
#         input("\n\nPress any key to continue...")
#         return
                    
        
#     print(f'\nWhere would you like to release the {plant.species}?')
#     choice = input("> ")

#     try:
#         plant_habitat = list_disponible[int(choice) - 1].name.lower() + 's'
#         for index, val in enumerate(arboretum.habitats[plant_habitat]):
#             if list_disponible[int(choice) - 1].id == val.id:
#                 arboretum.habitats[plant_habitat][index].addPlants(plant)
#     except ValueError:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Your choice was not a valid input.')
#         input("\n\nPress any key to continue...")
#         return
#     except IndexError:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('Your choice is not in the range of choices.')
#         input("\n\nPress any key to continue...")
#         return