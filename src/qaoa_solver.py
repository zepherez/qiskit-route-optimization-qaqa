from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit_algorithms.optimizers import COBYLA


def solve_qaoa(qp):

    sampler = Sampler()
    optimizer = COBYLA()

    qaoa = QAOA(
        sampler=sampler,
        optimizer=optimizer,
        reps=1
    )

    solver = MinimumEigenOptimizer(qaoa)

    return solver.solve(qp)
