# Creating a GEMINI based AI in webpage using streamLit.

import google.generativeai as ai
import streamlit as sl

ai.configure(api_key="AIzaSyCHC8x_nJxGjKyCfxouRgT2KcvyTBxkvfM")

sl.title("Welcome to Vansh's personal AI. Ask me anything.....")
model = ai.GenerativeModel("gemini-2.0-flash")
prompt = sl.text_input("Enter your prompt: ")
if sl.button("Generate"):
    with sl.spinner("wait karo process thay che...."):
        response = model.generate_content(prompt,stream=True)
        for chunk in response:
            sl.markdown(chunk.text)