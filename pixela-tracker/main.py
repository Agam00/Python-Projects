import os
import requests
from datetime import datetime

# Load sensitive info from environment variables
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

# Base Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# User creation (only run once)
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Graph creation (only run once)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Studying",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}
headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add a pixel
today = datetime(year=2025, month=9, day=22)
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}
response = requests.post(url=pixel_endpoint, json=pixel_param, headers=headers)
print(response.text)

# Update pixel for today
today = datetime.now()
put_endpoint = f'{pixel_endpoint}/{today.strftime("%Y%m%d")}'
update_param = {"quantity": "2"}
response = requests.put(url=put_endpoint, json=update_param, headers=headers)
print(response.text)

# Delete pixel (optional)
response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
