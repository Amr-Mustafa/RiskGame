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

        print("Red: " + str(
            [(self.players[0].territories[key].identifier, self.players[0].territories[key].armies) for key in
             self.players[0].territories]))
        print("Blue: " + str(
            [(self.players[1].territories[key].identifier, self.players[1].territories[key].armies) for key in
             self.players[1].territories]))

        # print("Red Armies: " + str(self.players[0].armies))
        # print("Blue Armies: " + str(self.players[1].armies))

        # Game loop.
        player_turn = 0
        while not self.winner():
            self.players[player_turn].play()
            player_turn = 0 if player_turn == 1 else 1

            print("Red: " + str(
                [(self.players[0].territories[key].identifier, self.players[0].territories[key].armies) for key in
                 self.players[0].territories]))
            print("Blue: " + str(
                [(self.players[1].territories[key].identifier, self.players[1].territories[key].armies) for key in
                 self.players[1].territories]))
            input("Press Enter to continue...")

    # Check for a winner. A winner is a player who eliminates the other player.
    def winner(self):
        if len(self.players[0].territories) == 0:
            return True
        elif len(self.players[1].territories) == 0:
            return True
        return False


if __name__ == '__main__':
    game = Game('Simulation', 'Egypt', ['Aggressive_Agent', 'Aggressive_Agent'])
    game.start()
