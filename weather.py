import requests

def request_city():
    city = input("Where in the world are you? ")
    while city == '':
        city = input("Where in the world are you? ")
    if " " in city:
        city = city.replace(" ", "%20")
    try:
        r = requests.get(f"https://www.metaweather.com/api/location/search/?query={city}")
        woeid = r.json()[0]["woeid"]
    except requests.exceptions.InvalidURL:
        print("Incorrect name")
    except IndexError:
        print("Wrong Index")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
    try:
        weather = requests.get(f"https://www.metaweather.com/api/location/{woeid}")
        return weather.json(), city
    except IndexError:
        print("Wrong Index")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
    except NameError:
        print("Name Error")


def get_forecast():
    weather_dict, city = request_city()
    print(f"Weather for {city}")
    print(f"{'Date':<20}{'Conditions':<20}{'Max Temperature':<20}{'Min Temperature':<20}")
    for forecast in weather_dict['consolidated_weather']:
        date = forecast['applicable_date']
        conditions = forecast['weather_state_name']
        max_temp = forecast['max_temp']
        min_temp = forecast['min_temp']
        print(f"{date:<20}{conditions:<20}{max_temp:<20.2f}{min_temp:<20.2f}")
    

get_forecast()
