import numpy as np
from ortools.linear_solver import pywraplp
import re

arr = [re.findall(r"\d+", _) for _ in open("input.txt").read().strip().split("\n\n")]
arr = np.array(arr, dtype=np.int64).reshape(len(arr), 3, 2)


def solveMachineMIP(clawMachine, error=10000000000000):
    solver = pywraplp.Solver.CreateSolver("SCIP")
    A = solver.IntVar(0, solver.infinity(), "A")
    B = solver.IntVar(0, solver.infinity(), "B")

    solver.Minimize(3 * A + B)
    solver.Add(clawMachine[0][0] * A + clawMachine[1][0] * B == clawMachine[2][0]+error)
    solver.Add(clawMachine[0][1] * A + clawMachine[1][1] * B == clawMachine[2][1]+error)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return int(solver.Objective().Value())
    else:
        return 0


totalCostP1, totalCostP2 = 0, 0
for idz in range(arr.shape[0]):
    totalCostP1 += solveMachineMIP(arr[idz], 0)
    totalCostP2 += solveMachineMIP(arr[idz])
print("AoC_2024_13.1:", totalCostP1)
print("AoC_2024_13.2:", totalCostP2)
