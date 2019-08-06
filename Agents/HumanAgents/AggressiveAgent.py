from Agents.Player import Player
from Map import Map


class AggressiveHuman(Player):

    # An aggressive human player places all of its bonus armies to the
    # territory with the most armies.
    def place_armies(self):

        # Calculate the number of additional armies.
        number_of_territories = len(self.territories)
        bonus_armies = 3 if number_of_territories < 3 else number_of_territories // 3

        # Find the conquered territory with the most number of armies and reinforce it.
        strongest_territory = list(sorted(self.territories.items(), key=lambda item: item[1], reverse=True))[0][0]
        self.territories[strongest_territory] = str(int(self.territories[strongest_territory]) + bonus_armies)

    # An aggressive human player greedily attempts to attack territories with most armies that he can attack.
    def attack(self):

        # Find the territory with the most armies that the player can attack.
        while True:
            if self.can_attack(sorted(self.map.game_map.items(), key=lambda item: item[1][1], reverse=True)[0]):
                pass

    # A player can attack a territory if it is adjacent to one of his conquered
    # territories and if it contains enough armies.
    def can_attack(self, territory):

        # Make sure at least one conquered territory is adjacent to the target territory.
        adjacent_territories = self.map.adjacent(territory)
        conquered_adjacent_territories = [territory for territory in adjacent_territories if territory in self.territories]

        # If the player controls no adjacent territories to the target, then he can not attack it.
        if len(conquered_adjacent_territories) is 0:
            return False

        # At this point, we know that the player controls an adjacent territory to the target, but still
        # we need to make sure that the player's armies in the adjacent territories are capable of attacking
        # the target territory.
        for conquered_adjacent_territory in conquered_adjacent_territories:
            if int(self.territories[conquered_adjacent_territory]) - 1 > int(self.map.game_map[territory][1]):

                # We return the territory from which we can attack the target.
                return conquered_adjacent_territory

        return False


if __name__ == '__main__':
    agent = AggressiveHuman(Map('Egypt'), {'10': '5', '2': '1', '14': '9'})
    agent.can_attack('1')
