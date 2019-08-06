from Map import Map
from Agents.HumanAgents.AggressiveAgent import AggressiveAgent
from Agents.HumanAgents.PassiveAgent import PassiveAgent


class Game:

    # Initial army size for each player depends on the total
    # number of players participating in the game.
    army_size = {
        '2': '40',
        '3': '35',
        '4': '30',
        '5': '25',
        '6': '20'
    }

    # Available players.
    possible_players = {
        'Passive_Agent': PassiveAgent,
        'Aggressive_Agent': AggressiveAgent,
        'Pacifist_Human': '',
        'Greedy_AI': '',
        'A*_V1_AI': '',
        'A*_V2_AI': '',
        'MiniMax_AI': ''
    }

    def __init__(self, map_choice, player_types):
        self.map = Map(map_choice)
        self.number_of_players = len(player_types)
        self.player_types = player_types
        self.players = []

    def start(self):

        # Create the players.
        for player_type in self.player_types:
            self.players.append(self.possible_players[player_type](self.map))

        self.map.randomize(self.number_of_players, self.army_size[str(self.number_of_players)])


if __name__ == '__main__':
    game = Game('Egypt', ['Aggressive_Agent', 'Passive_Agent'])
    game.start()
