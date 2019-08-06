import abc


class Player(abc.ABC):

    # Initially each player has 20 armies at his disposal,
    # and controls no territories at all.
    def __init__(self, territories=None):
        if territories is None:
            territories = {}
        self.armies = 20
        self.territories = territories
        super().__init__()

    def play(self):
        self.place_armies()
        self.attack()

    @abc.abstractmethod
    def place_armies(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass
