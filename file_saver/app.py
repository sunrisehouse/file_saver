import os

from fastapi import FastAPI, File, Form, UploadFile

class FileSaver:
    def __init__(self, upload_directory):
        app = FastAPI()

        @app.get("/")
        def get_root():
            return {"Hello": "World"}

        @app.post("/files")
        async def submit_file(file: UploadFile, key: str = Form()):
            contents = await file.read()
            with open(os.path.join(upload_directory + key, file.filename), "wb") as fp:
                fp.write(contents)
            return { "filename": file.filename }
