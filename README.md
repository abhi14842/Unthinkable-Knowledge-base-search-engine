# 🧠 Knowledge-base Search Engine

A simplified RAG (Retrieval-Augmented Generation) system using **100% FREE** APIs and models. Upload documents and ask questions to get AI-powered answers without any paid services!

## ✨ Features

- 📄 **Document Upload**: PDF and TXT file support
- 🤖 **Free AI Models**: Uses multiple free LLM APIs with automatic fallback
- 🔍 **Semantic Search**: ChromaDB vector database for document retrieval  
- 💬 **Smart Answers**: AI-powered responses with source citations
- 🎨 **Simple UI**: Clean, responsive web interface
- 🆓 **Completely Free**: No paid APIs required (but optional for better results)

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. (Optional) Set Free API Keys
Copy `.env.example` to `.env` and add your free API keys:

```bash
cp .env.example .env
# Edit .env with your free API keys
```

**Free API Options:**
- **Groq**: 14,400 free requests/day → [Get key](https://console.groq.com)
- **Hugging Face**: 300 free requests/hour → [Get key](https://huggingface.co/settings/tokens)  
- **GitHub Models**: Free with GitHub account → [Get token](https://github.com/settings/personal-access-tokens/new)

### 3. Run the Application
```bash
python main.py
```

### 4. Open Your Browser
Go to: http://localhost:8000

## 🔧 How It Works

1. **Upload Documents** - PDF or TXT files are processed and chunked
2. **Generate Embeddings** - Free sentence-transformers model creates vectors
3. **Store in Database** - ChromaDB saves embeddings for fast search
4. **Ask Questions** - Your query is matched against document chunks
5. **AI Answer** - Free LLM APIs generate responses with sources

## 🆓 Free Tier Limits

| API Provider | Free Limit | Best For |
|--------------|------------|----------|
| Groq | 14,400 requests/day | High volume, fast responses |
| Hugging Face | 300 requests/hour | Continuous usage |
| GitHub Models | Rate limited | Backup option |
| Local Fallback | Unlimited | Always works |

## 📁 Project Structure

```
├── main.py                 # FastAPI application
├── document_service.py     # Document processing
├── search_service.py       # Search and RAG logic
├── llm_service.py         # Multiple free LLM APIs
├── embedding_service.py   # Free sentence transformers
├── vector_store.py        # ChromaDB integration
├── pdf_processor.py       # PDF text extraction
├── text_chunker.py        # Text splitting
├── index.html            # Web interface
└── requirements.txt      # Dependencies
```

## 🎯 Usage Examples

1. **Upload a PDF** about machine learning
2. **Ask questions** like:
   - "What is machine learning?"
   - "How do neural networks work?"
   - "What are the main algorithms mentioned?"

The system will search your documents and provide answers with source citations!

## 🔄 API Fallback Strategy

The system tries APIs in this order:
1. **Groq** (fastest, 14.4k daily requests)
2. **GitHub Models** (reliable backup)
3. **Hugging Face** (good for research)
4. **Local Fallback** (rule-based, always works)

## 🚫 No Paid APIs Required

Unlike other RAG systems that require expensive OpenAI APIs, this version uses:
- ✅ Free embedding models (sentence-transformers)
- ✅ Free vector database (ChromaDB)
- ✅ Free LLM APIs (Groq, HuggingFace, GitHub)
- ✅ Local PDF processing (PyPDF2)

## 📊 Performance

- **Document Processing**: ~10 seconds for 10MB PDF
- **Query Response**: ~3-5 seconds with API keys
- **Fallback Response**: ~1 second without APIs
- **Storage**: Local ChromaDB database

## 🛠 Customization

- **Chunk Size**: Modify `chunk_size` in `text_chunker.py`
- **Embedding Model**: Change model in `embedding_service.py`
- **Response Length**: Adjust `max_tokens` in `llm_service.py`

## ⚠️ Limitations

- **File Types**: Only PDF and TXT (no DOCX in basic version)
- **Document Size**: Best with documents under 50MB
- **API Limits**: Dependent on free tier limits
- **Accuracy**: May be lower than paid models

## 🔍 Troubleshooting

**No API responses?**
- Check your API keys in `.env` file
- Verify internet connection
- System will fall back to rule-based answers

**PDF not processing?**
- Ensure PDF has extractable text (not scanned images)
- Try with TXT files first

**Slow responses?**
- Free APIs have rate limits
- Responses may be queued during high usage

## 🆙 Upgrading

To add paid APIs later, just update `llm_service.py` with:
- OpenAI API integration
- Anthropic Claude API
- Or any OpenAI-compatible API

## 📄 License

MIT License - Free to use, modify, and distribute!

---

**Built with ❤️ using 100% FREE and Open Source tools**

🔗 **No paid subscriptions required!** 🔗
```