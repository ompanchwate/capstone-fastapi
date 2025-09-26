from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

df = pd.read_csv("circuits.csv")
current_index = {"index": 0}

@app.get("/weather/next")
def get_next_weather():
    if current_index["index"] < len(df):
        row = df.iloc[current_index["index"]].to_dict()
        current_index["index"] += 1
        return JSONResponse(content=row)
    else:
        return JSONResponse(content={"message": "No more data available."})