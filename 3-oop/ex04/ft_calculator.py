class calculator:
    """Class providing operations on two vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Prints the dot product of two vectors

        Args:
            V1 (list[float]):
                first vector
            V2 (list[float]):
                second vector
        """
        dot_product = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is {dot_product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Print element-wise sum of two vectors

        Args:
            V1 (list[float]):
                first vector
            V2 (list[float]):
                second vector
        """
        sum_vector = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {sum_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Print element-wise subtraction of two vectors

        Args:
            V1 (list[float]):
                first vector
            V2 (list[float]):
                second vector
        """
        sub_vector = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is : {sub_vector}")
