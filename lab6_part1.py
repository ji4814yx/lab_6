import os
from pprint import pprint
import requests


def create_forecast(data):
    message = data['message']
    if message != 0:
        print('city not found')
    else:

        current_day = 0
        for day in data:
            daily_temp = data['list'][current_day]['main']['temp']
            daily_weather = data['list'][current_day]['weather'][0]['description']
            print(daily_temp)
            print(daily_weather)
            current_day = current_day + 1


key = os.environ.get('WEATHER_KEY')  # none will be returned if not found
success = False  # This because we have not gotten a weather report

while not(success):  # this will repeat forever until we get the city and country code correct

    city = input('Enter desired city: ')
    country = input('Enter associated two-letter country code: ')
    location = city + ',' + country

    forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?'  # this url to get the code from
    query = {'q': location, 'units': 'metric', 'appid': key}  # query with the parameters

    try:  # try to get the forecast date for city and country code
        forecast_data = requests.get(forecast_url, params=query).json()

        if forecast_data['cod'] == '404':  # Checking in if we have an invalid response
            raise Exception('Invalid city or country code.')  # this raises/throws exceptions

        success = True
        pprint(forecast_data)
        create_forecast(forecast_data)

    except Exception as e:  # handle any exception
        print(f'Something is wrong: "{e}"')   # printing the error message
