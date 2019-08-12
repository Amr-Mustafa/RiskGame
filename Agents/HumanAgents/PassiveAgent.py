from Agents.Player import Player


class PassiveAgent(Player):

    # A passive human player places all of its bonus armies to the
    # territory with the fewest armies.
    def place_armies(self):

        # Calculate the number of additional armies.
        number_of_territories = len(self.territories)
        bonus_armies = 3 if number_of_territories < 3 else number_of_territories // 3

        # Find the conquered territory with the least number of armies and reinforce it.
        if len(list(sorted(self.territories, key=lambda key: self.territories[key].armies))) == 0:
            return
        weakest_territory = list(sorted(self.territories, key=lambda key: self.territories[key].armies))[0]
        self.territories[weakest_territory].armies = int(self.territories[weakest_territory].armies) + bonus_armies

    # A passive human player does not attack at all.
    def attack(self):
        pass
