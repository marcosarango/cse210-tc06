from typing_extensions import ParamSpecArgs
from game.board import Board
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.console import Console


class Director:

    def __init__(self):
        self._board = Board()
        self._roster = Roster()
        self._guess = Guess()
        self._console = Console()


    def start_game(self):
        pass

    def _prepare_game(self):
        pass

    def _get_input(self):
        pass

    def _do_updates(self):
        pass

    def _do_output(self):
        pass
