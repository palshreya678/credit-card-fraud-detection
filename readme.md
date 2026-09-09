## 🚀 Live Demo
👉 [Try FraudGuard AI](https://credit-card-fraud-detection-27vu756uc5tuygmbxkvraf.streamlit.app)

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

 ## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|------------|--------|----------|---------|
| Logistic Regression | 95.85% | 26.55% | 100% | 41.96% | 99.33% |
| Decision Tree | 99.95% | 96.77% | 100% | 98.36% | 99.97% |
| Random Forest | 99.25% | 100% | 50% | 66.67% | 100% |
| KNN | 98.70% | 75% | 20% | 31.58% | 84.14% |

The tuned Decision Tree classifier achieved the strongest overall performance on the evaluation data and was selected as the final model.

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
