from random import randint

class Map:

    # Adjacency list representation of Egypt's map. The second element
    # in the tuple represents the current number of armies occupying
    # the territory. Initially, no armies are occupying any territory.
    # 'territory': ([adjacent territories, (controlling player, number of armies))
    Egypt = {
        '1':  (['2', '3', '14', '21'], ('0', 0)),
        '2':  (['1', '3'], ('0', 0)),
        '3':  (['2', '4', '9', '10', '14'], ('0', 0)),
        '4':  (['3', '5', '9'], ('0', 0)),
        '5':  (['4', '6', '9', '10', '11', '12'], ('0', 0)),
        '6':  (['5'], ('0', 0)),
        '7':  (['8', '13'], ('0', 0)),
        '8':  (['7', '13', '17', '18'], ('0', 0)),
        '9':  (['3', '4', '5', '10', '11'], ('0', 0)),
        '10': (['3', '5', '9', '11', '14'], ('0', 0)),
        '11': (['5', '9', '10', '12', '14', '16'], ('0', 0)),
        '12': (['5', '9', '10', '11', '13', '16', '17'], ('0', 0)),
        '13': (['7', '8', '12', '17'], ('0', 0)),
        '14': (['1', '3', '10', '11', '15', '16', '19', '20', '21'], ('0', 0)),
        '15': (['14', '19'], ('0', 0)),
        '16': (['11', '12', '14', '17', '19', '23'], ('0', 0)),
        '17': (['8', '12', '13', '16', '18', '23'], ('0', 0)),
        '18': (['8', '17'], ('0', 0)),
        '19': (['14', '15', '16', '20', '23'], ('0', 0)),
        '20': (['14', '19', '21', '22', '23'], ('0', 0)),
        '21': (['1', '14', '20', '22', '24', '25', '27'], ('0', 0)),
        '22': (['20', '21', '23', '24'], ('0', 0)),
        '23': (['16', '17', '19', '20', '22', '24', '25', '27'], ('0', 0)),
        '24': (['21', '22', '23', '25'], ('0', 0)),
        '25': (['21', '23', '24', '26', '27'], ('0', 0)),
        '26': (['25'], ('0', 0)),
        '27': (['21', '23', '25'], ('0', 0))
    }

    # Adjacency list representation of United States' map.
    UnitedStates = {
        '1':  ['2', '5'],
        '2':  ['1', '3', '4', '5'],
        '3':  ['2', '4', '9'],
        '4':  ['2', '3', '5', '8', '9'],
        '5':  ['1', '2', '4', '6', '7', '8'],
        '6':  ['5', '7', '16', '17'],
        '7':  ['5', '6', '8', '10', '15', '16', '17'],
        '8':  ['4', '5', '7', '9', '10', '11'],
        '9':  ['3', '4', '8', '10', '11'],
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

    # Default map option is Egypt.
    def __init__(self, game_map='Egypt'):
        if game_map == 'United States':
            self.game_map = self.UnitedStates
        else:
            self.game_map = self.Egypt

    # Get the adjacency list for the given territory.
    def adjacent_territories(self, territory):
        return self.game_map[territory][0]

    # Check if two territories are adjacent to each other.
    def adjacent(self, t_1, t_2):
        return t_2 in self.game_map[t_1][0]

    # Randomize initial map configuration given the number of players.
    def randomize(self, number_of_players, armies_per_player):

        player_ids = [x+1 for x in range(number_of_players)]

        for key in self.game_map:
            temp = list(self.game_map[key][1])
            temp[0] = str(player_ids[randint(1, number_of_players)-1])
            self.game_map[key] = (self.game_map[key][0], tuple(temp))


