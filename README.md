# Quantum-Assisted Mobility Optimization (Ruter-inspired)

This project explores a simplified mobility optimization problem inspired by public transportation systems such as Ruter.

Instead of solving a classical Traveling Salesman Problem, we model a **transport mobility routing problem** where:

- Nodes represent public transport stops in Oslo
- Edge weights represent travel time between stops
- Each stop has a demand weight representing passenger importance

---

##  Problem Definition

We aim to optimize a route that minimizes:

- Total travel time between stops
- Weighted passenger demand at each stop

This reflects a simplified version of real-world public transport routing challenges.

---

##  Methodology

We formulate the problem as a Quadratic Program (QP) and solve it using:

- Qiskit Optimization
- Quantum Approximate Optimization Algorithm (QAOA)
- Classical simulator backend

---

##  Mobility Interpretation

Unlike classical TSP formulations, this model includes:

- Travel time between real transport stops
- Passenger demand weighting per stop
- A mobility-focused objective function

---

##  Quantum Approach

We use QAOA to explore potential advantages of quantum-classical hybrid optimization for combinatorial mobility problems.

---

### Key Observations
- The model successfully finds valid permutations of stops.
- Demand weighting influences the structure of the optimized route.
- Solutions may vary between runs due to quantum-inspired sampling.
---
### Performance Notes
- Small-scale instances (3 stops) solve quickly using QAOA on classical simulators.
- No clear quantum advantage is expected at this scale.
- The primary value lies in modeling and hybrid optimization experimentation.


##  Future Work

- Integration with real-time mobility data APIs
- Dynamic routing under traffic conditions
- Scaling to Vehicle Routing Problems (VRP)
- Hybrid AI + quantum optimization models

---

##  Motivation

This project is motivated by research into how quantum computing may contribute to future mobility optimization systems in public transportation networks.
