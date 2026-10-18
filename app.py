import streamlit as st
import urllib.parse
st.set_page_config(page_title="EximSaif AI", page_icon="🌾")
st.title("🌾 EximSaif AI")
st.markdown("**Chhapra Se Dubai Tak - 1 Click Export**")
st.success("Verified: +91 7492013591 | Chhapra, Bihar")
st.divider()
buyer = st.text_input("Buyer Name", "Lulu Hypermarket Dubai")
if st.button("Find Buyer Email"):
    email="headoffice@ae.lulumea.com"
    subject="Basmati Export - EximSaif AI - Chhapra"
    body="Hello, I am Saif from Chhapra Bihar. +91 7492013591. Please share supplier process."
    link=f"https://mail.google.com/mail/?view=cm&to={email}&su={subject}&body={body}"
    st.link_button("Open Gmail", link)
