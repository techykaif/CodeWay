import requests
def get_weather_forecast(city, api_key):
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast = {
            'city': data['location']['name'],
            'country': data['location']['country'],
            'temperature': data['current']['temp_c'],
            'description': data['current']['condition']['text'],
        }
        return forecast
    else:
        print("Error Fetching Weather Forecast")
        return None

api_key = '6d543634252d432bacd123232241304'
city = input("Enter Your City : ")
forecast = get_weather_forecast(city, api_key)
if forecast is not None:
    print(f'The current temperature in {forecast["city"]}, {forecast["country"]} is {forecast["temperature"]}°C with {forecast["description"]}.')