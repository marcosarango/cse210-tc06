class Player:
    """The responsibility of Player is to keep track of their identity and last move

     Stereotype: 
        Information Holder
    
    """

    def __init__(self,name):
        """The class constructor.
        Args:
            self (Player): an instance of Player
        """
        self.player_name = name

    def _get_name(self):
        """Returns the player's name.
        Args:
            self (Player): an instance of Player.
        """
        return self.player_name