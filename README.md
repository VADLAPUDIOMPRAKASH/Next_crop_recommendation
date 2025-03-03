# Next Crop Recommendation

## Overview
This is a Flask-based web application that predicts the best crop to grow based on soil nutrients (N, P, K), pH level, and weather conditions (temperature and humidity). The application fetches real-time weather data using the user's IP-based location and integrates it into the prediction model.

## Features
- Predicts the best crop based on given soil and weather parameters.
- Fetches real-time temperature and humidity using Open-Meteo API.
- Uses a pre-trained machine learning model for predictions.
- Provides a REST API for easy integration.

## Technologies Used
- Python
- Flask
- Scikit-Learn
- NumPy
- Requests
- Pickle (for model and scaler serialization)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VADLAPUDIOMPRAKASH/Next_crop_recommendation.git
   cd Next_crop_recommendation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the required files are available:
   - `model.pkl` (Trained machine learning model)
   - `minmaxscaler.pkl` (MinMaxScaler for feature transformation)

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Access the web interface at `http://localhost:10000/`.
3. Use the API to get predictions:
   ```bash
   curl -X POST "http://localhost:10000/predict" -H "Content-Type: application/json" -d '{"N": 50, "P": 30, "K": 20, "ph": 6.5}'
   ```
4. Response format:
   ```json
   {
     "crop": "Rice",
     "temperature": 28.5,
     "humidity": 65.0
   }
   ```

## API Endpoints
- `GET /` - Renders the homepage.
- `POST /predict` - Takes soil parameters as JSON input and returns the predicted crop along with temperature and humidity.

## Deployment
To deploy this application on a cloud platform (e.g., Render, Heroku):
1. Set the environment variable for the port (`PORT=10000`).
2. Use `gunicorn` as a production WSGI server:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:10000 app:app
   ```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## Author
Vadlapudi Om Prakash

