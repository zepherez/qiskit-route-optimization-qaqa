import numpy as np
from qiskit_optimization import QuadraticProgram


def build_mobility_qp(travel_time: np.ndarray, demand: np.ndarray):

    n = len(travel_time)
    qp = QuadraticProgram()

    # x[i,t] = stop i is visited at position t
    for i in range(n):
        for t in range(n):
            qp.binary_var(name=f"x_{i}_{t}")

    # Each stop visited exactly once
    for i in range(n):
        qp.linear_constraint(
            linear={f"x_{i}_{t}": 1 for t in range(n)},
            sense="==",
            rhs=1,
            name=f"visit_{i}"
        )

    # Each position filled exactly once
    for t in range(n):
        qp.linear_constraint(
            linear={f"x_{i}_{t}": 1 for i in range(n)},
            sense="==",
            rhs=1,
            name=f"position_{t}"
        )

    # Objective: travel time weighted by demand (Ruter interpretation)
    objective = {}

    for i in range(n):
        for j in range(n):
            for t in range(n - 1):

                weight = demand[j]  # importance of destination stop

                objective[(f"x_{i}_{t}", f"x_{j}_{t+1}")] = travel_time[i][j] * weight

    qp.minimize(quadratic=objective)

    return qp