import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        users = response.json()
        return users
    except requests.exceptions.RequestException as e:
        print("Error fetching user data:", e)
        return []