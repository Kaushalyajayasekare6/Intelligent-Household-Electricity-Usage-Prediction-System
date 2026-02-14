# Intelligent Household Electricity Usage Prediction System

This project predicts daily household electricity consumption using a supervised machine learning model.  
The system estimates electricity usage based on appliance categories and their usage hours.

## Project Overview
This intelligent system predicts daily electricity usage for a household using:
- Number of appliances
- Appliance power categories
- Usage duration

A Multiple Linear Regression model is used to estimate daily electricity consumption.

Since real Sri Lankan household electricity datasets were not publicly available, a synthetic dataset was generated using realistic appliance power ratings and usage patterns.

## Machine Learning Details
Type: Supervised Learning  
Problem: Regression  
Algorithm Used: Multiple Linear Regression  

### Input Features
- Low-power device usage
- Medium-power device usage
- High-power device usage

### Target
- Daily electricity consumption (kWh)

## Model Performance
- MAE: 0.39 kWh
- RMSE: 0.49 kWh
- R² Score: 0.986

The high R² score indicates strong predictive performance.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Streamlit

## System Features
- Machine learning regression model
- Synthetic dataset based on realistic appliance usage
- Data preprocessing and feature engineering
- Model evaluation using standard regression metrics
- Streamlit web interface for real-time predictions

## Project Structure
electricity-usage-prediction/
│
├── Electricity_Usage_Model.ipynb
├── daily_electricity_data.csv
├── daily_electricity_model.pkl
├── app.py
└── README.md

## How to Run the Project

### 1. Install dependencies
Run in the terminal:
pip install pandas numpy scikit-learn streamlit joblib

### 2. Run the Streamlit app
streamlit run app.py

Then open the browser link shown in the terminal.

## Example Prediction
Example input:
- Low-power devices: 6 for 5 hours
- Medium-power devices: 3 for 7 hours
- High-power devices: 1 for 10 hours

Predicted daily usage: approximately 5.02 kWh

## Limitations
- Uses a synthetic dataset
- Does not consider seasonal or weather effects
- Assumes constant appliance power ratings

## Future Improvements
- Use real household electricity datasets
- Include weather and seasonal factors
- Add electricity cost prediction
- Extend to monthly forecasting

## Author
Student Project — Intelligent Systems (Machine Learning)  
University of Vavuniya  
Department of Information and Communication Technology
