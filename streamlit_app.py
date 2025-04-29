import streamlit as st
import streamlit.components.v1 as components

# Load the HTML file
with open("static/index.html", "r", encoding='utf-8') as f:
    html_content = f.read()

# Render the HTML inside the app
components.html(html_content, height=600, scrolling=True)

