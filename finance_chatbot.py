import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from dotenv import load_dotenv
import os
import google.generativeai as genai



load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")

if not gemini_api_key:
    gemini_api_key = st.secrets["gemini_api_key"]  # Access the secret

if gemini_api_key is None:
    st.error("API key not found. Please set the secret MY_API_KEY in Streamlit Cloud.")
    st.stop()
# Set up the Streamlit app
st.title('AI Chat Assistant')
st.write('Hi, I\'m your AI assistant. How can I help you today?')

# Chat interface wrapped in a fixed footer div
st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
st.markdown("## Chat with AI Assistant")
genai.configure(api_key=gemini_api_key)
prompt = st.text_input("Enter a prompt: ")
if prompt:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)

# Custom CSS to fix the chat bar to the bottom and avoid content overlap
st.markdown(
    """
    <style>
    .chat-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f9f9f9;
        padding: 10px;
        border-top: 1px solid #ccc;
        z-index: 100;
    }
    .chat-footer input {
        width: 80%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    .chat-footer button {
        padding: 10px 20px;
        margin-left: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

