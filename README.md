# 🌾 Crop Recommendation System

## 🚀 Overview
The **Crop Recommendation System** is a Flask-based web application that predicts the most suitable crop to grow based on soil and weather conditions. It leverages a **machine learning model** to analyze soil nutrients and real-time weather data fetched from the user's location.

🔗 **Live Demo:** [Next Crop Recommendation](https://next-crop-recommendation.onrender.com)

## 🛠️ Features
✅ Predicts the best crop based on soil nutrients and weather conditions.
✅ Fetches real-time **temperature and humidity** based on the user's IP location.
✅ Utilizes a **pre-trained ML model** for accurate predictions.
✅ Provides a **REST API** for easy integration into other applications.
✅ Simple, user-friendly web interface.

## 🏗️ Technologies Used
- **Python** 🐍
- **Flask** 🌐
- **Scikit-Learn** 🤖
- **NumPy & Pandas** 📊
- **Requests (for API calls)** 🔗
- **Pickle (for model serialization)** 📦

## 📥 Installation
Follow these steps to set up the project locally:

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/VADLAPUDIOMPRAKASH/Next_crop_recommendation.git
cd Next_crop_recommendation
```

2️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

3️⃣ **Ensure the required model files are available:**
- `model.pkl` (Pre-trained ML model)
- `minmaxscaler.pkl` (Scaler for feature normalization)

4️⃣ **Run the application:**
```bash
python app.py
```

5️⃣ **Access the web interface:** Open `http://localhost:10000/` in your browser.

## 🔥 API Usage
### **Endpoint: `/predict` (POST Request)**
Send a JSON payload with soil parameters:
```json
{
  "N": 50,
  "P": 30,
  "K": 20,
  "ph": 6.5
}
```
### **Response Format:**
```json
{
  "crop": "Rice",
  "temperature": 28.5,
  "humidity": 65.0
}
```

## 🌍 Deployment
The project is hosted on **Render**. To deploy on your own cloud platform:
1️⃣ Set the environment variable `PORT=10000`.
2️⃣ Run the app using `gunicorn`:
```bash
gunicorn -w 4 -b 0.0.0.0:10000 app:app
```

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
We welcome contributions! Feel free to **fork the repository**, submit **pull requests**, or suggest **feature enhancements**.


💡 _Let's make agriculture smarter with technology!_ 🌱

