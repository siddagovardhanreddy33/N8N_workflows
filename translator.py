import streamlit as st
import requests

st.title("AI Translator")

text = st.text_area("Enter Text")

if st.button("Telugu"):
    if text:
        response = requests.post(
            url="https://tobiuchiha77.app.n8n.cloud/webhook-test/e63b6168-2f2a-4ad0-ad35-83ff01643aba",
            json={"text": text}
        )
        if response.status_code == 200:
            st.write(response.json()["output"])

if st.button("Hindi"):
    if text:
        response = requests.post(
            url="https://tobiuchiha77.app.n8n.cloud/webhook-test/e63b6168-2f2a-4ad0-ad35-83ff01643aba",
            json={"text": text}
        )
        if response.status_code == 200:
            st.write(response.json()["output"])
