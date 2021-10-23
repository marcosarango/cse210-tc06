import random 

class Board:
    """
    The responsibility is to keep track of the game
    """

    def __init__(self):
        """the class instructor"""
        self._items = {}


    def _prepare(self, player):
        """The _prepare method sets up the board
        args:
           self (screen): An instance of Screen.
           player (string): show the player's name
        """

        name = player._get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def _to_string(self, players):
        """The to_string method converts the board data to its string representation and returns it to the caller. 
        
        args:
           self (screen): An instance of Screen.
           players (string): show the name of the players
        returns:
           text: the players and the dashed lines
        
        """
        text = ("\n--------------------")
        for player in players:
            text += (f"\nPlayer {player.capitalize()}: {self._items[player][1]}, {self._items[player][2]}")
        text += "\n--------------------"

        return text

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint