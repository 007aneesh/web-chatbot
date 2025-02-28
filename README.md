# Documentation Chatbot

This is a **Documentation Chatbot** built with **Streamlit** and **Google Generative AI**. It helps users query specific documentation datasets and provides responses strictly based on the selected documentation source.

## Features
- Select from multiple documentation sources (Segment, mParticle, Lytics, Zeotap)
- Asks questions and receives context-specific answers based on the chosen dataset
- Uses Google Generative AI (`gemini-2.0-flash`) for generating chatbot responses
- Clean and interactive UI built with Streamlit

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Google Generative AI (gemini-2.0-flash)
- **APIs:** Requests for fetching raw data from GitHub
- **Environment Management:** Python's `dotenv`

## Prerequisites
- Python 3.x installed
- A Google Generative AI API Key (GEMINI_API_KEY)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/007aneesh/web-chatbot.git
   cd web-chatbot
2.
 ```bash
  python -m venv venv
  source venv/bin/activate   # On MacOS/Linux
  venv\Scripts\activate      # On Windows
  ```
3.
 ```bash 
    pip install -r requirements.txt
   ```
4. 
```bash
      GEMINI_API_KEY=your_google_genai_api_key
   ```

## Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run main.py
Open the app in your browser:
After running the command, the app should automatically open in your default browser. If not, go to:

arduino
Copy
Edit
http://localhost:8501
Choose a Documentation Source:

Use the dropdown to select from the available datasets:
Segment
mParticle
Lytics
Zeotap
Ask Questions:

Enter your question in the text area.
Click on the "Ask Chatbot" button.
The chatbot will respond based on the selected documentation source.
Troubleshooting:

If the documentation fails to load, ensure the files are accessible on GitHub and the URLs are correct.
If you encounter issues with the chatbot responses, verify your API key in the .env file.
