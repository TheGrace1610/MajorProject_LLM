from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Streamlit app configuration
st.set_page_config(page_title="Q&A Demo")

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOGLE_API_KEY"))

# Initialize the model for text-based interactions
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text 

# Streamlit app components
st.header("Gemini LLM Application")
input_text = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input_text)
    st.subheader("The response is")
    st.write(response)





