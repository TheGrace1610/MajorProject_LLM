from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Initialize Streamlit app configuration - must be the first Streamlit command
st.set_page_config(page_title="Gemini Image Demo", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOGLE_API_KEY"))

# Function to load GeminiPro model and get a response
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_text, image):
    if input_text.strip():  # Check if input is not just empty spaces
        response = model.generate_content([input_text, image])
    else:  
        response = model.generate_content([input_text, image])
    return response.text 

# Initialize Streamlit app components
st.header("Gemini Application")
input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If submit is clicked
if submit:
    if image is not None:
        response = get_gemini_response(input_text, image)
        st.subheader("The response is")
        st.write(response)
    else:
        st.error("Please upload an image.")
