import numpy as np

def origami_fold_projection(points: np.ndarray, fold_angle=np.pi/4) -> np.ndarray:
    # Huzita-Hatori Axiom-inspired folding projection matrix
    fold_matrix = np.array([
        [np.cos(fold_angle), -np.sin(fold_angle)],
        [np.sin(fold_angle), np.cos(fold_angle)]
    ])
    return np.dot(points, fold_matrix)
