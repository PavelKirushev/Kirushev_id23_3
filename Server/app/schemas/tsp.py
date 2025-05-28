from typing import List
from pydantic import BaseModel

class Graph(BaseModel):
    nodes: List[int]
    edges: List[List[int]]

class PathResult(BaseModel):
    path: List[int]
    total_distance: float