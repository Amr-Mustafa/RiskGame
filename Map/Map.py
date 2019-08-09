from random import randint
from Map.Territory import Territory


class Map:

    # Default map option is Egypt.
    def __init__(self, game_map='Egypt'):

        # Adjacency list representation of Egypt's map. Each territory
        # has an id, a controlling player from the set {'Red', 'Blue'},
        # a list of adjacent territories, and a number of armies occupying
        # the territory.
        self.Egypt = {
            '1': Territory(self, '1', ['2', '3', '14', '21']),
            '2': Territory(self, '2', ['1', '3']),
            '3': Territory(self, '3', ['2', '4', '9', '10', '14']),
            '4': Territory(self, '4', ['3', '5', '9']),
            '5': Territory(self, '5', ['4', '6', '9', '10', '11', '12']),
            '6': Territory(self, '6', ['5']),
            '7': Territory(self, '7', ['8', '13']),
            '8': Territory(self, '8', ['7', '13', '17', '18']),
            '9': Territory(self, '9', ['3', '4', '5', '10', '11']),
            '10': Territory(self, '10', ['3', '5', '9', '11', '14']),
            '11': Territory(self, '11', ['5', '9', '10', '12', '14', '16']),
            '12': Territory(self, '12', ['5', '9', '10', '11', '13', '16', '17']),
            '13': Territory(self, '13', ['7', '8', '12', '17']),
            '14': Territory(self, '14', ['1', '3', '10', '11', '15', '16', '19', '20', '21']),
            '15': Territory(self, '15', ['14', '19']),
            '16': Territory(self, '16', ['11', '12', '14', '17', '19', '23']),
            '17': Territory(self, '17', ['8', '12', '13', '16', '18', '23']),
            '18': Territory(self, '18', ['8', '17']),
            '19': Territory(self, '19', ['14', '15', '16', '20', '23']),
            '20': Territory(self, '20', ['14', '19', '21', '22', '23']),
            '21': Territory(self, '21', ['1', '14', '20', '22', '24', '25', '27']),
            '22': Territory(self, '22', ['20', '21', '23', '24']),
            '23': Territory(self, '23', ['16', '17', '19', '20', '22', '24', '25', '27']),
            '24': Territory(self, '24', ['21', '22', '23', '25']),
            '25': Territory(self, '25', ['21', '23', '24', '26', '27']),
            '26': Territory(self, '26', ['25']),
            '27': Territory(self, '27', ['21', '23', '25'])
        }

        self.UnitedStates = {
            '1': ['2', '5'],
            '2': ['1', '3', '4', '5'],
            '3': ['2', '4', '9'],
            '4': ['2', '3', '5', '8', '9'],
            '5': ['1', '2', '4', '6', '7', '8'],
            '6': ['5', '7', '16', '17'],
            '7': ['5', '6', '8', '10', '15', '16', '17'],
            '8': ['4', '5', '7', '9', '10', '11'],
            '9': ['3', '4', '8', '10', '11'],
            '10': ['7', '8', '9', '11', '13', '14', '15'],
            '11': [],
            '12': [],
            '13': [],
            '14': [],
            '15': [],
            '16': [],
            '17': [],
            '18': [],
            '19': [],
            '20': [],
            '21': [],
            '22': [],
            '23': [],
            '24': [],
            '25': [],
            '26': [],
            '27': [],
            '28': [],
            '29': [],
            '30': [],
            '31': [],
            '32': [],
            '33': [],
            '34': [],
            '35': [],
            '36': [],
            '37': [],
            '38': [],
            '39': [],
            '40': [],
            '41': [],
            '42': [],
            '43': [],
            '44': [],
            '45': [],
            '46': [],
            '47': [],
            '48': [],
            '49': [],
            '50': []
        }

        if game_map == 'United States':
            self.game_map = self.UnitedStates
        else:
            self.game_map = self.Egypt

    # Randomize initial map configuration given the number of players.
    # Pick a random territory and assign a random player to it. Repeat
    # for all territories.
    def randomize(self, players):

        # For each territory in the map.
        for key in self.game_map:

            # If both players have no more armies to distribute, then we are done.
            if players[0].armies is 0 and players[1].armies is 0:
                break

            # Pick a random player. If this player has no more armies to distribute, pick the other one.
            index = randint(0, 1)
            player = players[index] if players[index].armies is not 0 else players[1 - index]

            # Pick a random number of armies to place on this territory and remove them from the player's reserve.
            armies = randint(1, player.armies)
            player.armies -= armies

            # Assign the player to the territory.
            self.game_map[key].player = player
            self.game_map[key].armies = armies
            player.territories[key] = self.game_map[key]

        # for key in self.game_map:
        #    if self.game_map[key].player is not None:
        #        print(key + ", " + str(self.game_map[key].player.identifier) + ", " + str(self.game_map[key].armies))

        # [players[0].territories[key].identifier for key in players[0].territories])
        # print(players[0].identifier + " " + str(players[0].territories))
        # print(players[1].identifier + " " + str(players[1].territories))
