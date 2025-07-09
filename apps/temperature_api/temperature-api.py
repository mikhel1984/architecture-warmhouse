from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the order service"}

@app.get("/temperature")
def read_temperature(location: str=Query(..., desctiption="Sensor location")):
    tmin, tmax = 0.0, 42.0
    return {"value": "{:.2f}".format(tmin + (tmax-tmin)*random.random())}

@app.get("/temperature/{id}")
def read_id_temperature(id: int):
    tmin, tmax = 0.0, 42.0
    return {"value": tmin + (tmax-tmin)*random.random()}
