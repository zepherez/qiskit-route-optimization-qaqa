import numpy as np

# Simulated Oslo mobility network (not geographic distance)
stops = [
    "Majorstuen",
    "Nationaltheatret",
    "Jernbanetorget"
]

# Travel time matrix (minutes). could be replaced with real API data later
travel_time = np.array([
    [0, 6, 12],
    [6, 0, 5],
    [12, 5, 0]
])

# Passenger demand per stop (importance weighting)
demand = np.array([120, 300, 200])
