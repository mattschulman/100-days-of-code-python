import pandas

#Create the DataFrame from the CSV file
squirrel_data = pandas.read_csv("Squirrel_Data.csv")
#print(squirrel_data['Primary Fur Color'])

#Pick out the "Primary Fur Color" Series and assign to a variable.
fur_colors = squirrel_data["Primary Fur Color"]

#Identify the unique colors in the Series and save to a list.
colors = fur_colors.unique().tolist()
#print(colors)

counts = []

#For each color in the colors list (except the 0 index which is nan), get the count of the color in the fur_colors Series and 
# append to a list
for color in colors[1:]:
    counts.append(fur_colors[fur_colors == color].count())

#print(counts)

#Create a dictionary that has a colors dictionary and a counts dictionary that will be converted into a DataFrame
colors_dict = {
    "colors": colors[1:],
    "counts": counts
}

#Convert the colors_dict dictionary into a Pandas DataFrame and save as a CSV file
color_data = pandas.DataFrame(colors_dict)
#print(color_data)
color_data.to_csv("squirrel_counts.csv")