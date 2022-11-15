class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output 
    operations for the terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given 
        prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
        
        
    def write_display_word(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (list): A list of characters and underscores in display_word.
        """
        for i in text:
            print(i, end=" ")

    def draw_jumper(self, parts):
        """Displays the jumper's remaining parts.
        
        Args:
            self (TerminalService): An instance of TerminalService.
            parts (list): A list of strings to draw the jumper with
        """
        for i in parts:
            print(i, sep=" ")