from Agents.Player import Player


class AggressiveAgent(Player):

    # An aggressive human player places all of its bonus armies to the
    # territory with the most armies.
    def place_armies(self):

        # Calculate the number of additional armies.
        number_of_territories = len(self.territories)
        bonus_armies = 3 if number_of_territories < 3 else number_of_territories // 3

        # Find the conquered territory with the most number of armies and reinforce it.
        strongest_territory = list(sorted(self.territories, key=lambda key: self.territories[key].armies, reverse=True))[0]
        self.territories[strongest_territory].armies = int(self.territories[strongest_territory].armies) + bonus_armies

    # An aggressive human player greedily attempts to attack territories with most armies that he can attack.
    def attack(self):

        # Get all the territories that the player can attack.
        weak_territories = [self.map.game_map[key] for key in self.map.game_map if self.can_attack(self.map.game_map[key]) is True]

        # A player can not attack a territory he is already occupying so we remove those.
        weak_territories = list(
            filter(lambda territory: territory.identifier not in self.territories.keys(), weak_territories))

        # Attack all weak territories starting with the strongest one.
        while len(weak_territories) > 0:

            # Now that we have all the territories that can be attacked, we need to pick the one
            # with the highest number of armies (strongest one) and attack it.
            strongest_territory = list(sorted(
                weak_territories, key=lambda territory: territory.armies, reverse=True))[0]

            # At this point, we know the target of the attack, but we still do not know from which
            # conquered territory the player is going to attack. Thus, we find the possible attack bases.
            attack_bases = [self.territories[key] for key in self.territories.keys()
                            if self.can_attack(strongest_territory, self.territories[key])]

            # Choose the attack base.
            attack_base = attack_bases[0]

            # The actual battle starts here! We know the player's base and the target.
            # What if the territory is unoccupied?
            if strongest_territory.player is not None:
                strongest_territory.player.territories.pop(strongest_territory.identifier)  # Territory lost.
            strongest_territory.player = self  # Territory gained.
            self.territories[strongest_territory.identifier] = strongest_territory  # Territory gained.
            strongest_territory.armies = attack_base.armies - 1  # Must leave one army behind for defense.
            attack_base.armies = 1  # One army for defense.

            # Get all the territories that the player can attack.
            weak_territories = [self.map.game_map[key] for key in self.map.game_map if
                                self.can_attack(self.map.game_map[key]) is True]

            # A player can not attack a territory he is already occupying so we remove those.
            weak_territories = list(
                filter(lambda territory: territory.identifier not in self.territories.keys(), weak_territories))

    # A player can attack a territory if it is adjacent to one of his conquered
    # territories and if it is "weak".
    def can_attack(self, target_territory, base_territory=None):

        # Check if an attack on the target territory is possible through the base territory.
        if base_territory is not None:
            if base_territory.is_adjacent(target_territory):
                if int(base_territory.armies) - 1 > int(target_territory.armies):
                    return True
                else:  # Base is weaker than the target.
                    return False
            else:  # Base is not adjacent to the target.
                return False

        # Make sure at least one conquered territory is adjacent to the target territory.
        adjacent_territories = target_territory.adjacent()
        conquered_adjacent_territories = [territory for territory in adjacent_territories
                                          if territory.identifier in self.territories.keys()]

        # If the player controls no adjacent territories to the target, then he can not attack it.
        if len(conquered_adjacent_territories) is 0:
            return False

        # At this point, we know that the player controls an adjacent territory to the target, but still
        # we need to make sure that the player's armies in the adjacent territories are capable of attacking
        # the target territory.
        for conquered_adjacent_territory in conquered_adjacent_territories:
            if int(conquered_adjacent_territory.armies) - 1 > int(target_territory.armies):
                return True

        return False
