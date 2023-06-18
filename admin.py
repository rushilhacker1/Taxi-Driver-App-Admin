import math
import requests


def fetch_driver_routes(api_url, auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        driver_data = response.json()
        driver_routes = {driver['name']: driver['location'] for driver in driver_data}
        return driver_routes
    else:
        print('Failed to fetch driver routes:', response.status_code)
        return {}

def generate_auth_token(api_url, username, password):
    auth_url = api_url + '/auth'
    payload = {
        'username': username,
        'password': password
    }
    response = requests.post(auth_url, json=payload)
    if response.status_code == 200:
        auth_token = response.json().get('access_token')
        return auth_token
    else:
        print('Failed to generate auth token:', response.status_code)
        return None

# Example usage

def finddriver(user_cords):

    api_url = 'http://192.168.43.62:5000'
    username = 'johndoe@example.com'
    password = 'password123'
    auth_token = generate_auth_token(api_url, username, password)

    api_url = 'http://192.168.43.62:5000/drivers'
    driver_list = fetch_driver_routes(api_url, auth_token)

    user_cord_list = user_cords.split(",")
    user_x = float(user_cord_list[0])
    user_z = float(user_cord_list[1])

    radius = 12

    matched_drivers = {}

    for driver_name, driver_cords in driver_list.items():
        driver_x, driver_z = map(float, driver_cords.split(","))
        
        distance = math.sqrt((driver_x - user_x) ** 2 + (driver_z - user_z) ** 2)
        if distance <= radius:
            matched_drivers[driver_name] = driver_cords

    return matched_drivers
  
