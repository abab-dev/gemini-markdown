from google import genai
from google.genai import types
import httpx
import os
from io import BytesIO
from dotenv import load_dotenv
import pathlib

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Function to download file from URL
def download_file(url):
    response = httpx.get(url, timeout=30)
    response.raise_for_status()  # Raise an error for bad responses
    return BytesIO(response.content)  # Store in memory buffer

# URL of the PDF file
pdf_url = "https://nguyenduyliemgis.wordpress.com/wp-content/uploads/2014/09/understanding-gps-principles-and-applications-2006.pdf"
file_path = pathlib.Path(pdf_url)
# print(file_path.read_bytes())
# sys.exit()


# Download the PDF
pdf_buffer = download_file(pdf_url)
# print(buffer.getvalue())
# # Upload the PDF
sample_doc = client.files.upload(
    file=pdf_buffer,
    config={"mime_type": "application/pdf"}
)


# # Markdown conversion prompt
prompt = """
        Convert this document into Markdown, processing each page separately.
        Follow these guidelines for accurate representation:

        1. **Page Separation:**
        - Each page should be a distinct Markdown section.
        - Insert a delimiter in the format: `<!----Page-{n}---->` to
            indicate page breaks.

        2. **Text Extraction:**
        - Retain all text content with minimal modifications.
        - Preserve headings, paragraphs, and lists as they appear in the
            document.
        - Maintain **bold, italic, and other text formatting** from the
            original document.
        - Keep bullet points, numbered lists, and indentation where
            applicable.

        3. **Images and Figures:**
        - Replace images and figures with **detailed textual descriptions**
            that capture their essential content.
        - If a caption is present, include it in the description.

        4. **Tables:**
        - Convert tables into **proper Markdown tables** with correct
            formatting.
        - Maintain the structure, headers, and data integrity.

        5. **Mathematical Content:**
        - Perform OCR on mathematical symbols and equations.
        - Represent them using **LaTeX-compatible Markdown syntax**
            (`$...$` for inline math, `$$...$$` for block math).
        - Maintain correct mathematical formatting and structure.
        - Make sure no whitespaces around the `$...$` and `$$...$$` blocks

        6. **Code Blocks:**
        - If any code snippets exist, wrap them in appropriate Markdown
            fenced code blocks:
            ```md
            ```language
            code snippet
            ```
            ```
        - Detect and retain the programming language if specified.

        7. **No System Messages:**
        - Do not include system messages, metadata, or parsing-related
            information.
        - Output must be **clean and directly usable** for downstream
            processing.
"""

# Line below outputs total_tokens=699216 cached_content_token_count=None
print(client.models.count_tokens(model="gemini-2.0-flash",contents=[prompt,sample_doc]))


fpath = pathlib.Path("output_from_url.md")
output = client.files.upload(
    file=fpath,
)

# Line below outputs total_tokens=8107 cached_content_token_count=None
print(client.models.count_tokens(model="gemini-2.0-flash",contents=[output]))


# # Generate Markdown from the uploaded file
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=[sample_doc, prompt]
# )

# # Save output to a file
# output_path = "output_from_url.md"
# with open(output_path, "w", encoding="utf-8") as f:
#     f.write(response.text)

# print(f"Markdown file saved as {}")
