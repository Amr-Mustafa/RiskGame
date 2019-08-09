class Territory:

    # Each territory has an identifier, a controlling player, a list of
    # adjacent territories, and a number of armies occupying the territory.
    def __init__(self, game_map, identifier, adjacent_identifiers, player=None, armies=0):
        self.map = game_map
        self.identifier = identifier
        self.adjacent_identifiers = adjacent_identifiers
        self.player = player
        self.armies = armies

    # Get the adjacency list for the given territory. Returns a list of territories.
    def adjacent(self):
        return [self.map.game_map[key] for key in self.map.game_map if self.map.game_map[key].is_adjacent(self)]

    # Check if two territories are adjacent to each other.
    def is_adjacent(self, territory):
        return territory.identifier in self.adjacent_identifiers
