import requests

# request to add country to database
url = 'http://localhost:5000/add_country'
data = {'name': 'Slovenia'}
response = requests.post(url, json=data)
print(response.json())

# request to show all country to database
url = 'http://localhost:5000/get_countries'
response = requests.get(url)
countries = response.json()
print(countries)
