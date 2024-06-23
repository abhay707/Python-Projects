import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "90dd4193af167b7b53ce751dfa1226c2"
account_sid = 'AC0d2bc416f6962fbe7f5927c295d83b65'
auth_token = 'e8b85cfab8f6853ff9999600bdb1e0ce'


weather_params = {
    "lat": 31.326059,
    "lon": 75.575623,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][0:12]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella",
        from_='+12295972066',
        to='+919993475853'
    )
    print(message.status)