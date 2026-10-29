from storage import load_workouts, save_workouts
from datetime import date

def add_workout(exercise, sets, reps, weight):
    entry = {"date": date.today().isoformat(), 
            "exercise": exercise, 
            "sets": sets, 
            "reps": reps, 
            "weight": weight}
    workouts = load_workouts()
    workouts.append(entry)
    save_workouts(workouts)
    return entry

# returs oldest first, same order as the file
def get_history():
    history = load_workouts()
    return history
