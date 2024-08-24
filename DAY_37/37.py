# 🍵 , Hanji Kaise ho aap sabhi this is 37th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# -------------------- ADVANCE AUTHENTICATION  -------------------- #

# Use Pixela for api build habit taker

# HTTP Post Requests
# -- GET Ask external system
# -- POST give the data to external system
# -- PUT 
# -- DELETE

# Advance Authentication using http headers
# What is header -- header is part contains main thing

# put -- for update



name = "Alice"
college = "Harvard"

print(f"{name} is topper in {{college}}")


# ------------------- DELETE USER FROM PIXEL ------------------------------ #


import requests

# Define the user ID you want to delete
user_id = "hariom123"  # Replace with your actual user ID
pixela_endpoint = "https://pixe.la/v1/users"

# Define the endpoint for deleting the user account
pixel_deletion_endpoint = f"{pixela_endpoint}/{user_id}"  # This constructs the correct URL for deletion

# Define headers with the authorization token
headers = {
    "X-USER-TOKEN": "hariom5266",  # Use "X-USER-TOKEN" for Pixela's authorization
    "Content-Type": "application/json"
}

# Attempt to delete the user
try:
    response = requests.delete(pixel_deletion_endpoint, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    
    if response.status_code == 200:
        print("User deleted successfully.")
    else:
        print(f"Unexpected status code received: {response.status_code} - {response.text}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # For HTTP errors
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")  # For connection errors
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")  # For timeout errors
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")  # For all other requests-related errors

