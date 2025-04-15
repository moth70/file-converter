from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
import shutil
import magic
import os
from markitdown import MarkItDown

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def read_root():
    return (
        "Instrukcja użycia:\n\n"
        "GET / - pokazuje tę instrukcję\n"
        "POST /upload - przyjmij dowolny plik jako multipart/form-data i zapisz do /tmp\n"
        "Rozpoznawany jest również typ przesłanego pliku.\n"
    )

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    mime = magic.Magic(mime=True)
    detected_type = mime.from_file(file_location)

    md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
    result = md.convert(file_location)

    try:
        os.remove(file_location)
        print(f"Plik {file_location} został usunięty.")
    except FileNotFoundError:
        print(f"Plik {file_location} nie istnieje.")
    except PermissionError:
        print(f"Brak uprawnień do usunięcia pliku {file_location}.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    return {
        "status": "success",
        "filename": file.filename,
        "saved_to": file_location,
        "detected_mime_type": detected_type,
        "md_outcome": result.text_content
    }

