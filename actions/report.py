import os
from actions import Colors
from actions import Colorizer
from actions import Loading
from actions import Typer

colors = Colors()
colorizer = Colorizer()
loader = Loading()
typer = Typer()

def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorizer.colorize('+-++-++-++-++-++-++-++-++-+ +-++-++-++-++-++-+', colors.text_colors['OKGREEN'], '', ''))
    print(colorizer.colorize('|A||r||b||o||r||e||t||u||m| |R||e||p||o||r||t|', colors.text_colors['HEADER'], colors.background_colors['BLUE'], colors.effects['BOLD']))
    print(colorizer.colorize('+-++-++-++-++-++-++-++-++-+ +-++-++-++-++-++-+', colors.text_colors['OKGREEN'], '', ''))
    empty_list = 1
    for key, habitats in arboretum.habitats.items():
        if len(habitats) == 0:
            empty_list+=1
        for item in habitats:
            print(f'\n{item.name} [{item.id}]')
            if len(item.animal_population) > 0:
                print('    Animals:')
                for index, animal in enumerate(item.animal_population):
                    print(f'      {index + 1}. {animal.species} ({animal.id})')
            if len(item.plant_population) > 0:
                print('\n    Plants:')
                for index, plant in enumerate(item.plant_population):
                    print(f'      {index + 1}. {plant.species} ({plant.id})')
        if empty_list > 6:
            print('There are no biomes. Go create some!')
            input("\n\nPress any key to continue...")
            return

    input("\n\nPress any key to continue...")
