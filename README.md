# 🏡 EstateAI – House Price Prediction System

**An interactive Machine Learning web application that predicts house prices based on property features.**

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)

## 📌 Project Overview

EstateAI is a BCA academic Machine Learning project developed to estimate house prices using property-related information. It uses a **Linear Regression** model trained on housing data and provides an interactive interface where users can enter property details and view an estimated price.

## ✨ Features

- House price prediction using Machine Learning
- Interactive property input form
- Property details such as area, bedrooms, bathrooms and parking
- Furnishing status selection
- Prediction history
- Dashboard with prediction statistics
- Property image gallery
- Model performance information

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data handling and preprocessing
- **Scikit-learn** – Machine Learning model
- **Streamlit** – Interactive web interface
- **Pickle** – Saving and loading trained model files

## 🤖 Machine Learning Model

- **Algorithm:** Linear Regression
- **Dataset:** Housing.csv
- **R² Score:** 65.3%
- **Mean Absolute Error (MAE):** Approximately 979,043 dataset price units

*These are the model performance values recorded for this project.*

## 📂 Project Structure

```text
EstateAI-House-Price-Prediction/
│
├── dataset/
│   └── Housing.csv
│
├── app.py
├── train_model.py
├── model.pkl
├── feature_columns.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/gungungoyal16/EstateAI-House-Price-Prediction.git
```

### 2. Open the project folder

```bash
cd EstateAI-House-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Project Objective

The main objective of EstateAI is to apply Machine Learning concepts to a real-world problem and develop an interactive application that demonstrates how property features can be used to estimate house prices.

## 👩‍💻 Developer

**Gungun Goyal**  
BCA – 3rd Year

GitHub: [@gungungoyal16](https://github.com/gungungoyal16)

---

⭐ If you find this project interesting, feel free to explore the repository!
