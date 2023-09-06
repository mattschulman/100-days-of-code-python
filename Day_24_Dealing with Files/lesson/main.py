# Manual method of opening, reading, and closing a file
#
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#Using the with method and a File handler so it automatically closes the file when done.  Default mode is "r" or read only
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Write to a file - mode "w" will replace the entire file.  mode "a" will append to existing text.
#
# with open("my_file.txt","a") as file:
#     file.write("\nNew text.")

# If you open a file for writing that doesn't exist, it creates it.
#
with open("new_file.txt","w") as file:
    file.write("New text.")