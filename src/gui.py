# gui.py
import streamlit as st
from receipt import generate_receipt 

st.title("Payment Receipt Generator")

# Input fields
name = st.text_input("Customer Name")
product = st.text_input("Product")
quantity = st.number_input("Quantity", min_value=1, step=1)
price = st.number_input("Price (Rs)", min_value=0.0, step=0.01)
payment_method = st.text_input("Payment Method")

if st.button("Generate Receipt"):
    if not (name and product and payment_method):
        st.error("Please fill all fields!")
    else:
        file_path = generate_receipt(name, product, quantity, price, payment_method)
        st.success("✅ Receipt Generated!")
        with open(file_path, "rb") as f:
            st.download_button("Download Receipt", f, file_name=file_path.split("/")[-1], mime="application/pdf")