
import streamlit as st
import pandas as pd
import pickle

# --------------------------------------------------
# Load Model
# --------------------------------------------------

with open("fraud_detection_model.pkl", "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="FraudGuard AI",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #1f2937);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
    opacity: 0.8;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

.card {
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-bottom: 20px;
}

.result-fraud {
    padding: 30px;
    border-radius: 20px;
    border: 2px solid #ff4b4b;
    text-align: center;
    margin-top: 25px;
}

.result-safe {
    padding: 30px;
    border-radius: 20px;
    border: 2px solid #21c55d;
    text-align: center;
    margin-top: 25px;
}

.result-title {
    font-size: 32px;
    font-weight: 800;
}

.probability {
    font-size: 24px;
    font-weight: 700;
}

.footer {
    text-align: center;
    margin-top: 50px;
    opacity: 0.6;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Hero Section
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>💳 FraudGuard AI</h1>

<p>
AI-powered Credit Card Fraud Detection System
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Project Description
# --------------------------------------------------

st.markdown("""
<div class="card">

<b>🔐 Smart Transaction Security</b>

<p>
Enter transaction details below and let the machine learning
model determine whether the transaction is legitimate or potentially fraudulent.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Transaction Details
# --------------------------------------------------

st.markdown(
    '<div class="section-title">💰 Transaction Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    transaction_hour = st.slider(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=12
    )

    merchant_category = st.selectbox(
        "Merchant Category",
        [
            "Electronics",
            "Food",
            "Grocery",
            "Travel"
        ]
    )


with col2:

    foreign_transaction = st.selectbox(
        "🌍 Foreign Transaction?",
        ["No", "Yes"]
    )

    location_mismatch = st.selectbox(
        "📍 Location Mismatch?",
        ["No", "Yes"]
    )

    velocity_last_24h = st.number_input(
        "Transactions in Last 24 Hours",
        min_value=0,
        value=5
    )


# --------------------------------------------------
# Cardholder Information
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👤 Cardholder & Device Information</div>',
    unsafe_allow_html=True
)

col3, col4 = st.columns(2)

with col3:

    device_trust_score = st.slider(
        "🔐 Device Trust Score",
        min_value=0,
        max_value=100,
        value=50
    )

with col4:

    cardholder_age = st.number_input(
        "Cardholder Age",
        min_value=18,
        max_value=100,
        value=30
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

predict_button = st.button(
    "🔍  ANALYZE TRANSACTION",
    use_container_width=True
)


if predict_button:

    # Convert Yes/No to 1/0

    foreign_transaction_value = (
        1 if foreign_transaction == "Yes" else 0
    )

    location_mismatch_value = (
        1 if location_mismatch == "Yes" else 0
    )


    # Create input dataframe
    input_data = pd.DataFrame([{

        "amount": amount,

        "transaction_hour": transaction_hour,

        "foreign_transaction": foreign_transaction_value,

        "location_mismatch": location_mismatch_value,

        "device_trust_score": device_trust_score,

        "velocity_last_24h": velocity_last_24h,

        "cardholder_age": cardholder_age,

        "merchant_category_Electronics": 0,

        "merchant_category_Food": 0,

        "merchant_category_Grocery": 0,

        "merchant_category_Travel": 0

    }])


    # Set selected merchant category
    merchant_column = "merchant_category_" + merchant_category

    input_data[merchant_column] = 1


    # Prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    # --------------------------------------------------
    # Result
    # --------------------------------------------------

    if prediction == 1:

        st.markdown(
            f"""
            <div class="result-fraud">

            <div class="result-title">
            🚨 FRAUDULENT TRANSACTION
            </div>

            <p>
            The model detected suspicious characteristics
            in this transaction.
            </p>

            <div class="probability">
            Fraud Probability: {probability * 100:.2f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-safe">

            <div class="result-title">
            ✅ LEGITIMATE TRANSACTION
            </div>

            <p>
            The transaction appears to be legitimate
            according to the machine learning model.
            </p>

            <div class="probability">
            Fraud Probability: {probability * 100:.2f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("""
<div class="footer">

🤖 Powered by Machine Learning &nbsp; | &nbsp;
Credit Card Fraud Detection Project

</div>
""", unsafe_allow_html=True)
