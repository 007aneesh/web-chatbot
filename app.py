import streamlit as st
import requests
from google import genai 
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
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

# Function to ask Gemini with strict limitations
def ask_chatbot(question, documentation):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    You are a support chatbot that strictly answers based on the provided documentation.
    If the question is unrelated or the answer is not in the data, respond with "I can only provide information from the selected documentation."

    Documentation:
    {documentation}

    Question: {question}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit App
st.title("Documentation Chatbot")

# Dropdown to select the dataset
selected_dataset = st.selectbox("Choose the documentation source:", list(DATASETS.keys()))

if selected_dataset:
    # Load the corresponding data
    data_file = DATASETS[selected_dataset]
    documentation = load_data(data_file)
    if documentation:
        st.success(f"Loaded documentation for {selected_dataset}")

        # Display a text area for user query
        question = st.text_area("Ask your question:")

        # Button to ask the chatbot
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
