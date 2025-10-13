import time
from typing import Dict
from embedding_service import EmbeddingService
from vector_store import VectorStore
from llm_service import LLMService

class SearchService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.llm_service = LLMService()

    async def search_and_answer(self, query: str, top_k: int = 5) -> Dict:
        """Search documents and generate AI-based answer"""
        print(f"🔍 Searching for: {query}")
        start_time = time.time()

        try:
            query_embedding = await self.embedding_service.get_embeddings([query])
            query_emb = query_embedding[0]

            results = await self.vector_store.search_similar(query_emb, top_k)
            if not results:
                return {
                    "query": query,
                    "answer": "No relevant information found in your uploaded documents.",
                    "sources": [],
                    "confidence": 0.0,
                    "processing_time": time.time() - start_time
                }

            contexts = [r["text"] for r in results[:3]]
            answer = await self.llm_service.generate_answer(query, contexts)

            avg_score = sum(r["score"] for r in results) / len(results)
            confidence = min(avg_score * 100, 95.0)

            sources = [
                {
                    "filename": r["filename"],
                    "text": (r["text"][:200] + "...") if len(r["text"]) > 200 else r["text"],
                    "score": round(r["score"], 3)
                } for r in results
            ]

            return {
                "query": query,
                "answer": answer,
                "sources": sources,
                "confidence": round(confidence, 1),
                "processing_time": round(time.time() - start_time, 2)
            }

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {
                "query": query,
                "answer": "An error occurred while processing your request.",
                "sources": [],
                "confidence": 0.0,
                "processing_time": time.time() - start_time
            }
