class Roster:

    def __init__(self):
        self.current = 0
        self.players = []


    def _add_player(self, player_Name):
        if player_Name not in self.players:
            self.players.append(player_Name)
        pass

    def _current_player(self):
        return self.players[self.current]


    def _next_player(self):
        self.current = (self.current + 1) % len(self.players)