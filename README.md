# Bank Customer Churn Prediction System

## Project Overview

This project predicts whether a bank customer is likely to leave the bank (churn) using Machine Learning techniques. The solution includes data analysis, model training, a Power BI dashboard, and an interactive Streamlit web application.

## Objective

The objective of this project is to identify customers who are at risk of leaving the bank so that proactive retention strategies can be implemented.

## Live Demo

**Streamlit App:**
https://bank-customer-churn-prediction-s.streamlit.app

**GitHub Repository:**
https://github.com/shrutithapa244-prog/bank-customer-churn-prediction


## Dataset

The project uses the Bank Customer Churn dataset containing customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Status
* Active Member Status
* Estimated Salary

Target Variable:

* Exited (1 = Customer Churned, 0 = Customer Retained)

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Power BI
* Jupyter Notebook
* VS Code

## Machine Learning Workflow

1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Data Cleaning and Preprocessing
4. Feature Engineering
5. Train-Test Split
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Feature Importance Analysis
10. Web Application Development

## Model Performance

* Model: Random Forest Classifier
* Accuracy: 87.05%

## Features

* Predict customer churn
* Display churn probability
* Risk classification (Low / Medium / High)
* Interactive Streamlit interface
* Power BI dashboard for business insights

## Project Structure

Bank Churn Project/

├── App/
    -> app.py

├── Data/
    -> Churn_Modelling.csv

├── Model/
    -> churn_model.pkl
    -> scaler.pkl

├── Notebooks/
    -> churn_analysis.ipynb

├── Screenshots/
    -> PowerBI_Overview.png
    -> PowerBI_Insights.png
    -> Streamlit_App.png

└── README.md

## How to Run

1. Open terminal.
2. Navigate to the project folder.
3. Go to the App folder:

       cd App

4. Run the Streamlit application:

       python -m streamlit run app.py

5. Open the local Streamlit URL in your browser.

## Future Improvements

* Hyperparameter tuning
* Compare additional machine learning models
* Improve the Streamlit user interface
* Real-time database integration

## Author

Shruti Thapa
