import numpy as np
from src.origami_solver import origami_fold_projection

nodes = np.array([
    [1.0, 1.0],
    [2.0, -1.0],
    [0.5, 3.0]
])

folded_nodes = origami_fold_projection(nodes)
print("Original 2D coordinates:\n", nodes)
print("Folded projection coordinates:\n", folded_nodes)
