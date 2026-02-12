import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "https://expense-tracker-and-budgeting-system.onrender.com/" 

st.set_page_config(
    page_title="Smart Finance AI",
    layout="wide"
)



st.sidebar.title("Expense Tracker")
page = st.sidebar.radio("Option:", ["Dashboard", "Add Expense"])



if page == "Add Expense":

    st.title("➕ Add New Expense")

    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Submit Expense"):
        try:
            response = requests.post(
                f"{API_URL}/add-expense",
                json={"description": description, "amount": amount}
            )
            st.write("Status Code:", response.status_code)
            st.write("Response:", response.text)
        except Exception as e:
            st.error(str(e))




if page == "Dashboard":

    st.title("📊 Financial Dashboard")

    response = requests.get(f"{API_URL}/summary")

    if response.status_code == 200:
        data = response.json()

        if data:
            df = pd.DataFrame(list(data.items()), columns=["Category", "Total"])

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Category Breakdown")
                fig = px.pie(df, names="Category", values="Total")
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.subheader("Spending Bar Chart")
                fig2 = px.bar(df, x="Category", y="Total")
                st.plotly_chart(fig2, use_container_width=True)

        else:
            st.info("No expenses yet.")

    else:
        st.error("Could not fetch data from backend.")

