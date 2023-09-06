#Open up the weather data file and read in each line as a separate item in a list
#
# data = []
# with open("weather_data.csv") as weather_file:
#     data = weather_file.read().splitlines()
# print(data)

#Use CSV Module - however working with columns and rows is a pain.  Pandas can help
#
# import csv
# temps = []
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     print(data)
#     for row in data:
#         print(row)
#         #Skip the header row and extract the temps as integers and append to new list
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)


#Do the above but with Pandas - print out the Temps column
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#
# the output of the read_csv funciton is of type DataFrame - kind of like a worksheet
#
#print(type(data))
#
#A column in a Panda object is called a series.
#
#print(type(data["temp"]))

# Use a Dataframe function to convert it to a python dictonary
#
#data_dict = data.to_dict()
#print(data_dict)

#Use a Series function to convert it to a python list
#temps = data["temp"].to_list()
#print(temps)

# Find the average temp - could do it by taking the sum of the temps divided by length of temps list, or use the Series mean() function
#
#avg_temp = data["temp"].mean()
#print(avg_temp)

#Find the max temp using the Series max() function
#
#max_temp = data["temp"].max()
#print(max_temp)

#Get data from columns.  Panda will make column names an attribute
#rint(data["condition"])
#or
#print(data.condition)

#Get data from rows.  This is saying print data where data.day == Monday
#
#print(data[data.day == "Monday"])

#Get  the row that has the highest temp.
#print(data[data.temp == data.temp.max()])

#Set a variable to be a specific row, then use that variable to get a specific field.  Convert monday's temp to degrees F
#monday = data[data.day == "Monday"]
#print(monday.condition)
#tempf = (monday.temp[0]*9/5)+32
#print(tempf)

#Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
#Save DataFrame to a CSV file
data.to_csv("student_database.csv")