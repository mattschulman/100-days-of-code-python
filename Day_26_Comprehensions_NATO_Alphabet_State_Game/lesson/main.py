#For loop method to take list and add 1 to each number in the list together and generate a new list.
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#   add_1 = n + 1
#   new_list.append(add_1)
# print(new_list)

#Above done as a list comprehension
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

#String comprehension - creates a list of each letter in the string
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

#range comprehension with a range instead of a list
# new_range = [num * 2 for num in range(1,5)]
# print(new_range)

#Conditional list comprehension - only add the name to the list if it has less than 5 chars
#new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# upper_case_long_names = [n.upper() for n in names if len(n) > 5]
# print(upper_case_long_names)

#Dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
#Generate a dictionary of student names from names list and a random score
# import random
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

#Generate a dictionary of student names and scores if the score > = 60
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed_students)

#Iterate over Pandas DataFrames

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

# Loop through the dictionaries
# for (key,value) in student_dict.items():
#     #print(key)
#     print(value)

import pandas
student_dataframe = pandas.DataFrame(student_dict)
#print(student_dataframe)

# use traditional for loop to iterate through the DataFrame.  Printing the keys works, but printing the values results in a Series
# for key,value in student_dataframe.items():
#     print(key)
#     print(value)

#Pandas has an built-in loop called iterrows() which is also a series.  You can then reference the column name
for (index, row) in student_dataframe.iterrows():
    #print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)

