from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient, Credentials
from django.conf import settings
import requests

def get_weather(city):
    api_key = settings.WEATHER_API_KEY  # Replace with your OpenWeather API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        return {
            "city": city,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "description": description.capitalize()
        }
    else:
        print("Error:", response.status_code, response.json())
        return None
    
weather_data = get_weather("Gainesville, Florida")

credentials = Credentials(
    url = "https://us-south.ml.cloud.ibm.com",
    api_key = settings.DEREK_WATSON_API_KEY
)

client = APIClient(credentials)

model = ModelInference(
  model_id="ibm/granite-13b-chat-v2",
  api_client=client,
  project_id= settings.PROJECT_ID,
  params={"max_new_tokens": 1000}
)

# # Shelters information
shelters = [
    {
        "name": "GRACE Marketplace",
        "latitude": 29.680760,
        "longitude": -82.309170,
        "good_for": ["Cold shelter", "Severe weather shelter"]
    },
    {
        "name": "Southwest Recreation Center",
        "latitude": 29.638060,
        "longitude": -82.368553,
        "good_for": ["Severe weather shelter", "Flood-prone areas", "Substandard housing"]
    },
    {
        "name": "The Martin Luther King Jr. Multipurpose Center",
        "latitude": 29.661190,
        "longitude": -82.307790,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "The Easton-Newberry Sports Complex",
        "latitude": 29.669300,
        "longitude": -82.602410,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "Saint Francis House",
        "latitude": 29.648080,
        "longitude": -82.324610,
        "good_for": ["Cold shelter"]
    },
    {
        "name": "FW Buchholz Senior HS",
        "latitude": 29.67776870727539,
        "longitude": -82.40684509277344,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "Santa Fe HS",
        "latitude": 29.8037703,
        "longitude": -82.5231457,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "Easton-Newberry Sports Complex",
        "latitude": 26.1773507,
        "longitude": -80.1628684,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "Marjorie K Rawlings ES",
        "latitude": 29.6846141,
        "longitude": -82.3074232,
        "good_for": ["Severe weather shelter"]
    },
    {
        "name": "Waldo Community School",
        "latitude": 29.791079,
        "longitude": -82.174658,
        "good_for": ["Severe weather shelter"]
    },
]

# Format shelter information
shelters_info = "\n".join(
    [f"{shelter['name']} (Latitude: {shelter['latitude']}, Longitude: {shelter['longitude']}) - Good for: {', '.join(shelter['good_for'])}" for shelter in shelters]
)

# Weather data for the prompt
prompt = (
    f"Current weather in {weather_data['city']}:\n"
    f"Temperature: {weather_data['temperature']}°F\n"
    f"Pressure: {weather_data['pressure']} hPa\n"
    f"Humidity: {weather_data['humidity']}%\n"
    f"Description: {weather_data['description']}\n\n"
    "Based on the current weather conditions, please recommend THREE of the safest shelters in Gainesville, Florida.\n"
    "Provide their names along with locations (latitude and longitude) in a clear format:\n\n"
    f"Here is a list of available shelters:\n{shelters_info}\n"
    "Make sure the response is structured in json format."
)

@api_view(['GET'])
def map(request):
    response = model.generate_text(prompt)
    return Response(response)

