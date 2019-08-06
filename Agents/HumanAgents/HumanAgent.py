import abc
from Agents import Player


class HumanAgent(Player):

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def place_armies(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass
