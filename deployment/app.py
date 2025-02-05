import streamlit as st

import prediction
import eda

page = st.sidebar.selectbox("Select Page : ", ["EDA", "Prediction"])

if page == "EDA":
    eda.run()
else:
    prediction.run()