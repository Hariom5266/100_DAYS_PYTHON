# 🍵 , Hanji Kaise ho aap sabhi this is 39th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# -------------------- CASPTONE PROJECT  -------------------- #

# Cheap Flight Finder
# it is help to find cheap filght

# KAYAKA -- Flight search website

# We have gogle sheet that tracke locations which we want to visit and price

# Search in Flight Search API and search for cheapest flight in 6 month and date & Price

# If the price of flight is chape for our expected price then it send us sms and details of flight

# SpredSheets
# City                IATA Code                   Lowest Price
#  10 records 

######################################## FLOW OF CODE  ########################################

# First Make a google sheet which have below listed Column
# -- City 
# -- IATA Code
# -- Price

# Then take it and search in flight search api 
# API -- https://developers.amadeus.com/

# search flight for that place 
# if price of that flight of todat in api is lower than our predefine price then send sms to the use using willio

# --------------------------------------------------------------------------------------------------------------------------------

# Step 2: Create a Google Sheet
# Create a Google Sheet:

# Go to Google Sheets and create a new spreadsheet.
# Add the following columns:
# City
# IATA Code
# Price
# Use Sheety to Access Google Sheets:

# Go to Sheety and create a new project.
# Connect your Google Sheet to Sheety and follow the instructions to get your API endpoint.
# Make a note of the Sheety API URL, which will look like this:
# arduino
# Copy code
# https://api.sheety.co/{YOUR_SHEETY_PROJECT_ID}/{YOUR_SHEET_NAME}
# Step 3: Set Up the Amadeus API
# Sign Up for Amadeus API:

# Go to the Amadeus Developer Portal and create an account.
# Once registered, create a new application to obtain your API key and secret.
# Familiarize Yourself with the API:

# Review the documentation for the Flight Offers API to understand how to make requests and interpret responses.
# Step 4: Set Up Twilio for SMS Notifications
# Sign Up for Twilio:

# Go to Twilio and create a free account.
# Follow the instructions to get a Twilio phone number that you can use to send SMS.
# Get Your Twilio Credentials:

# Make a note of your Twilio Account SID and Auth Token from the Twilio console.
# Step 5: Write the Python Script
# Create a New Python File:

# Open your favorite code editor (like VSCode, PyCharm, or even a simple text editor).
# Create a new Python file (e.g., flight_tracker.py).
# Import Required Libraries:

# At the top of your script, import the libraries you need:
# python
# Copy code
# import requests
# from twilio.rest import Client
# Set Up Configuration Constants:

# Define constants for your API keys and URLs:
# python
# Copy code
# SHEETY_API_URL = "https://api.sheety.co/YOUR_SHEETY_PROJECT_ID/YOUR_SHEET_NAME"
# AMADEUS_API_KEY = "YOUR_AMADEUS_API_KEY"
# AMADEUS_API_SECRET = "YOUR_AMADEUS_API_SECRET"
# TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
# TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
# TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
# USER_PHONE_NUMBER = "YOUR_PHONE_NUMBER"
# Function to Get Flight Data from Sheety:

# Write a function to fetch flight data from Sheety:
# python
# Copy code
# def get_flight_data():
#     response = requests.get(SHEETY_API_URL)
#     if response.status_code == 200:
#         return response.json()['YOUR_SHEET_NAME']  # Adjust this based on your sheet name
#     else:
#         print(f"Error fetching data from Sheety: {response.status_code}, {response.text}")
#         return []
# Function to Search for Flights Using Amadeus API:

# Write a function to search for flights:
# python
# Copy code
# def search_flights(iata_code):
#     amadeus_api_url = f"https://api.amadeus.com/v2/shopping/flight-offers"
    
#     # Obtain access token from Amadeus API
#     token_response = requests.post(
#         "https://test.api.amadeus.com/v1/security/oauth2/token",
#         data={"grant_type": "client_credentials"},
#         auth=(AMADEUS_API_KEY, AMADEUS_API_SECRET)
#     )

#     if token_response.status_code != 200:
#         print("Error obtaining access token")
#         return []
    
#     access_token = token_response.json()['access_token']
    
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
    
#     params = {
#         "originLocationCode": iata_code,
#         "destinationLocationCode": "YourDestinationIATA",  # Define or read from the sheet
#         "departureDate": "2024-08-25",  # Define the departure date
#         "adults": 1,
#         "maxPrice": 1000  # Optional: max price filter
#     }

#     response = requests.get(amadeus_api_url, headers=headers, params=params)

#     if response.status_code == 200:
#         flight_offers = response.json().get('data', [])
#         return flight_offers
#     else:
#         print(f"Error fetching flight data: {response.status_code}, {response.text}")
#         return []
# Function to Send SMS Using Twilio:

# Write a function to send SMS:
# python
# Copy code
# def send_sms(message):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
#     message = client.messages.create(
#         body=message,
#         from_=TWILIO_PHONE_NUMBER,
#         to=USER_PHONE_NUMBER
#     )
#     print(f"Message sent: {message.sid}")
# Main Execution Flow:

# Combine all functions in the main execution block:
# python
# Copy code
# if __name__ == "__main__":
#     flight_data = get_flight_data()

#     for entry in flight_data:
#         city = entry['City']
#         iata_code = entry['IATA Code']
#         predefined_price = entry['Price']

#         # Search for flights
#         flights = search_flights(iata_code)

#         for flight in flights:
#             flight_price = flight['price']['total']  # Adjust based on API response structure
#             if flight_price < predefined_price:
#                 # Send SMS notification
#                 sms_message = f"Cheaper flight found for {city}: ${flight_price}"
#                 send_sms(sms_message)
#                 break
# Step 6: Test Your Project
# Run the Script:

# In your terminal, navigate to the directory containing your script and run:
# bash
# Copy code
# python flight_tracker.py
# Check SMS Notifications:

# If a cheaper flight is found, you should receive an SMS notification.
# Step 7: Optional Enhancements
# Error Handling: Improve error handling to manage different types of errors (network issues, API limits, etc.).

# Scheduling: Use a task scheduler (like cron on Linux or Task Scheduler on Windows) to run your script at regular intervals.

# User Input: Modify the script to allow user input for parameters like destination and departure date.

# Deployment: Consider deploying your script on a cloud service (like Heroku or AWS) to run continuously.

# Hints and Tips
# Read API Documentation: Familiarize yourself with the Amadeus API documentation to understand the required parameters and response structures.
# Debugging: Use print statements to debug and check the flow of data through your script.
# Version Control: Consider using Git for version control to keep track of your changes.
# Code Organization: Keep your code organized by using functions for modularity.
# By following these steps, you should be able to successfully implement your project. Good luck, and feel free to reach out if you have any questions!

