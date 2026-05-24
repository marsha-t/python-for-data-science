from S1E9 import Character


class Baratheon(Character):
    """Class representing a member of House Baratheon"""

    def __init__(self, first_name, is_alive=True):
        """
        Initialise a Baratheon character

        Args:
            first_name (str):
                character's first name
            is_alive (bool):
                character living state; defaults is True
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return string representation of Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return object representation of Baratheon character"""
        return str(self)


class Lannister(Character):
    """Class representing a member of House Lannister"""

    def __init__(self, first_name, is_alive=True):
        """
        Initialise a Lannister character

        Args:
            first_name (str):
                character's first name
            is_alive (bool):
                character living state; defaults is True
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return string representation of Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return object representation of Lannister character"""
        return str(self)

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create and return a Lannister character.

        Args:
            first_name (str):
                Character's first name.
            is_alive (bool):
                Character's living state.

        Returns:
            Lannister:
                A new Lannister instance.
        """
        return cls(first_name, is_alive)
