import json
from pathlib import Path

FILE = Path(__file__).parent / "workouts.json"

def save_workouts(workouts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(workouts, f, indent=4)

def load_workouts():
    if not FILE.exists():
        return[]
    with open(FILE, "r", encoding="utf-8") as f:
        loaded = json.load(f)
        return loaded
