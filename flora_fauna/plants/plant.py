class Plant:

    def __init__(self, species, season, num_seeds):
      self.__species = species
      self.__peak_season = season
      self.__seeds_produced = num_seeds

    @property
    def seeds_produced(self):
      return self.__seeds_produced

    @property
    def species(self):
      return self.__species

    @property
    def peak_season(self):
      return self.__peak_season