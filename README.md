# Project Overview
This project predicts whether a bank customer will stay or leave (churn) using Machine Learning.
A Random Forest Classifier is trained on customer data and deployed using a Streamlit web app for real-time predictions.

# Problem Statement
Banks lose revenue when customers leave (churn).
The goal is to build a model that can identify customers likely to churn so that retention strategies can be applied.

# Machine Learning Approach
Data preprocessing and cleaning
Encoding categorical variables
Feature selection
Model training using Random Forest Classifier
Model evaluation using accuracy, precision, recall, and F1-score

# Model Performance
Accuracy: ~86%
Precision: ~0.76
Recall: ~0.47
F1 Score: ~0.58

# Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
Joblib

# Project Structure
Customer-Churn-Prediction/
│
├── app.py              # Streamlit web app
├── model.pkl           # Trained ML model
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
