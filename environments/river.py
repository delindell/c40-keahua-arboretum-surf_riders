from environments.biome import Environment


class River(Environment):

    def __init__(self, name):
        super().name = name
        super().__capacity_animal = 6 # it will be declared at sub classes
        super().__capacity_plant = 12 # it will be declared at sub classes

r = River("river")
print(r)
