
import requests  # type: ignore
import pymupdf as fitz  # type: ignore

url = "https://raw.githubusercontent.com/akashprabhu683/DOCS/main/CCS370_UI%20and%20UX%20Design%20Laboratory_250730_151513.pdf"

response = requests.get(url)
response.raise_for_status()

with open("lab_manual.pdf", "wb") as f:
    f.write(response.content)

doc = fitz.open("lab_manual.pdf")

with open("lab_manual_extracted.txt", "w", encoding="utf-8") as f:
    for page_num, page in enumerate(doc, start=1):
        f.write(f"\n\n========== PAGE {page_num} ==========\n\n")
        f.write(page.get_text())

print(f"Extracted {len(doc)} pages.")
print("Saved as lab_manual_extracted.txt")