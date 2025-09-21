from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os


FILE_PATH = os.path.join(os.path.dirname(__file__), 'index.html')

app = FastAPI()


@app.get('/')
async def print_hello():
    if os.path.exists(FILE_PATH):

        return FileResponse(FILE_PATH, media_type='text/html')
    else:

        raise HTTPException(status_code=404, detail='Not Found')
