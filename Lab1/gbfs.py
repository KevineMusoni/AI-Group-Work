from greedy_bfs import GBFS
def bfs(
    G: nx.Graph, destination: str, start: str = "SportsComplex"
) -> (List[adj_list], Set[str]):
    """
    Searches for a path from *destination* from *start* in the
    graph *G*. A path is a list of nodes from start you need to
    pass to reach destination. Returns the path and a set of
    nodes visited during the search
    """
    if start == destination:
        return []
    frontier = deque([start])
    explored = set()
    solution = []
    visited = set()
    while True:
        if not frontier:
            return []
        node = frontier.popleft()
        explored.add(node)
        solution.append(node)
        for adj in G.neighbors(node):
            visited.add(adj)
            if adj not in explored and adj not in frontier:
                if adj == destination:
                    return solution, visited
                frontier.appendleft(adj)
