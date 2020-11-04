from typing import Optional

from fastapi import FastAPI

app = FastAPI()

#afficher hello word
@app.get("/")
def read_root():
    return {"Hello": "World"}

##afficher hello bengamin
@app.get("/benjamin")
def read_root():
    return {"Hello" : "Benjamin"}
