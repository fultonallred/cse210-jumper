from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
        guess (str): The user's current guess.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._guess = None
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Displays info and gets a guess from the user.

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        # Get info from Puzzle and Jumper.
        display_word = self._puzzle.get_display_word()
        jumper_parts = self._jumper.get_parts()

        # Display info to user and get input.
        self._terminal_service.write_display_word(display_word)
        print()
        print()
        self._terminal_service.draw_jumper(jumper_parts)
        self._guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        
        
    def _do_updates(self):
        """Sends guess to Puzzle and updates Jumper if necessary.

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        correct_guess = self._puzzle.evaluate_guess(self._guess)
        if not correct_guess:
            self._jumper.remove_part()

        # Check for a gameover.
        self._is_playing = self._puzzle.check_solved()
        if not self._is_playing:
            return
        self._is_playing = self._jumper.check_alive()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        