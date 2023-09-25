#Use the : to declare the data type and it can be used later
# age: int
# name: str
# height: float
# is_human: bool

#You can decalare the type for the argument by using :
#Define the datatype of the output using ->  
#These are Type Hints
def police_check(age: int) -> bool:
    if age > 10:
        can_drive = True
    else:
        can_drive = False
    return can_drive

#Passing an integer works, but if you try and pass a string, a TypeError will be thrown.
#Showing that the parameter needs to be an int will help prevent this.
if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")