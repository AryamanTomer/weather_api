import requests
api_key = "22e31e1a542bf11aef156b09107692f9"

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Write your city:")

response = requests.get(
    url=api_url,
    params={
        "q": city,
        "appid": api_key,
        "units":"metric",
    }    
)

weather_data = response.json()
print(city, "has a temperature of",weather_data['main']['temp'])