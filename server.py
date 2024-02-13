import requests
from flask import Flask, jsonify
from flask import request
import os
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
swagger(app)

# Swagger config
SWAGGER_URL = '/api/docs'  
API_URL = '/spec'  
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Weather App"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/spec')
def spec():
    """
    Swagger specification for our API.
    ---
    responses:
      200:
        description: Swagger specification for our API.
    """
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Weather App"
    return jsonify(swag)


@app.route('/')
def hello():
    """
    Simple endpoint to see if server is working. Returns Hello World in h1 tags.
    ---
    tags:
      - Welcome
    
    
    """
    return '<h1>Hello, World!</h1>'

@app.route('/get-weather')
def getWeather():
    """
    Get current weather information for a specified city and country.

    This endpoint retrieves current weather data from the OpenWeatherMap API. It requires a city name and country code as query parameters.

    ---
    tags:
      - Weather
    parameters:
      - name: city
        in: query
        type: string
        required: true
        description: The name of the city to retrieve weather information for.
      - name: country
        in: query
        type: string
        required: true
        description: The ISO country code for the specified city.
    responses:
      200:
        description: An object containing the current temperature and other weather details.
        schema:
          type: object
          properties:
            temperature:
              type: number
              description: Current temperature in Celsius.
            description:
              type: string
              description: Weather condition description.
      400:
        description: Invalid request, such as missing or incorrect query parameters.
      500:
        description: Internal server error or OpenWeatherMap API service failure.
    """
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
    
    app.run(debug=True, host='0.0.0.0', port=80)


