class Roster:
    """The responsibility is to keep track of the players
     Stereotype: 
        Information Holder
     Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Players.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.current = 0
        self.players = []


    def _add_player(self, player_Name):
        """Adds the given player.
        
        Args:
            self (Roster): An instance of Roster.
            player_Name (Player): The players to add.
        """
        if player_Name not in self.players:
            self.players.append(player_Name)
        pass

    def _current_player(self):
        """Gets the current player.
        
        Args:
            self (Roster): An instance of Roster.
        
        Returns:
            Player: The current player.
        """
        return self.players[self.current]


    def _next_player(self):
        """the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """
        self.current = (self.current + 1) % len(self.players)