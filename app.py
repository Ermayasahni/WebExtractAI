import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/extract-price"

st.set_page_config(page_title="Amazon Price Extractor", page_icon="💰")

st.title("🛍️ Product Price Extractor")
st.write("Enter an Amazon product URL to extract its price.")

# Input field
url = st.text_input("Product URL")

if st.button("Extract Price"):
    if url:
            try:
                response = requests.post(API_URL, json={"url": url})
                data = response.json()
                st.success(f"💰 Price: {data['price']}")
                
            except Exception as e:
                st.error(f"Failed to connect to API: {e}")
    else:
        st.warning("Please enter a URL.")