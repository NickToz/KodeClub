import requests
import sqlite3
import datetime
conn = sqlite3.connect('weather.db')
c = conn.cursor()

def main():
    print_weather_history()
    # print the header
    print_the_header()
    # Get zipcode from user
    postcode = input('What are the first three letters of your postcode (e.g. SE4)? ')
    weather_json = get_html_from_web(postcode)
    # Parse the html
    # Display for the forecast

    print_weather(weather_json, postcode)
    save_weather(weather_json, postcode)

def print_the_header():
    print('--------------------------------------------------------------')
    print('                      UK WEATHER APP')
    print('--------------------------------------------------------------')
    print()

def get_zip():
    postcode = input('What are the first three letters of your postcode (e.g. SE4)? ')


def get_html_from_web(postcode):
    url = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{}'.format(postcode)
    print(url)
    response = requests.get(url)
    # print(response.text)
    return response.json()

def print_weather(weather_json, postcode):
    forecast = weather_json['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription']
    temp = weather_json['forecasts'][0]['detailed']['reports'][0]['temperatureC']
    print('The weather in {} is {} and the temperature feels like {} degrees celcius'.format(postcode,forecast,temp))

def save_weather(weather_json, postcode):
    forecast = weather_json['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription']
    temp = weather_json['forecasts'][0]['detailed']['reports'][0]['temperatureC']
    # Insert a row of data
    c.execute("INSERT INTO weather VALUES (?, ?, ?, ?)", (datetime.datetime.utcnow(), postcode, forecast, temp))
    conn.commit()
    print ("saved")

def print_weather_history():
    c.execute("SELECT * FROM weather")
    for row in c.fetchall():
        print (row)

if __name__=='__main__':
    main()

