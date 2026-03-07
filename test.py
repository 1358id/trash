import requests

# Fetch data from Codeforces API
url = "https://codeforces.com/api/user.info?handles=StelIawinD"
response = requests.get(url)
data = response.json()

# Print current rating
if data['status'] == 'OK':
    rating = data['result'][0]['rating']
    print(f"Your current rating is: {rating}")
else:
    print("Something went wrong")