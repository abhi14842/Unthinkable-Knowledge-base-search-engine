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

### 1️⃣ Clone the repository
   ```bash
   git clone https://github.com/your-username/knowledge-base-search.git
   cd knowledge-base-search
   
### 2️⃣ Create a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate   

### 3️⃣ Install dependencies
   ```bash
   pip install -r requirements.txt

### 4️⃣ Add your Groq API key

Create a .env file in the root folder and add:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here


### ▶️ Run the Application
Start the server:
   ```bash
   python main.py

Then open the browser and go to:
   ```bash
   http://127.0.0.1:8000/static/index.html


##💡 How It Works

Upload your document (PDF or TXT).
The backend extracts text and stores it in ChromaDB.
Ask a question related to the uploaded document.
The system retrieves relevant chunks and generates an answer using the Groq LLM.

## 📂 Project Structure
knowledge-base-search/
│
├── main.py
├── llm_service.py
├── search_service.py
├── document_service.py
├── vector_store_service.py
├── embedding_service.py
├── static/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## 🧠 Example

User Query:
What is reinforcement learning?

AI Answer:
Reinforcement learning is a machine learning approach where agents learn by interacting with their environment and receiving feedback in the form of rewards.


## 🏁 Future Improvements

Support multiple file uploads
Add chat-style interface
Deploy on cloud (Render / Vercel / AWS)