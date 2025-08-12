# 🏠 Real Estate Price Prediction – India Housing Dataset

## 📌 Project Overview
This project is about predicting **house prices** in various Indian cities using **Machine Learning**.  
The model takes property details like size, location, furnishing status, and accessibility to amenities, and returns the estimated price in lakhs.  

The goal is to **make property valuation faster, more accurate, and transparent** for buyers, sellers, and real estate companies.

---

## 📂 Features
- Data preprocessing: handling missing values, encoding categorical variables, and removing outliers.
- Exploratory Data Analysis (EDA) to identify trends and correlations.
- Feature engineering: creating derived features like property age and log-transformed price.
- Multiple regression models: Linear Regression, Lasso, Ridge, LightGBM, and XGBoost.
- Model evaluation using RMSE, MSE, and R² metrics.
- Deployment-ready model via **Flask REST API**.

---

## 🛠️ Tech Stack
**Programming Language:** Python 3.8+  
**Libraries:**  
- Data Processing: `pandas`, `numpy`
- Visualization: `matplotlib`, `seaborn`
- Machine Learning: `scikit-learn`, `xgboost`, `lightgbm`
- Deployment: `Flask`, `joblib`

---

## 📊 Dataset
- **Source:** https://www.kaggle.com/datasets/mohamedafsal007/house-price-dataset-of-india
- **Rows:** 200,000  
- **Columns:** 24  
- **Target Variable:** `Price_in_Lakhs`

### Example Features:
- `State` – Property location state  
- `City` – Property location city  
- `Size_in_SqFt` – Size of property  
- `BHK` – Number of bedrooms  
- `Furnishing` – Furnished/Semi-furnished/Unfurnished  
- `Public_Transport_Accessibility` – Low/Medium/High  

---

## 🚀 Project Workflow
1. **Data Collection** – Load CSV from Kaggle.
2. **Data Preprocessing** – Remove irrelevant columns, handle missing values, encode categories.
3. **EDA** – Visualize trends, correlations, and outliers.
4. **Feature Engineering** – Add new features like property age and log price.
5. **Model Training** – Train multiple regression models.
6. **Model Evaluation** – Compare models and select the best one.
7. **Deployment** – Save model and serve predictions using Flask API.

---

## 📈 Model Performance
- **Best Model:** XGBoost Regressor  
- **Why XGBoost?**  
  - Handles non-linear relationships well.  
  - High accuracy and low error metrics.  
  - Robust with missing values and categorical data.

---

## 🖥️ Deployment
The trained model is deployed as a **Flask REST API**.  
You can send a POST request with property details and get an estimated price.

Example API call:
```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"State": "Maharashtra", "City": "Pune", "Size_in_SqFt": 1200, "BHK": 2, "Furnishing": "Furnished", "Public_Transport_Accessibility": "High"}'
