ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Lists: mutable & ordered
ft_list[1] = "World!"

# Tuple: immutable & ordered
ft_tuple = (ft_tuple[0], "UAE!") # Create new tuple

# Set: mutable, unordered, unique values only
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!") # Note: Order not guaranteed

# Dictionary: mutable key/value mapping
ft_dict["Hello"] = "42AbuDhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)