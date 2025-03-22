# Medical AI Chatbot

This repository contains a **fine-tuned LLaMA 3** model for medical queries. The chatbot is trained on medical datasets and provides responses to health-related questions.

## 🚀 Features
- **Fine-tuned LLaMA 3 Model**: Trained for medical-related conversations.
- **Streamlit Web Interface**: A user-friendly chatbot UI.
- **Hugging Face API Integration**: Uses HF for model inference.
- **Secure API Handling**: API keys stored in Streamlit secrets.

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/medical-ai-chatbot.git
cd medical-ai-chatbot
```

### 2️⃣ Install Dependencies
Create a virtual environment and install required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Hugging Face API Key
Store your **Hugging Face API key** in Streamlit secrets:
1. Open `secrets.toml` or add via Streamlit settings.
2. Add:
   ```toml
   [secrets]
   api_key = "your_huggingface_api_key"
   ```

### 4️⃣ Run the Chatbot
Start the Streamlit app:
```bash
streamlit run app.py
```

## 🏗️ Model Training & Deployment

### Fine-tuning LLaMA 3
The model was fine-tuned using **Unsloth & PEFT** with a medical dataset.
```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    "knight2122/fine-tuned-llama3",
    max_seq_length=2048,
    load_in_4bit=True
)
```

### Deploying the Model
To push the fine-tuned model to Hugging Face:
```python
model.push_to_hub("knight2122/fine-tuned-llama3", token="your_hf_token")
tokenizer.push_to_hub("knight2122/fine-tuned-llama3", token="your_hf_token")
```

## 🔍 Troubleshooting
If you see **"Model is still loading or unavailable"**, try:
- Checking the model status on Hugging Face.
- Restarting the Hugging Face Space.
- Ensuring correct API key setup in secrets.

## 📌 Future Improvements
- Add multi-turn conversations.
- Improve response accuracy with more datasets.
- Deploy as an API service.
