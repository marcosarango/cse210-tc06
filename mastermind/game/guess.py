class Guess:
    """the responsibility is to guess the number that the player enters the game
    
    Stereotype: 
        Information Holder

    """

    def __init__(self):
        """The class constructor
        Args:
            self (Board): an instance of guess.
        """
        
        self.guess = str


    def _get_guess(self):
        """get the number guessed

        Args:
            self (guess): an instance of guess.
        
        """
        return ("What is your guess? ")