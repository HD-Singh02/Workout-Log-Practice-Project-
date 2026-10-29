from storage import load_workouts, save_workouts
from logic import add_workout

add_workout("Bench", 3, 8, 60.0)
add_workout("Squat", 4, 5, 80.0)
#save_workouts([{"exercise": "Bench", "sets": 3}])
print(load_workouts())
