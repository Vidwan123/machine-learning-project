#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import joblib

st.title("Cyber Attack Detection — CSV Upload")

# Load trained model
model = joblib.load("model.pkl")

st.write("Upload a CSV file to predict cyber attack types.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.write(data)

    try:
        # Make predictions
        predictions = model.predict(data)

        # Add predictions to dataframe
        data["Predicted Attack Type"] = predictions

        st.subheader("Predictions")
        st.write(data)

        # Download button
        csv = data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Results",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error("Error during prediction. Check column names and preprocessing.")
        st.exception(e)

