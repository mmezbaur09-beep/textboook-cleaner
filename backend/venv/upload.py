from fastapi import UploadFile, File
from pathlib import Path

UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


async def save_image(file: UploadFile):

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "location": str(file_path)
    }