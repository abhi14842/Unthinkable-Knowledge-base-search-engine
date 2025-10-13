import asyncio
import uuid
import json
import os
from pathlib import Path
from datetime import datetime

from pdf_processor import extract_pdf_text
from text_chunker import chunk_text
from embedding_service import EmbeddingService
from vector_store import VectorStore

class DocumentService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.metadata_file = "documents_metadata.json"
        self._load_metadata()

    def _load_metadata(self):
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, "r") as f:
                self.documents = json.load(f)
        else:
            self.documents = {}

    def _save_metadata(self):
        with open(self.metadata_file, "w") as f:
            json.dump(self.documents, f, indent=2, default=str)

    async def process_document(self, file_path: str, filename: str) -> str:
        print(f"📄 Processing document: {filename}")
        doc_id = str(uuid.uuid4())

        try:
            if filename.lower().endswith(".pdf"):
                text = await extract_pdf_text(file_path)
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

            if not text.strip():
                raise Exception("No text found in document")

            chunks = chunk_text(text)
            texts = [c["text"] for c in chunks]
            embeddings = await self.embedding_service.get_embeddings(texts)

            await self.vector_store.add_documents(doc_id, texts, embeddings, filename)

            self.documents[doc_id] = {
                "id": doc_id,
                "filename": filename,
                "upload_date": datetime.now().isoformat(),
                "chunk_count": len(chunks),
                "character_count": len(text),
                "status": "processed"
            }
            self._save_metadata()

            print(f"✅ Document processed successfully: {filename}")
            return doc_id

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            raise
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    async def get_documents(self):
        return list(self.documents.values())
