import requests
Key = "2c1b151a651a694c40970873e2b1b290"

def search_city(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={Key}&limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        if len(response.json()) == 1:
            return response.json()[0]
        else:
            for i, city in enumerate(response.json()):
                print(f'{i+1}. {city["name"]}, {city["country"]}')
            print("Multiple matches found, which city did you mean?")
            return response.json()[int(input("> "))-1]
    else:
        print(f"Error: {response.status_code}")     

    
def weather_forecast(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly&appid={Key}"
    response = requests.get(url)
    if response.status_code == 200:
        daily_forecast = response.json()['list'][::8]
        execute_forcast = []
        for i in daily_forecast:
            forcast = {}
            forcast['date'] = i['dt_txt'][:10]
            forcast['weather'] = i["weather"][0]["main"]
            forcast['temp'] = int(i["main"]["temp"]- 273.15)
            execute_forcast.append(forcast)
        return execute_forcast

    else:
        print(f"Error: {response.status_code}")

def main():
    while True:
        print("City?")
        city = search_city(input("> "))
        daily_forecast = weather_forecast(city["lat"], city["lon"])
        print(f"Here's the weather in {city['name']}")
        for i in daily_forecast:
            print(f'{i["date"]}: {i["weather"]} {i["temp"]}°C')

if __name__ == "__main__":
    main()
