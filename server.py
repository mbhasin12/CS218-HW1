import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/get-weather')
def getWeather():
    api_key = "4368db269e8f41204a439dfa6b8655d7"
    
    city_name = request.args.get('city')
    country_code = request.args.get('country')

    #print(city_name, country_code)
    # Construct the API endpoint with the necessary parameters
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"
    

    # Make the GET request to the OpenWeatherMap API
    response = requests.get(api_url)
    #print(response)
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON format
        weather_data = response.json()
        # Extract and print the desired information, for example, temperature
        temperature = weather_data['main']['temp']
        return(f"<h1>Current temperature in {city_name}, {country_code} is: {temperature}°C</h1>")
    else:
        
        return("Failed to retrieve weather data")



if __name__ == '__main__':
    app.run(debug=True, port=8001)


