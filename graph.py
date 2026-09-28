import time
import numpy as np
from scipy.optimize import linprog
import pathlib as pth

class Graph:
    def __init__(self, graph_edges: set[tuple[int,int]], graph_nodes: set[int]):
        self.solution = None
        self.duration = None

        self.edges: list[tuple[int,int]] = list(graph_edges)
        self.nodes: set[int] = graph_nodes

    """
        min c^T x
        s.t.
            A_{ub} x <= b_{ub}          --- (i)
            A_{eq} x = b_{eq}           --- (ii)
            lb <= x <= ub               --- (iii)
    """
    def _solve_lpp(self) -> np.ndarray:
        n = len(self.nodes)
        m = len(self.edges)

        c = np.ones((n,))

        a_ub = np.zeros((m,n))
        b_ub = np.ones((m,))

        for i in range(m):
            edge : tuple[int,int] = self.edges[i]
            u,v = edge
            a_ub[i,u] = 1
            a_ub[i,v] = 1

        """
            a_ub x >= b_ub
            -a_ub x <= -b_ub
        """
        lpp_sol = linprog(c = c, A_ub=-a_ub, b_ub=-b_ub, bounds=(0,1), method="highs")

        sol: np.ndarray = np.array(lpp_sol.x)

        return sol

    def calculate_approximate(self, ) -> None:
        start_time = time.perf_counter_ns()

        solution = self._solve_lpp()

        solution = (solution >= 0.5).tolist()

        self.solution = set()

        for i in range(len(solution)):
            if solution[i]:
                self.solution.add(i)

        end_time = time.perf_counter_ns()

        # duration in micro seconds
        self.duration = (end_time - start_time) * 1e-3

    def store(self, save_file: pth.Path) -> None:
        with open(save_file, 'w') as file:
            file.write(f"{self.duration}\n")
            file.write(" ".join(str(x) for x in self.solution))
