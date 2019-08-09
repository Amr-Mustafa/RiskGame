from Map.Map import Map
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

    # The user can choose between two different game modes: Simulation mode, and playing mode.
    # In the simulation mode, the user will choose any two agents from the defined agents except
    # for the human agent, to play against each other. In the playing mode, the human agent will
    # choose only one agent to play against it.
    def __init__(self, mode, map_choice, player_types):
        self.mode = mode
        self.map = Map(map_choice)
        self.player_types = player_types
        self.players = []

    def start(self):

        # Create the players. Players' objects are stored in the players list.
        self.players.append(self.possible_players[self.player_types[0]]('Red', self.map))
        self.players.append(self.possible_players[self.player_types[1]]('Blue', self.map))

        # Setup the map. The initial placement of armies is done randomly for all players.
        self.map.randomize(self.players)

        # Game loop.
        print("Red: " + str(
            [(self.players[0].territories[key].identifier, self.players[0].territories[key].armies) for key in
             self.players[0].territories]))
        print("Blue: " + str(
            [(self.players[1].territories[key].identifier, self.players[1].territories[key].armies) for key in
             self.players[1].territories]))

        # while len(self.players[0].territories) < 27 and len(self.players[1].territories) < 27:

        self.players[0].play()

        print("Red: " + str(
            [(self.players[0].territories[key].identifier, self.players[0].territories[key].armies) for key in
             self.players[0].territories]))
        print("Blue: " + str(
            [(self.players[1].territories[key].identifier, self.players[1].territories[key].armies) for key in
             self.players[1].territories]))

        self.players[1].play()

        print("Red: " + str(
            [(self.players[0].territories[key].identifier, self.players[0].territories[key].armies) for key in
             self.players[0].territories]))
        print("Blue: " + str(
            [(self.players[1].territories[key].identifier, self.players[1].territories[key].armies) for key in
             self.players[1].territories]))


if __name__ == '__main__':
    game = Game('Simulation', 'Egypt', ['Aggressive_Agent', 'Passive_Agent'])
    game.start()
