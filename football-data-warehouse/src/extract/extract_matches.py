import requests

def extract_data():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    return response.json()