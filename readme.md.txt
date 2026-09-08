# 💳 Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to detect whether a credit card transaction is legitimate or fraudulent.

The project focuses on binary classification and handles the class imbalance present in fraud detection data.

## 🎯 Objective

The main objective is to build a machine learning model that can identify fraudulent transactions based on transaction and cardholder-related features.

## 📊 Features Used

- Transaction Amount
- Transaction Hour
- Merchant Category
- Foreign Transaction
- Location Mismatch
- Device Trust Score
- Transaction Velocity in Last 24 Hours
- Cardholder Age

## 🤖 Machine Learning Models

The following models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

Hyperparameter tuning was also performed for the Decision Tree model.

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

## 🏆 Final Model

The tuned Decision Tree classifier was selected as the final model based on its performance on the evaluation data.
 
##💻 Deployment

A Streamlit web application was created where users can enter transaction details and receive a fraud prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Pickle

## 🚀 How to Run

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

Run the application:

```bash
streamlit run app.py
```

## ⚠️ Note

This project is intended for educational and portfolio purposes. Model performance depends on the dataset used for training and evaluation.