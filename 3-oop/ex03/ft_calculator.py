class calculator:
    """Class for a calculator that performs scalar operations on a vector"""

    def __init__(self, vector):
        """
        Initialisation of calculator

        Args:
            vector (list[int | float]):
                vector of numbers

        Notes:
            Prints error message if vector is not a list of numbers.
                Created calculator contains empty list
        """
        if (
            isinstance(vector, list)
            and all(
                isinstance(element, (int, float)) for element in vector
            )
        ):
            self.vector = vector.copy()
            # in case input list already referenced elsewhere
        else:
            print(
                "Error: Numbers should be int/float and in a list. "
                "Empty list created in class"
            )
            self.vector = []

    def __add__(self, object) -> None:
        """
        Add scalar value to vector of numbers

        Args:
            object (int | float):
                scalar value to add

        Notes:
            Prints error message if scalar value is not a number
        """
        if not isinstance(object, (int, float)):
            print("Error: Scalar should be int or float")
            return
        self.vector = [element + object for element in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiply values in vector by a scalar

        Args:
            object (int | float):
                scalar value to multiply by

        Notes:
            Prints error message if scalar value is not a number
        """
        if not isinstance(object, (int, float)):
            print("Error: Scalar should be int or float")
            return
        self.vector = [element * object for element in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtract scalar value from vector of numbers

        Args:
            object (int | float):
                scalar value to subtract

        Notes:
            Prints error message if scalar value is not a number
        """
        if not isinstance(object, (int, float)):
            print("Error: Scalar should be int or float")
            return
        self.vector = [element - object for element in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divide values in vector by a scalar

        Args:
            object (int | float):
                scalar value to divide by

        Notes:
            Prints error message if
                - scalar value is not a number
                - scalar value equals to 0
        """
        if not isinstance(object, (int, float)):
            print("Error: Scalar should be int or float")
            return
        if object == 0:
            print("Error: Division by 0")
            return
        self.vector = [element / object for element in self.vector]
        print(self.vector)
