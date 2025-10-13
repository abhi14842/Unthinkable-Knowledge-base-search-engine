from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

# Import our services
from document_service import DocumentService
from search_service import SearchService

app = FastAPI(title="Knowledge Base Search Engine", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
doc_service = DocumentService()
search_service = SearchService()

# Create required directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)

# Mount static files (if you add a /static folder for CSS or JS)
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the frontend (index.html)
@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    """Serve the main HTML UI."""
    html_path = Path("index.html")
    if not html_path.exists():
        return HTMLResponse(content="<h1>⚠️ index.html not found</h1>", status_code=404)
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"), status_code=200)


# Health check (optional)
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "🚀 Knowledge Base Search API is running with Groq!"}

# Upload endpoint
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.pdf', '.txt')):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files supported")

    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        doc_id = await doc_service.process_document(file_path, file.filename)
        return {"message": f"Document '{file.filename}' processed successfully!", "document_id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Search endpoint
@app.post("/search")
async def search_documents(query_data: dict):
    query = query_data.get("query", "").strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        result = await search_service.search_and_answer(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# List documents
@app.get("/documents")
async def list_documents():
    return await doc_service.get_documents()

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Knowledge Base Search Engine...")
    print("📖 Frontend: http://localhost:8000")
    print("📊 API Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
