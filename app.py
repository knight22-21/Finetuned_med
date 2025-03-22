import streamlit as st
import requests
import json

# Retrieve API key from Streamlit secrets
try:
    HF_API_KEY = st.secrets["HUGGINGFACE_API_KEY"]  # Ensure this matches the name in Secrets
except KeyError:
    st.error("❌ Hugging Face API key is missing! Add it in 'Settings' → 'Secrets' as HUGGINGFACE_API_KEY.")
    st.stop()

MODEL_NAME = "knight2122/fine-tuned-llama3"

st.set_page_config(page_title="Medical Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 Medical AI Chatbot")
st.markdown("This chatbot is powered by a **fine-tuned Llama 3 model** trained on medical data.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything about medical topics...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        headers = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}
        data = {"inputs": f"### Instruction:\nAnswer the question truthfully, you are a medical professional.\n\n### Input:\n{user_input}\n\n### Response:\n", "parameters": {"max_new_tokens": 256}}

        response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL_NAME}", headers=headers, json=data)

        if response.status_code == 200:
            response_text = response.json()[0]["generated_text"]
        else:
            response_text = "❌ Error: Model is still loading or unavailable."

    with st.chat_message("assistant"):
        st.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
