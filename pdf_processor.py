import asyncio
import PyPDF2

async def extract_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file"""
    print(f"📄 Extracting text from PDF: {file_path}")

    def extract():
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n\n"
                        print(f"📃 Extracted page {i+1}")
                except Exception as e:
                    print(f"⚠️ Error reading page {i+1}: {e}")
        return text

    loop = asyncio.get_event_loop()
    text = await loop.run_in_executor(None, extract)
    print(f"✅ Extracted {len(text)} characters from PDF")
    return text
