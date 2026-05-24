from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King character"""

    def __init__(self, first_name, is_alive=True):
        """Initialise a King character"""
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        """Get eye colour"""
        return self.__dict__["eyes"]

    @eyes.setter
    def eyes(self, colour):
        """Set eye colour"""
        allowed = ["blue", "brown"]
        if colour not in allowed:
            print("Error: Impossible eye colour")
            return
        self.__dict__["eyes"] = colour

    @property
    def hairs(self):
        """Get hair colour"""
        return self.__dict__["hairs"]

    @hairs.setter
    def hairs(self, colour):
        """Set hair colour"""
        allowed = ["light", "dark"]
        if colour not in allowed:
            print("Error: Impossible hair colour")
            return
        self.__dict__["hairs"] = colour

    def get_eyes(self):
        """Get eye colour"""
        return self.eyes

    def set_eyes(self, colour):
        """Set eye colour"""
        self.eyes = colour

    def get_hairs(self):
        """Get hair colour"""
        return self.hairs

    def set_hairs(self, colour):
        """Set hair colour"""
        self.hairs = colour
