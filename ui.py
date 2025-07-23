import streamlit as st
import requests

st.title("🏡 Smart Property Advisor – Hessen 🇩🇪")
query = st.text_area("🔍 Enter your query")

if st.button("Ask AI"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        response = requests.post("http://localhost:8000/ask", json={"prompt": query})
        st.success(response.json()["answer"])