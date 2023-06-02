import os

from fastapi import FastAPI, Form, UploadFile
import uvicorn

class FileSaver:
    def __init__(self, host, port, upload_directory):
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
        
        uvicorn.run(app, host=host, port=port)
