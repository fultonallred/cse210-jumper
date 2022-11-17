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
        display_word (list): The list of characters and underscores in the
            word being guessed.
        jumper_parts (list): The current pieces of the jumper
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
        self._display_word = []
        self._jumper_parts = []
        
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
        # Get info from Puzzle and Jumper.
        self._display_word = self._puzzle.get_display_word()
        self._jumper_parts = self._jumper.get_parts()

        # Display info to user and get input.
        self._terminal_service.write_display_word(self._display_word)
        print()
        print()
        self._terminal_service.draw_jumper(self._jumper_parts)
        print()
        print("^^^^^^^")
        
        if self._is_playing:
            self._guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        
    def _do_updates(self):
        """Sends guess to Puzzle and updates Jumper if necessary.

        Args:
            self (Director): An instance of Director.
        """
        # Check if guess is correct.
        correct_guess = self._puzzle.evaluate_guess(self._guess)
        if not correct_guess:
            self._jumper.remove_part()

            

    def _do_outputs(self):
        """Outputs the display word from Puzzle and the jumper from Jumper.

        Args:
            self (Director): An instance of Director.
        """
        # Check for a gameover.
        self._is_playing = self._puzzle.check_solved()
        if self._is_playing:
            self._is_playing = self._jumper.check_alive()

        if not self._is_playing:
            print("\nThanks for playing!")
            self._terminal_service.write_display_word(self._display_word)
            print("\n")
            self._terminal_service.draw_jumper(self._jumper_parts)
            print("\n^^^^^^^")

            
        
        
        

        