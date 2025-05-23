import requests

API_key = "6b67b15b93b5c86ec6436f230c0a561f"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return temp, description
    else:
        return None, data.get('message', 'Unable to fetch weather data')