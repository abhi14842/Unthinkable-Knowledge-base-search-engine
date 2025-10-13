import re
from typing import List, Dict

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[Dict]:
    """Split text into overlapping chunks"""
    print(f"✂️ Chunking text ({len(text)} chars)...")

    text = re.sub(r"\s+", " ", text).strip()
    chunks = []
    start = 0
    idx = 0

    while start < len(text):
        end = start + chunk_size
        if end < len(text):
            last_period = text.rfind('.', start, end)
            if last_period > start + chunk_size // 2:
                end = last_period + 1

        chunk = text[start:end].strip()
        if chunk:
            chunks.append({"text": chunk, "chunk_index": idx})
            idx += 1
        start = end - overlap
        if start <= 0:
            break

    print(f"✅ Created {len(chunks)} chunks")
    return chunks
