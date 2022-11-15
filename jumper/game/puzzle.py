import random

class Puzzle:
    """Puzzle is a hidden word that the player must guess one letter at a
    time.
    
    Attributes:
        word_list (list): a list of possible words to be guessed
        hidden_word (str): the randomly-selected word to be guessed
        display_word (list): correct guesses mixed with underscores
    """

    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle
        """
        self._word_list = ["dog", "cat", "mouse", "frog"]
        self._hidden_word = ""
        self._display_word = []
        self._incorrect_guesses = ""

        # Choose a random word.
        self._hidden_word = random.choice(self._word_list)

        # Fill the display word with underscores.
        for _ in range(len(self._hidden_word)):
            self._display_word.append("_")

    def evaluate_guess(self, guess):
        """Checks if the guess is a letter in the hidden word and, if so, adds
        letter to display_word.
        
        Args:
            self (Puzzle): an instance of Puzzle
            guess (str): a letter from the user

        Return:
            in_word (boolean): whether the guess is in the hidden word or not
        """
        in_word = (guess in self._hidden_word)

        if in_word:
            index = self._hidden_word.index(guess)
            self._display_word[index].append(guess)

        return in_word

    def check_solved(self):
        """Checks if the puzzle is solved.
        
        Args:
            self (Puzzle): an instance of Puzzle

        Return:
            solved (boolean): whether Puzzle is solved
        """
        solved = ("_" not in self._display_word)
        return solved

    def get_display_word(self):
        """Returns display word.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._display_word