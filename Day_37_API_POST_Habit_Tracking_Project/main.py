import requests
#from datetime import date,timedelta

USERNAME = <<username>>
TOKEN = <<token>>
GRAPH = "graph1"

# Create a user on pixe.la
pixela_users_endpoint="https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }


# response = requests.post(url=pixela_users_endpoint, json=user_params)
# print(response.text)

# Create a Graph on pix.la
pixela_graph_endpoint = f"{pixela_users_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH,
#     "name": "Rowing Graph",
#     "unit": "meters",
#     "type": "int",
#     "color": "sora",
#     "timezone": "America/New_York",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

#Post a pixel on the graph
pixel_endpoint = f"{pixela_graph_endpoint}/{GRAPH}"

# today = date.today()
# yesterday = today - timedelta(days=2)
# yesterday_string = yesterday.strftime("%Y%m%d")

date = input("Enter Date (YYYYMMDD): ")
meters = input("Enter number of meters rowed: ")

body = {
    "date": date,
    "quantity": meters,
}

response = requests.post(url=pixel_endpoint,json=body, headers=headers)
print(response.text)


#Update a pixel
#pixel_change_endpoint = f"{pixel_endpoint}/{yesterday_string}"

# body = {
#     "quantity": "6000"
# }

# response = requests.put(url=pixel_change_endpoint,json=body, headers=headers)
# print(response.text)

# Delete a pixel

# response = requests.delete(url=pixel_change_endpoint, headers=headers)
# print(response.text)