from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient, Credentials
from django.conf import settings

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

prompt = "What is the weather like in San Francisco?"

@api_view(['GET'])
def map(request):
    response = model.generate_text(prompt)
    return Response(response)

