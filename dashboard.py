from flask import Flask, render_template_string
import folium
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("gps-tracker-83b05-firebase-adminsdk-fbsvc-176208bf0a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gps-tracker-83b05-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch latest GPS data from Firebase
    ref = db.reference('gps_data')
    data = ref.get()
    latitude = data['latitude']
    longitude = data['longitude']

    # Create a map
    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], tooltip="Current Location").add_to(m)

    # Render the map in the browser
    return render_template_string(m._repr_html_())

if __name__ == '__main__':
    app.run(debug=True)