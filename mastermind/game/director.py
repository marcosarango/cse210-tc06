
from game.board import Board
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:
    """ A code template that directs the game. The responsibility of this 
    class of objects is to control the sequece of play. 

    stereotype:
        controller

    attributes:
        board: an instance of the class of objects known as board. 
        console: an instance of the class of objects known as console. 
        roster: an instance of the class of objects known as roster
        guess: an instance of the class of objects known as guess
        player: an instance of the class of objects known as player

    """
    def __init__(self):
        """ The class constructor.

        Args:
            self (Director): an instance of Director
        
        """
        
        self._board = Board()
        self._roster = Roster()
        self._guess = Guess()
        self._console = Console()
        self._keep_playing = True

    def start_game(self):
        """This method control the sequence of play"""

        self._prepare_game()
        while self._keep_playing == True:
            self._get_input()
            self._do_updates()
            self._do_output()



    def _prepare_game(self):
        """In this Method adds the player names and adds them to the roster.
        
        Args:
           self (Director): An instance of Director
        """

        for i in range(2):
            player_Name = self._console._read(f"Enter username player {i + 1}: ")
            player = Player(player_Name)
            self._roster._add_player(player_Name)
            self._board._prepare(player)

        

    def _get_input(self):
        """
        This method show the inputs of each round of play. 
        That means getting the move from the current player

        Args:
             self (Director): An instance of Director.
        """
        self._console._write(self._board._to_string(self._roster.players))
        current_player = self._roster._current_player()
        self._console._write(f"{current_player.capitalize()}'s turn:")
        guess_valid = False
        while guess_valid == False:
            player_guess = self._console._read(self._guess._get_guess())
            guess_valid = self._console._check_guess(player_guess)   
        self._guess.guess = player_guess
        self._board._items[current_player][1] = player_guess

    def _do_updates(self):
        """
        Update every change in every game round.
        Args:
            self (Director): An instance of Director.
        
        """
        code = self._board._items[self._roster._current_player()][0]
        self._board._items[self._roster._current_player()][2] = self._board._create_hint(code, self._guess.guess)
       

    def _do_output(self):
        """
        Display important information in each round of the game.
        Args:
            self (Director): An instance of Director.
        """
        if self._console._check_if_win(self._board._items[self._roster._current_player()][2]) == True:
            message = (f"{self._roster._current_player().capitalize()} is the winner")
            self._console._write(message)
            self._keep_playing = False
        else:
            self._roster._next_player()
