import requests
from watson_developer_cloud import NaturalLanguageUnderstandingV1

# Weather API credentials
weather_api_key = "WEATHER_API_KEY"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

# Watson AI credentials
watson_api_key = "WATSON_API_KEY"
watson_api_url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com"

# Fetch weather data from API
weather_response = requests.get(weather_api_url, params={"q": "London, UK", "appid": weather_api_key})

# Send weather data to Watson AI for analysis
nlu = NaturalLanguageUnderstandingV1(
    version="2019-07-12",
    iam_api_key=watson_api_key,
    url=watson_api_url
)

analysis = nlu.analyze(
    text=weather_response.json()["weather"][0]["description"],
    features=["entities", "sentiment"]
).get_result()