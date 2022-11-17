class Jumper:
    """Jumper has a parachute that gets clipped away as the player makes
    incorrect guesses.
    
    Attributes:
        parts (list): a list of jumper parts
    """
    def __init__(self):
        """Constructs a new instance of Jumper.
        
        Args:
            self (Jumper): and instance of Jumper
        """
        self._parts = [" ___", "/___\\", "\\   /", " \\ /", "  O", " /|\\", " / \\"]

    def remove_part(self):
        """Removes a piece of the jumper from top to bottom.
        
        Args:
            self (Jumper): an instance of Jumper"""
        self._parts.pop(0)

    def check_alive(self):
        """Checks if the jumper is alive and returns true or false.
        
        Args:
            self (Jumper): an instance of Jumper
            
        Return:
            alive (boolean): Whether Jumper is alive
        """
        alive = (len(self._parts) > 3)
        if not alive:
            self._parts[0] = "  X"
        return alive

    def get_parts(self):
        """Returns the Jumper's parts.
        
        Args:
            self (Jumper): an instance of Jumper
        """
        return self._parts