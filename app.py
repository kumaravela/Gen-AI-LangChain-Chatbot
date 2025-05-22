from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not set in .env file")

# Load document
try:
    loader = TextLoader("data/policy.txt")
    documents = loader.load()
except Exception as e:
    raise RuntimeError(f"Error loading document: {e}")

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create vectorstore
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# Create retriever and QA chain
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=retriever,
    return_source_documents=True
)

# CLI loop for Q&A
print("✅ LangChain chatbot is ready. Ask questions or type 'exit' to quit.\n")

while True:
    query = input("🔍 Ask: ")
    if query.lower() in ("exit", "quit"):
        print("👋 Exiting chatbot. Bye!")
        break
    try:
        result = qa_chain({"query": query})
        print("💬 Answer:", result["result"])
    except Exception as e:
        print("⚠️ Error:", e)
