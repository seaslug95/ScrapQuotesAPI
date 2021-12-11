from fastapi import FastAPI
from myscraper import myscrap

app = FastAPI()

@app.get('/{tag}')
async def read_item(tag: str):
    return myscrap(tag)
