# import requests
# import json

# def get_location(phone_number):
#     # Enter your OpenCelliD API key here
#     api_key = "pk.8139a87ea371ae3e12f7688e9ecbec3f"
    
#     # Format the phone number in the required format (remove leading '+')
#     formatted_number = phone_number.lstrip('+')
    
#     # Make a request to OpenCelliD API
#     url = f"https://ap1.unwiredlabs.com/v2/process.php?token={api_key}&radio=umts&mcc=123&mnc=456&cells=12345,23456&format=json"
#     response = requests.get(url)
    
#     # Parse the JSON response
#     data = json.loads(response.text)
    
#     # Extract the location details
#     lat = data['lat']
#     lon = data['lon']
#     address = data['address']
    
#     # Return the location information
#     return lat, lon, address

# # Example usage
# phone_number = "+255684548258"  # Replace with the desired phone number
# location = get_location(phone_number)
# print(location)






import requests
import json

def get_location(phone_number):
    api_key = "8139a87ea371ae3e12f7688e9ecbec3f"
    formatted_number = phone_number.lstrip('+')
    
    url = f"https://ap1.unwiredlabs.com/v2/process.php?token={api_key}&radio=umts&mcc=123&mnc=456&cells=12345,23456&format=json"
    response = requests.get(url)
    
    data = json.loads(response.text)
    
    try:
        lat = data['lat']
        lon = data['lon']
        address = data['address']
        return lat, lon, address
    except KeyError:
        print("Error: Failed to extract location information from API response")
        print("API Response:", response.text)
        return None

phone_number = "+1234567890"  # Replace with the desired phone number
location = get_location(phone_number)
if location:
    print(location)

