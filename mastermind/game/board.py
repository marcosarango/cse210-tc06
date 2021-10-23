import random 

class Board:

    def __init__(self):
        self._items = {}


    def _prepare(self, player):

        name = player._get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def _to_string(self, players):
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