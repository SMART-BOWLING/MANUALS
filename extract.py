import os
from PyPDF2 import PdfReader

PDF_FOLDER = "manuals"   # папка где лежат PDF
TEXT_FOLDER = "texts"    # папка для сохранённых TXT

def extract_pdfs(pdf_folder=PDF_FOLDER, text_folder=TEXT_FOLDER):
    os.makedirs(text_folder, exist_ok=True)

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            txt_path = os.path.join(text_folder, filename.replace(".pdf", ".txt"))

            try:
                reader = PdfReader(pdf_path)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"✅ {filename} → {txt_path}")
            except Exception as e:
                print(f"❌ Ошибка при обработке {filename}: {e}")

if __name__ == "__main__":
    extract_pdfs()
