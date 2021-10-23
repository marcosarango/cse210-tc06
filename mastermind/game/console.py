class Console:
    """
    The responsibility of this class of objects is to get text or numerical input and display text output
    

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        message (string): The messege to display on each line.
        text (string): the text to display on each line.
        guess (number): the guess to display on each line.

    """

    def _read(self, message):
        """
        Gets messege input from the user through the screen.

         Args: 
            self (Screen): An instance of Screen.
            message (string): The message to display to the user.

        
        Returns:
            string: The user's input as message
        
        """
        return input(message)



    def _write(self, text):
        """Displays the given text on the screen. 
        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        
        Returns:
            string: The user's input as an text.
        """
        return print(text)

    def _check_guess(self, guess):
        """
        Ensure that the number digits are correct.

        Args: 
            self (Screen): An instance of Screen.
            guess (string): The guess to display to the user.

        Returns:
            bool: The user's input as an bool.
        
        """
        if len(guess) != 4:
            return False

        else:
            return True
        

    def _check_if_win(self, hint):
        """ Show the winner of the game.
        Args: 
            self (Screen): An instance of Screen.
            hint (string): The hint to display xxxx.
         Returns:
            bool: The user's input as an bool.
        """
        if hint == "xxxx":
            return True
        else:
            return False
