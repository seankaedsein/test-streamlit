import streamlit as st
from PIL import Image

input_code = "A"

# Text input
prompt_text = st.text_area('Enter prompt', placeholder='Input prompt here...')

# Buttons
if st.button("Generate Image"):
    input_code = prompt_text

if st.button("Reset", type="primary"):
    input_code = "A"

st.divider()

# Placeholder for image display
if input_code == "B":
    image = Image.open('generic_CXR.jpg')
else:
    image = Image.open('placeholder_CXR.jpg')

image
st.caption('Output displayed above.')




