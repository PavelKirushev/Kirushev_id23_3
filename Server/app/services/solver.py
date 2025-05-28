def solve_tsp(graph: dict) -> dict:
    nodes = graph["nodes"]
    edges = {tuple(edge[:2]): 1.0 for edge in graph["edges"]}  # Преобразуем рёбра в словарь

    if not nodes:
        return {"path": [], "total_distance": 0.0}

    # Базовый случай: 1 или 2 узла
    if len(nodes) == 1:
        return {"path": nodes, "total_distance": 0.0}
    if len(nodes) == 2:
        edge = tuple(sorted((nodes[0], nodes[1])))
        dist = edges.get(edge, float('inf'))
        return {"path": nodes + [nodes[0]], "total_distance": dist}

    # Жадный алгоритм для поиска приближённого решения
    path = [nodes[0]]
    unvisited = set(nodes[1:])
    total_distance = 0.0

    while unvisited:
        last = path[-1]
        # Находим ближайшего соседа
        nearest = None
        min_dist = float('inf')

        for node in unvisited:
            edge = tuple(sorted((last, node)))
            dist = edges.get(edge, float('inf'))
            if dist < min_dist:
                min_dist = dist
                nearest = node

        if nearest is None:  # Нет пути
            return {"path": [], "total_distance": float('inf')}

        path.append(nearest)
        unvisited.remove(nearest)
        total_distance += min_dist

    # Возвращаемся в начальную точку
    edge = tuple(sorted((path[-1], path[0])))
    total_distance += edges.get(edge, float('inf'))
    path.append(path[0])

    return {"path": path, "total_distance": total_distance}