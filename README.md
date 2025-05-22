# 🤖 Gen-AI LangChain Chatbot (Week 1 – Gen AI Architect Project)

This is a document-aware chatbot built using [LangChain](https://www.langchain.com/), [OpenAI GPT](https://platform.openai.com/), and a [FAISS](https://github.com/facebookresearch/faiss) vector store. It lets you ask natural language questions about a company policy document.

---

## 📌 Project Overview

This chatbot demonstrates how to:

- Load and process local documents (TXT format)
- Chunk documents into manageable pieces
- Embed them using OpenAI embeddings
- Store and retrieve them via a vector database (FAISS)
- Use `RetrievalQA` to answer user queries with context
- Run everything in a simple command-line interface

---

## 📁 Project Structure

```
Gen-AI-LangChain-Chatbot/
├── app.py                 # Main LangChain chatbot script
├── .env                  # Contains OpenAI API key (excluded from repo)
├── requirements.txt       # Required packages
├── data/
│   └── policy.txt         # Sample company policy document
```

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/kumaravela/Gen-AI-LangChain-Chatbot.git
cd Gen-AI-LangChain-Chatbot
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your .env file
Create a `.env` file in the root and add your OpenAI key:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the chatbot
```bash
python app.py
```

---

## 💬 Example Questions

Try asking things like:

- "What is the company's leave policy?"
- "What are the working hours?"
- "Does the company allow remote work?"
- "Summarize the code of conduct."

---

## 🛠️ Built With

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🧠 What's Next (Week 2 Goals)

- ✅ Week 1: CLI chatbot using LangChain + FAISS ✅
- 🔜 Week 2: Integrate PDF loading, RAG pipeline, Qdrant/Chroma support
- 🔜 Add Streamlit or Gradio UI

---

## 📸 Demo Screenshot

_A screenshot can be added here after testing the bot UI_  
Place it under `/screenshots/demo.png` and uncomment the line below:

<!-- ![LangChain Chatbot](screenshots/demo.png) -->

---

## 🙌 Author

[Kumar Avela](https://github.com/kumaravela) — learning to become a Gen AI Architect 🚀

---

## 📜 License

MIT License – feel free to fork, use, and contribute!
