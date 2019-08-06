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

        # Get all the territories that the player can attack.
        weak_territories = [territory for territory in self.map.game_map if self.can_attack(territory) is True]

        # A player can not attack a territory he is already occupying so we remove those.
        weak_territories = list(filter(lambda territory: territory not in self.territories, weak_territories))

        # Append strength of each territory.
        weak_territories = [(territory, self.map.game_map[territory][1]) for territory in weak_territories]

        # Now that we have all the territories that can be attacked, we need to pick the one
        # with the highest number of armies (strongest one) and attack it.
        strongest_territory = list(sorted(weak_territories, key=lambda item: item[1], reverse=True))[0]

        # At this point, we know the target of the attack, but we still do not know from which
        # conquered territory the player is going to attack. Thus, we find the possible attack bases.
        attack_bases = [(territory, self.territories[territory]) for territory in self.territories
                        if self.can_attack(strongest_territory[0], territory)]

        attack_base = attack_bases[0]

        # The actual battle starts here! We know the player's base and the target.
        self.territories[strongest_territory[0]] = str(int(attack_base[1]) - 1)
        self.territories[attack_base[0]] = '1'

    # A player can attack a territory if it is adjacent to one of his conquered
    # territories and if it is "weak".
    def can_attack(self, target_territory, base_territory=None):

        # Check if an attack on the target territory is possible through the base territory.
        if base_territory is not None:
            if self.map.adjacent(target_territory, base_territory):
                if int(self.territories[base_territory]) - 1 > int(self.map.game_map[target_territory][1]):
                    return True
                else:  # Base is weaker than the target.
                    return False
            else:  # Base is not adjacent to the target.
                return False

        # Make sure at least one conquered territory is adjacent to the target territory.
        adjacent_territories = self.map.adjacent_territories(target_territory)
        conquered_adjacent_territories = [territory for territory in adjacent_territories if territory in self.territories]

        # If the player controls no adjacent territories to the target, then he can not attack it.
        if len(conquered_adjacent_territories) is 0:
            return False

        # At this point, we know that the player controls an adjacent territory to the target, but still
        # we need to make sure that the player's armies in the adjacent territories are capable of attacking
        # the target territory.
        for conquered_adjacent_territory in conquered_adjacent_territories:
            if int(self.territories[conquered_adjacent_territory]) - 1 > int(self.map.game_map[target_territory][1]):
                return True

        return False


if __name__ == '__main__':
    agent = AggressiveHuman(Map('Egypt'), {'1': '9', '2': '1', '14': '9'})
    agent.attack()
