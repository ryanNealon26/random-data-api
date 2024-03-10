from typing import Union

from fastapi import FastAPI
from RandomData import RandomData
app = FastAPI()

random_api = RandomData()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user-data")
def read_item():
    return random_api.profile_json()

@app.get("/user-data/{total}")
def read_item(total: int):
    total_profiles = []
    for profile in range(total):
        data = random_api.profile_json() 
        total_profiles.append(data)
    json = {
        "data": total_profiles
    }
    return json

@app.get("/random-date")
def read_item():
    return random_api.generate_rand_date()

@app.get("/random-date/{total}")
def read_item(total: int):
    total_dates = []
    for date in range(total):
        data = random_api.generate_rand_date()
        total_dates.append(data)
    json = {
        "data": total_dates
    }
    return json

@app.get("/random-text/{wordCount}")
def read_item(wordCount: int):
    return random_api.generate_random_text(wordCount)
@app.get("/random-time/")
def read_item():
    return random_api.generate_time_of_day()