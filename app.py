import streamlit as st
import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    # getting invalid api key for now directly using it
    genai.configure(api_key="AIzaSyC1b24YZAIU9-XUVGNb4Up3F5QHik3bvKw")
else:
    print("API key not found. Please set GEMINI_API_KEY in the .env file.")

BASE_URL = "https://raw.githubusercontent.com/007aneesh/web-chatbot/main/"
DATASETS = {
    "Segment": "segment_data.txt",
    "mParticle": "mparticle_data.txt",
    "Lytics": "lytics_data.txt",
    "Zeotap": "zeotap_data.txt"
}

def load_data(file_name):
    url = BASE_URL + file_name
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            st.error(f"Failed to fetch data from {url}")
            return ""
    except Exception as e:
        st.error(f"Error: {e}")
        return ""

def ask_chatbot(question, documentation):
    prompt = f"""
    You are a support chatbot that strictly answers based on the provided documentation.
    If the question is unrelated or the answer is not in the data, respond with "I can only provide information from the selected documentation."

    Documentation:
    {documentation}

    Question: {question}
    """

    try:
        model = genai.GenerativeModel(model_name='gemini-2.0-flash')
        response = model.generate_content(prompt)
        return response.text if hasattr(response, 'text') else "Error: Invalid response format."
    except Exception as e:
        return f"An error occurred: {str(e)}"


st.title("Documentation Chatbot")

selected_dataset = st.selectbox("Choose the documentation source:", list(DATASETS.keys()))

if selected_dataset:
    data_file = DATASETS[selected_dataset]
    documentation = load_data(data_file)
    if documentation:
        st.success(f"Loaded documentation for {selected_dataset}")

        question = st.text_area("Ask your question:")

        if st.button("Ask Chatbot"):
            if question:
                with st.spinner("Getting response..."):
                    answer = ask_chatbot(question, documentation)
                    st.success("Chatbot Response:")
                    st.write(answer)
            else:
                st.warning("Please enter a question.")
    else:
        st.error("Failed to load documentation.")
