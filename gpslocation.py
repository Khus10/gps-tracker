from opencage.geocoder import OpenCageGeocode
import requests

def get_location():
    try:
        # Fetch public IP address
        ip_response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip_response.raise_for_status()  # Raise an error for bad status codes
        ip_address = ip_response.json()['ip']

        # Use OpenCage to get location
        geocoder = OpenCageGeocode("782a0fd548ca4d1e8f5bf6b53a636931")  # Replace with your OpenCage API key
        results = geocoder.geocode(ip_address)
        if results:
            return (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
        else:
            print("Error: Unable to fetch location data.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None

# Example usage
location = get_location()
if location:
    latitude, longitude = location
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Failed to fetch location.")

import firebase_admin
from firebase_admin import credentials, db
import time

# Initialize Firebase
cred = credentials.Certificate("C:/Users/Dell/OneDrive/Desktop/gps-tracker-83b05-firebase-adminsdk-fbsvc-176208bf0a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gps-tracker-83b05-default-rtdb.firebaseio.com/'
})

def send_to_firebase(latitude, longitude):
    ref = db.reference('gps_data')
    ref.set({
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': time.time()
    })
from geopy.distance import geodesic

def check_distance(initial_location, current_location):
    distance = geodesic(initial_location, current_location).meters
    if distance > 500:
        print(f"Alert! You have moved {distance:.2f} meters from your starting point.")
    else:
        print(f"You are within {distance:.2f} meters of your starting point.")
def main():
    # Store initial location
    initial_location = get_location()
    if not initial_location:
        print("Failed to fetch initial location. Exiting.")
        return

    while True:
        # Fetch current location
        current_location = get_location()
        if current_location:
            # Send to Firebase
            send_to_firebase(current_location[0], current_location[1])

            # Check distance and trigger alert
            check_distance(initial_location, current_location)

        # Wait for 1 minute before updating again
        time.sleep(60)

if __name__ == '__main__':
    main()