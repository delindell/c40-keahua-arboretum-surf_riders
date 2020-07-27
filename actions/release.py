import os
from flora_fauna import RiverDolphin, GoldDustDayGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider, MountainTree, Silversword, RainbowTree, BlueJadeVine

# The release function will decide whether to display animals or plants
def release(arboretum, name):
    if name == 'animal':
        arr_avail_species = ["River Dolphin", "Gold Dust Day Gecko", "Nene Goose", "Kīkākapu", "Pueo", "'Ulae", "Ope'ape'a", "Happy-Face Spider"]
    else:
        arr_avail_species = ['Mountain Apple Tree', 'Silversword', 'Rainbow Eucalyptus Tree', 'Blue Jade Vine']

    os.system('cls' if os.name == 'nt' else 'clear')

    for index, value in enumerate(arr_avail_species):
        print(f'{index + 1}. {value}')

    print(f'\nChoose which {name}.')   
    choice = input("> ")

    choosing_which_species(arboretum, choice, name)


# The choosing which species function will record the users choice
def choosing_which_species(arboretum, choice, name):
    if name == 'animal':
        if choice == "1":
            species = RiverDolphin()
        elif choice == "2":
            species = GoldDustDayGecko()
        elif choice == "3":
            species = NeneGoose()
        elif choice == "4":
            species = Kikakapu()
        elif choice == "5":
            species = Pueo()
        elif choice == "6":
            species = Ulae()
        elif choice == "7":
            species = Opeapea()
        elif choice == "8":
            species = HappyFaceSpider()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Choice.')
            input("\n\nPress any key to continue...")
            return
    else:
        if choice == "1":
            species = MountainTree()
        elif choice == "2":
            species = Silversword()
        elif choice == "3":
            species = RainbowTree()
        elif choice == "4":
            species = BlueJadeVine()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Choice.')
            input("\n\nPress any key to continue...")
            return

    biomes = []
    biomes.extend(arboretum.habitats["forests"])
    biomes.extend(arboretum.habitats["mountains"])
    biomes.extend(arboretum.habitats["rivers"])
    biomes.extend(arboretum.habitats["coastlines"])
    biomes.extend(arboretum.habitats["grasslands"])
    biomes.extend(arboretum.habitats["swamps"])
        
    finding_which_biome(biomes, choice, species, arboretum, name)


# The finding which biome function will ask the user where they would like to release an animal or cultivate a plant
# Once the user decides, it will add that plant or animal to the targeted biome
def finding_which_biome(biomes, choice, species, arboretum, name):
    os.system('cls' if os.name == 'nt' else 'clear')
    checking_for_habitats = 0
    checking_max_population = 0
    arr_of_max_biomes = list()
    list_disponible = list()

    if name == 'animal':
        for index, value in enumerate(biomes):
            if len(value.animal_population) == value.capacity_animal:
                checking_max_population += 1
                arr_of_max_biomes.append(value)
            elif len(value.animal_population) < value.capacity_animal:
                list_disponible.append(value)
                checking_for_habitats += 1
        for bio in list_disponible:
            print(f'{list_disponible.index(bio)+1}. {bio.name} [{bio.id}] ({len(bio.animal_population)} animals)')
    else:
        for index, value in enumerate(biomes):
            if len(value.plant_population) == value.capacity_plant:
                checking_max_population += 1
                arr_of_max_biomes.append(value)
            elif len(value.plant_population) < value.capacity_plant:
                list_disponible.append(value)
                checking_for_habitats += 1
        for bio in list_disponible:
            print(f'{list_disponible.index(bio)+1}. {bio.name} [{bio.id}] ({len(bio.plant_population)} plants)')

    biomes = list_disponible

    if checking_for_habitats == 0:
        blank_screen_error(checking_max_population, arr_of_max_biomes, species)
        return
                    
    print(f'\nWhere would you like to release the {species.species}?')
    choice = input("> ")

    try:
        habitat = list_disponible[int(choice) - 1].name.lower() + 's'
        if name == 'animal':
            for index, val in enumerate(arboretum.habitats[habitat]):
                if list_disponible[int(choice) - 1].id == val.id:
                    arboretum.habitats[habitat][index].addAnimal(species)
        else:
            for index, val in enumerate(arboretum.habitats[habitat]):
                if list_disponible[int(choice) - 1].id == val.id:
                    arboretum.habitats[habitat][index].addPlants(species)
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice was not a valid input.')
        input("\n\nPress any key to continue...")
        return
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Your choice is not in the range of choices.')
        input("\n\nPress any key to continue...")
        return


# The blank screen error is called on in the finding which biome function to display a propmt to let the user know why there was nothing displayed
def blank_screen_error(checking_max_population, arr_of_max_biomes, species):
    os.system('cls' if os.name == 'nt' else 'clear')
    if checking_max_population > 0:
        for value in arr_of_max_biomes:
            print(f'The {value.name} biome is full. Please create another for the {species.species}')
    elif len(species.habitats) > 1:
            print(f'No biomes available. \nThese are the available biomes to create for the {species.species}:\n')
            for habitat in species.habitats:
                print(f'{habitat}')
    else:
        print(f'No biomes available.\n\nPlease create a {species.habitats[0]} biome for the {species.species}')
    input("\n\nPress any key to continue...")
    