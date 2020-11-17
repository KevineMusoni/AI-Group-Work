from collections import defaultdict
import heapq


class UCS:

    # Constructor
    def __init__(self):
        self.visited = []
        self.end_search = False


    def UCS(self, graph, start_node, goal_node):
        frontier = []
        frontier_i = {}
        node = (0, start_node, [start_node])
        frontier_i[node[1]] = [node[0], node[2]]
        heapq.heappush(frontier, node)
        explored = set()
        while frontier:
            if len(frontier) == 0:
                return []
            node = heapq.heappop(frontier)
            del frontier_i[node[1]]
            if node[1] == goal_node:
                self.visited.append(node)
                return node
            explored.add(node[1])
            neighbours = list(graph.neighbors(node[1]))
            path = node[2]
            for child in neighbours:
                path.append(child)
                childNode = (
                    str(node[0]) + str(graph.get_edge_data(node[1], child)["weight"]), child, path)
                if child not in explored and child not in frontier_i:
                    heapq.heappush(frontier, childNode)
                    frontier_i[child] = [childNode[0], childNode[2]]
                elif child in frontier_i:
                    if childNode[0] < frontier_i[child][0]:
                        tmp = (
                            frontier_i[child][0], child, frontier_i[child][1])
                        frontier.remove(tmp)
                        heapq.heapify(frontier)
                        del frontier_i[child]

                        heapq.heappush(frontier, childNode)
                        frontier_i[child] = [childNode[0], childNode[2]]
                path = path[:-1]
