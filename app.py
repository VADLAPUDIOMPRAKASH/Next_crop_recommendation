from flask import Flask, request, jsonify, render_template
import pickle
import requests
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("minmaxscaler.pkl", "rb"))

def get_weather_data():
    """Fetch user location & weather data using IP-based services."""
    try:
        # Get public IP-based location
        location_response = requests.get("https://ipinfo.io/json")
        location_data = location_response.json()
        lat, lon = map(float, location_data["loc"].split(","))

        # Fetch weather data from Open-Meteo
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=relative_humidity_2m,temperature_2m"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # Get the latest available temperature and humidity
        temperature = weather_data["hourly"]["temperature_2m"][0]
        humidity = weather_data["hourly"]["relative_humidity_2m"][0]

        return temperature, humidity
    except Exception as e:
        print("Error fetching weather data:", e)
        return None, None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        N = float(data["N"])
        P = float(data["P"])
        K = float(data["K"])
        ph = float(data["ph"])

        # Get weather data automatically
        temperature, humidity = get_weather_data()
        if temperature is None or humidity is None:
            return jsonify({"error": "Could not fetch weather data"}), 500

        # Prepare input features
        features = np.array([[N, P, K, temperature, humidity, ph]])
        transformed_features = scaler.transform(features)

        # Predict crop
        prediction = model.predict(transformed_features)[0]

        # Crop dictionary
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop_name = crop_dict.get(prediction, "Unknown Crop")
        return jsonify({"crop": crop_name, "temperature": temperature, "humidity": humidity})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses 10000 by default
    app.run(host="0.0.0.0", port=port)
