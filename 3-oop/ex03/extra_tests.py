from ft_calculator import calculator

# negative scalar
v = calculator([1, 2, 3])
v + (-5)  # [-4, -3, -2]
v * (-2)  # [8, 6, 4]

# decimal scalar
v = calculator([1, 2, 3])
v / 2  # [0.5, 1.0, 1.5]

# mutation
v = calculator([1, 2, 3])
v + 1  # [2, 3, 4]
v + 1  # [3, 4, 5]
print(v.vector)  # [3, 4, 5]

# empty vector
v = calculator([])
v + 5  # []
v * 2  # []

# invalid constructor
v = calculator("hello")
# Error: Numbers should be int/float and in a list.
# Empty list created in class
print(v.vector)  # []

# invalid scalar
v = calculator([1, 2, 3])
v + "abc"  # Error: Scalar should be int or float
v * [1]  # Error: Scalar should be int or float

# division by 0
v = calculator([1, 2, 3])
v / 0  # Error: Division by 0
