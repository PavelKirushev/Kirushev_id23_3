from fastapi import APIRouter
from app.schemas.tsp import Graph, PathResult
from app.services.solver import solve_tsp

router = APIRouter()

@router.post("/shortest-path/", response_model=PathResult)
def shortest_path(graph: Graph):
    result = solve_tsp(graph.dict())
    return result