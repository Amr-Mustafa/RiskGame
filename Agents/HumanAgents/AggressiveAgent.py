from Agents.Player import Player


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

    # An aggressive human player greedily attempts to attack territories
    # with most armies that he can attack.
    def attack(self):

        # Find the territory with the most armies that he can attack.
        pass


if __name__ == '__main__':
    agent = AggressiveHuman({'1': '5', '2': '1', '4': '9'})
    agent.play()
