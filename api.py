from typing import Union

from fastapi import FastAPI
from RandomData import RandomData
app = FastAPI()

randData = RandomData()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user-data")
def read_item():
    return randData.profile_json()