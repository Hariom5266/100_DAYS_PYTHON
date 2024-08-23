import requests
from twilio.rest import Client

# API Endpoints and Keys
OBM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = ""  # Replace with your OpenWeatherMap API Key
account_sid = ''  # Replace with your Twilio Account SID
auth_token = ''    # Replace with your Twilio Auth Token

# Weather API Request Parameters
weather_params = {
    "lat": 30.0444,  
    "lon":  31.2357,  
    "appid": api_key,
    "cnt": 4,
}

# Making a request to OpenWeatherMap API
response = requests.get(OBM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain in the next 4 time periods
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    # Check for rain codes (200-599 represent different types of rain in OpenWeatherMap)
    if 200 <= int(condition_code) < 700:
        will_rain = True
        break  # Stop checking further if rain is detected

# Send SMS using Twilio if rain is expected
if will_rain:
    print("Bring an umbrella.")
    
    # Initialize the Twilio client
    client = Client(account_sid, auth_token)
    
    # Sending the SMS
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+',  # Replace with your Twilio phone number
        to='+'  # Replace with the recipient's phone number
    )
    
    # Print the message SID to confirm sending (optional)
    # print(message.sid)
else:
    print("No rain expected.")
