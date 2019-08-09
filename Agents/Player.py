import abc


class Player(abc.ABC):

    # Initially each player has 20 armies at his disposal,
    # and controls no territories at all. Each player also
    # has a copy of the game map to plan his moves accordingly.
    def __init__(self, identifier, game_map):
        self.identifier = identifier
        self.map = game_map
        self.armies = 20
        self.territories = {}
        super().__init__()

    # Each turn consists of two parts: placing armies and attacking.
    # Strategies of placing armies and attacking territories depend
    # on the player.
    def play(self):
        self.place_armies()
        self.attack()

    @abc.abstractmethod
    def place_armies(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass
