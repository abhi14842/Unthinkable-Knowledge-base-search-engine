# 📚 Knowledge Base Search Engine

A simple **AI-powered search engine** that lets you upload PDF or text documents, ask questions, and get summarized answers using **Groq LLM** and **ChromaDB**.

---

## 🚀 Features

- Upload PDF or TXT documents  
- Store document embeddings in a local database  
- Ask natural language questions  
- Get concise AI-generated answers  
- Simple and clean web interface  

---

## 🧰 Tech Stack

- **Backend:** FastAPI  
- **LLM:** Groq API  
- **Vector Store:** ChromaDB  
- **Frontend:** HTML + TailwindCSS + JavaScript  
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)

---

## ⚙️ Setup Instructions

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/knowledge-base-search.git
   cd knowledge-base-search

2. Create a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Add your Groq API key
   Create a .env file in the root folder and add:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here

5. Run the Application
   Start the server:
   ```bash
   python main.py
   
6. Then open the browser and go to:
   ```bash
   http://127.0.0.1:8000



##💡 How It Works

Upload your document (PDF or TXT).
The backend extracts text and stores it in ChromaDB.
Ask a question related to the uploaded document.
The system retrieves relevant chunks and generates an answer using the Groq LLM.


## 🧠 Example

User Query:
What is reinforcement learning?

AI Answer:
Reinforcement learning is a machine learning approach where agents learn by interacting with their environment and receiving feedback in the form of rewards.


## 🏁 Future Improvements

Support multiple file uploads
Add chat-style interface
Deploy on cloud (Render / Vercel / AWS)
