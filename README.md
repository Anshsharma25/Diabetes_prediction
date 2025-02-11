# AI Diabetes Prediction

This project is a **web-based AI Diabetes Prediction system** that allows users to enter their health details and receive an AI-powered prediction of whether they have diabetes. The model is built using **Flask (Backend), TailwindCSS (Frontend), and Machine Learning (Decision Tree Algorithm trained with the Pima Indians Diabetes Dataset).**

## 🚀 Features
- **User-friendly UI** with a modern design
- **AI-powered prediction** using a trained machine learning model
- **Flask API backend** for model inference
- **Live prediction display** with color-coded alerts

---

## 📂 Project Structure
```
/diabetes-prediction
│── /static              # (Optional) Static assets (CSS, JS, Images)
│── /templates           # HTML frontend files
│── app.py               # Flask API backend
│── diabetes_model.pkl   # Trained ML model (saved using Joblib)
│── scaler.pkl           # Scaler for input features
│── README.md            # Documentation
│── requirements.txt     # Python dependencies
│── diabetes_ui.html     # Main HTML UI file
```

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Flask API
```sh
python app.py
```

### 4️⃣ Open the UI
- Open `diabetes_ui.html` in your browser.
- Enter the required details.
- Click **"Predict Now"** to get the AI prediction.

---

## 🔬 API Endpoint
The backend API runs on **http://127.0.0.1:5000/**.

**POST /predict**  
📌 **Request:**
```json
{
  "features": [3, 78, 50, 32, 88, 33.1, 0.45, 29]
}
```
📌 **Response:**
```json
{
  "prediction": 1
}
```
(`1` = Diabetic, `0` = Not Diabetic)

---

## 🤖 Machine Learning Model
### 🔹 Algorithm Used
The model is trained using the **Decision Tree Algorithm** from `scikit-learn` to classify whether a person has diabetes or not.

### 🔹 Feature Engineering
- **BMI_Age**: A new feature created by multiplying BMI and Age.
- **Feature Scaling**: Standardization using `StandardScaler` to normalize input values.

### 🔹 Training Dataset
- **Pima Indians Diabetes Dataset** from the UCI Machine Learning Repository.
- Contains **768 samples** with **8 input features**.

---

## 🏗️ Technologies Used
- **Frontend:** HTML, TailwindCSS, JavaScript
- **Backend:** Flask (Python)
- **Machine Learning:** Decision Tree (`sklearn`)
- **Deployment:** AWS EC2 (optional)

---

## 📜 License
This project is **open-source** and free to use under the MIT License.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a PR. 🚀

For any issues, contact **anshsharma8nbi@gmail.com**.

---

### 🎯 Future Enhancements
- ✅ Deploy the Flask API to AWS
- ✅ Store user predictions in a database
- ✅ Improve accuracy with deep learning

---
![Screenshot 2025-02-11 131137](https://github.com/user-attachments/assets/086cd4e9-07f7-49c7-8b3e-9adc5c0c0c29)

⭐ **If you found this useful, give it a star on GitHub!** ⭐

