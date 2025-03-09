# gps-tracker
This project is an IoT system that retrieves real-time GPS coordinates from a user's laptop, processes them, and transmits them to a cloud database (Firebase Realtime Database). The data is then visualized on a web dashboard with a live map. The system also triggers an alert if the user moves more than 500 meters from their starting point.

Prerequisites
Before running the project, ensure you have the following installed:

1.Python : Download and install Python from python.org.

2.Firebase Account: Create a Firebase project at Firebase Console.

3.Create an account on opencagedata.com 

Set Up Firebase

1.Go to your Firebase project in the Firebase Console.

2.Navigate to Project Settings > Service Accounts.

3.Click Generate New Private Key and download the JSON file.

4.Place the JSON file in the project folder and rename it to firebase-key.json.

5.Update the Firebase database URL:

6.Open the firebase_send.py file.

7.Replace 'https://your-database-name.firebaseio.com/' with your Firebase Realtime Database URL.

INSTALL DEPENDENCIES 

pip install opencage firebase-admin flask folium

RUN THE PROJECT 

  gpslocation.py- It retrieves real-time GPS coordinates from a user's laptop, processes them, and transmits them to Firebase Realtime Database. The system also triggers an alert if the user moves more than 500 meters from their starting point.

  dashboard.py- It helps in visualisation of data on a web dashboard with a live map.
