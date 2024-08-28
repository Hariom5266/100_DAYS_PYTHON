import requests
from twilio.rest import Client

# Configuration Constants
SHEETY_API_URL = "https://api.sheety.co/YOUR_SHEETY_PROJECT_ID/YOUR_SHEET_NAME"  # Sheety API URL
AMADEUS_API_KEY = "YOUR_AMADEUS_API_KEY"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
USER_PHONE_NUMBER = "YOUR_PHONE_NUMBER"  # Your phone number to receive SMS

# Function to get data from Sheety
def get_flight_data():
    response = requests.get(SHEETY_API_URL)
    if response.status_code == 200:
        return response.json()['YOUR_SHEET_NAME']  # Adjust this based on your sheet name
    else:
        print(f"Error fetching data from Sheety: {response.status_code}, {response.text}")
        return []

# Function to search for flights using Amadeus API
def search_flights(iata_code):
    amadeus_api_url = f"https://api.amadeus.com/v2/shopping/flight-offers"
    
    # Obtain access token from Amadeus API
    token_response = requests.post(
        "https://test.api.amadeus.com/v1/security/oauth2/token",
        data={"grant_type": "client_credentials"},
        auth=(AMADEUS_API_KEY, "YOUR_AMADEUS_API_SECRET")  # Replace with your Amadeus API Secret
    )

    if token_response.status_code != 200:
        print("Error obtaining access token")
        return []
    
    access_token = token_response.json()['access_token']
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    params = {
        "originLocationCode": iata_code,
        "destinationLocationCode": "YourDestinationIATA",  # Define a destination or read from the sheet
        "departureDate": "2024-08-25",  # Define the departure date
        "adults": 1,
        "maxPrice": 1000  # Optional: max price filter
    }

    response = requests.get(amadeus_api_url, headers=headers, params=params)

    if response.status_code == 200:
        flight_offers = response.json().get('data', [])
        return flight_offers
    else:
        print(f"Error fetching flight data: {response.status_code}, {response.text}")
        return []

# Function to send SMS using Twilio
def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print(f"Message sent: {message.sid}")

# Main execution flow
if __name__ == "__main__":
    flight_data = get_flight_data()

    for entry in flight_data:
        city = entry['City']
        iata_code = entry['IATA Code']
        predefined_price = entry['Price']

        # Search for flights
        flights = search_flights(iata_code)

        for flight in flights:
            flight_price = flight['price']['total']  # Adjust based on API response structure
            if flight_price < predefined_price:
                # Send SMS notification
                sms_message = f"Cheaper flight found for {city}: ${flight_price}"
                send_sms(sms_message)
                break
