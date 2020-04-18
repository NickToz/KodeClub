import requests


def main():
    # print the header
    print_the_header()
    # Get zipcode from user
    postcode = input('What are the first three letters of your postcode (e.g. SE4)? ')
    weather_json = get_html_from_web(postcode)
    # Parse the html
    # Display for the forecast
    print_weather(weather_json, postcode)

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
    print(response.text)
    return response.json()

def print_weather(weather_json, postcode):
    forecast = weather_json['forecasts'][0]['detailed']['reports'][0]['enhancedWeatherDescription']
    temp = weather_json['forecasts'][0]['detailed']['reports'][0]['temperatureC']
    print('The weather in {} is {} and the temperature is {} degrees celcius'.format(postcode,forecast,temp))



if __name__=='__main__':
    main()

