class Colorizer:

    def colorize(self, str, tcolor, bcolor, effect):
        print(f'{effect}{bcolor}{tcolor}{str}\033[0m')