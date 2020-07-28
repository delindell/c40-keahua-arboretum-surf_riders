class Colorizer:

    def colorize(self, str, tcolor, bcolor, effect):
        return f'{effect}{bcolor}{tcolor}{str}\033[0m'