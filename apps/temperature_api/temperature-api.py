from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the order service"}

@app.get("/temperature")
def read_temperature(location: str=Query(..., desctiption="Sensor location")):
    tmin, tmax = 0.0, 42.0
    return {
        "temperature": "{:.1f}".format(tmin + (tmax-tmin)*random.random()),
        "location": location}
