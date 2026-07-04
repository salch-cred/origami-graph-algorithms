from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.origami_solver import origami_fold_projection

app = FastAPI(title="Origami Graph Algorithms API")

class FoldRequest(BaseModel):
    nodes: List[List[float]]
    fold_angle: float = 0.785 # pi/4

@app.post("/fold")
def fold(req: FoldRequest):
    import numpy as np
    nodes_arr = np.array(req.nodes)
    folded = origami_fold_projection(nodes_arr, req.fold_angle)
    return {"folded_nodes": folded.tolist()}
