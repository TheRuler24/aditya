from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)

weather_descriptions = [
    "clear sky", "few clouds", "scattered clouds",
    "light rain", "heavy rain", "thunderstorm",
    "snow", "mist", "haze"
]

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    weather_info = {
        "city": city.title(),
        "temperature": round(random.uniform(10.0, 35.0), 2),
        "description": random.choice(weather_descriptions),
        "humidity": random.randint(40, 90),
        "wind_speed": round(random.uniform(1.0, 10.0), 2),
        "timestamp": datetime.datetime.now().isoformat()
    }

    return jsonify(weather_info)

if __name__ == "__main__":
    app.run(debug=True)