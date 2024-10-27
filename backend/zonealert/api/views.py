from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient, Credentials
from django.conf import settings
from noaa_sdk import NOAA
import json

n = NOAA()
observations = n.get_observations('32607', 'US')
weather_info = {
    "temperature": observations['temperature']['value'],
    "wind_speed": observations['windSpeed']['value'],
    "wind_direction": observations['windDirection']['value'],
    "cloud_coverage": observations['textDescription'],
    "visibility": observations['visibility']['value'],
    "humidity": observations['relativeHumidity']['value']
}

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

prompt = {
    "text": "Watson, based on the current weather conditions, what are the safest shelters in Gainesville, Florida?",
    "entities": {
        "location": {
            "value": "Gainesville, Florida"
        },
        "weather": {
            "value": json.dumps(weather_info)  # Include all observations as JSON
        }
    }
}

        # "shelters": {
        #     "value": "list of safe shelters"
        # },

@api_view(['GET'])
def map(request):
    response = model.generate_text(prompt)
    return Response(response)

