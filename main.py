from fastapi import FastAPI
import csv
import os

app = FastAPI()
CSV_FILE = "observations.csv"

@app.post("/observations")
def add_observation(obs: dict):
    date = obs.get("date")
    hb = obs.get("hb")

    # Create file if not exists, write header
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "hb"])
        writer.writerow([hb, date])

    return {"message": "Saved", "date": date, "hb": hb}
