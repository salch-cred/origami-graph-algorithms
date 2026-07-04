# Origami Graph Algorithms

An architectural approach to graph optimization and dimensionality reduction using the Huzita-Hatori axioms of origami mathematics.

By treating the vector space of the graph as a flat sheet of paper, connections are mapped onto fold lines. Multidimensional graphs can be projected into lower dimensions by executing folding rules that guarantee structural integrity.

## Usage
```bash
python examples/fold_graph.py
```


## FastAPI API Service
The project includes a FastAPI server wrapper. 

### Running the API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
- **Interactive docs**: Navigate to `/docs` for swagger documentation.
- **POST `/fold`**: Projects layout spaces using paper folding geometries.
