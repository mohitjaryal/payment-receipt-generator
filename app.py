import streamlit as st
from generate_receipt import generate_pdf  # your existing function

st.title("Payment Receipt Generator")

# Input fields
name = st.text_input("Enter Name")
amount = st.number_input("Enter Amount", min_value=0.0)
date = st.date_input("Select Date")

if st.button("Generate Receipt"):
    data = {
        "name": name,
        "amount": amount,
        "date": str(date)
    }
    filename = generate_pdf(data)  # your existing PDF function
    st.success("Receipt Generated!")
    st.download_button(
        label="Download Receipt",
        data=open(filename, "rb"),
        file_name=filename,
        mime="application/pdf"
    )