# Dictionaries and sets are un-ordered while lists and tuples are ordered
# Dictionaries are accessed by keys and not by index
# Keys in dictionaries are immutable. Hence, we can use tuples as keys in dictionaries but not lists

fruit = { "apple" : "crunchy and red",
          "orange": "citrus and orange",
          "lemon": "citrus and green",
          "grape":"grows on bunches"
        }

print(fruit)
print(fruit["lemon"]) # this is how you access the values in dictionary by using a key
fruit["pear"]="round and orange/red in color"  # this is how you would add a new key-value pair to a dictionary
print(fruit)
del fruit["pear"] # this is how you would remove a particular key-value pair
print(fruit)
#fruit.clear() # this would delete all the elements of the dictionary

print(fruit.__getitem__("grape")) #this is another way of accessing the values in dictionary by using a key