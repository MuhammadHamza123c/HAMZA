# AI PDF/Text Chatbot using LangChain, RAG, and Groq (LLaMA3)

This is a beginner-friendly project that builds a simple AI chatbot capable of answering questions from a text file using LangChain, sentence-transformer embeddings, Chroma vector store, and the Groq API (with LLaMA3-8B model).

## 📂 Project Structure

project/
│
├── hamza_port.txt # Your input text file (e.g., intro or resume)
├── main.py # Main chatbot code
├── requirements.txt # Python dependencies
└── README.md # This file

markdown
Copy
Edit

## 🚀 Features

- Loads your `.txt` file
- Splits the text into chunks
- Embeds chunks using HuggingFace sentence-transformers
- Stores vectors in Chroma vector store
- Retrieves similar content based on a user question
- Sends a context-aware prompt to Groq's LLaMA3 API
- Returns a clean answer from the AI

## 🛠️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/llm-pdf-chatbot.git
cd llm-pdf-chatbot
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add your text file
Make sure hamza_port.txt is present in the root folder.

4. Run the project
bash
Copy
Edit
python main.py
🔑 API Key
You need a Groq API key. Get it from https://console.groq.com/keys and replace it in main.py.

python
Copy
Edit
api_key = "your_groq_api_key"
📘 Example Use Case
Question: What is your interest?

AI Response (based on your intro):

"I am interested in artificial intelligence, machine learning, and LLM-based projects like chatbots and PDF question answering."

