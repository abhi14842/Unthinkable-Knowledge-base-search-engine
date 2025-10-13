import asyncio
from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        print("🔄 Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("✅ Embedding model loaded")

    async def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []

        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(None, self._encode_texts, texts)
        return embeddings.tolist()

    def _encode_texts(self, texts: List[str]) -> np.ndarray:
        limited = [t[:1000] for t in texts]
        return self.model.encode(limited, normalize_embeddings=True)
