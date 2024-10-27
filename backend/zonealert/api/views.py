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
  params={"max_new_tokens": 100}
)

# prompt = {
#     "text": "Watson, based on the current weather conditions, what are the safest shelters in Gainesville, Florida?",
#     "entities": {
#         "location": {
#             "value": "Gainesville, Florida"
#         },
#         "shelters": {
#             "value": "list of safe shelters"
#         },
#         "weather": {
#             "value": 
#         }
#     }
# }

prompt = (f"Current weather in {weather_data['city']}:\n"
              f"Temperature: {weather_data['temperature']}°F\n"
              f"Pressure: {weather_data['pressure']} hPa\n"
              f"Humidity: {weather_data['humidity']}%\n"
              f"Description: {weather_data['description']}\n"
              "Is it safe to go outside?")

@api_view(['GET'])
def map(request):
    response = model.generate_text(prompt)
    return Response(response)

