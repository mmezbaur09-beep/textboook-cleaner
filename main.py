from fastapi import FastAPI, UploadFile, File
from pathlib import Path

app = FastAPI()


UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Textbook Cleaner API Running"
    }


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Image uploaded successfully",
        "file": file.filename
    }

    