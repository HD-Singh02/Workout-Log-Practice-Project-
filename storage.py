import json
from pathlib import Path

FILE = Path(__file__).parent / "worouts.json"

def save_workouts(workouts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(workouts, f, indent=4)

save_workouts([{"exercise": "Bench", "Sets": 3}])
