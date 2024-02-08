def test_home_endpoint(client):
    response = client.get('/')  # Use the test client to make requests
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '<h1>Hello, World!</h1>'

def test_get_weather(client):
    response = client.get('/get-weather?city=San Francisco&country=USA')
    assert response.status_code == 200

def test_bad_get_weather(client):
    response = client.get('/get-weather?city=fjaskflja&country=fjaskflja')
    assert response.data.decode('utf-8') == 'Failed to retrieve weather data'
    
