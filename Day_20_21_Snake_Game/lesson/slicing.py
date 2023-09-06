piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

#Print the 3rd through 5th item in the list.  Since first item starts at index 0, the starting index is 1 less, 
#but the ending index is the same
print(piano_keys[2:5])

#Print the 3rd item though the end of the list.  Leave off the end index, but include the :
print(piano_keys[2:])

#Print everything up to the 5th item in the list, leave off the first endex, but include the :
print(piano_keys[:5])

#You can also set an increment in the slice.  Print every other item in the list between the 3rd and 5th items.
print(piano_keys[2:5:2])

#Print every other item in the list.  leave off the start and end indexes.
print(piano_keys[::2])

#The increment can be a negative number.  This means go in reverse.  This is how you can reverse a list
print(piano_keys[::-1])

#slicing works with tuples as well
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[2:5])

