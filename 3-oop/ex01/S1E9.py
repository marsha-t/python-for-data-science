from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise a character

        Args:
            first_name (str):
                character's first name
            is_alive (bool):
                character living state; default is True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Set character state to dead
        """
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        """
        Return string representation of character
        """
        pass


class Stark(Character):
    """
    Class representing member of House Stark
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise a Stark character

        Args:
            first_name (str):
                character's first name
            is_alive (bool):
                character living state; defaults is True
        """
        super().__init__(first_name, is_alive)

    def __str__(self):
        """
        Return family name
        """
        return "Stark"
