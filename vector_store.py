import chromadb
from typing import List, Dict

class VectorStore:
    def __init__(self):
        print("🔄 Initializing ChromaDB vector store...")
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="documents")
        print("✅ Vector store ready")

    async def add_documents(self, doc_id: str, texts: List[str], embeddings: List[List[float]], filename: str):
        print(f"💾 Adding {len(texts)} chunks for {filename}...")
        ids = [f"{doc_id}_{i}" for i in range(len(texts))]
        metadatas = [{"filename": filename, "chunk_index": i} for i in range(len(texts))]

        self.collection.add(ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas)
        print("✅ Chunks added successfully")

    async def search_similar(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )

        formatted = []
        for i, doc in enumerate(results["documents"][0]):
            distance = results["distances"][0][i]
            similarity = 1 / (1 + distance)
            formatted.append({
                "text": doc,
                "filename": results["metadatas"][0][i]["filename"],
                "score": similarity
            })

        print(f"📋 Found {len(formatted)} relevant chunks")
        return formatted
