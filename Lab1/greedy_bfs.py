# Importing the Python Queue library
from queue import Queue
 
#Dictionary that stores the adjacent nodes of each node
adj_list = {
    "SportsComplex":["Siwaka"],
    "Siwaka":["SportsComplex", "Ph.1A", "Ph.1B"],
    "Ph.1A":["Siwaka", "Ph.1B", "Mada"],
    "Mada":["Ph.1A", "ParkingLot", "J1"],
    "Ph.1B":["Siwaka", "Ph.1A", "Phase2", "STC"],
    "Phase2":["Ph.1B", "STC", "J1", "Phase3"],
    "STC":["Ph.1B", "Phase2", "ParkingLot"],
    "ParkingLot":["STC", "Phase3", "Mada"],
    "J1":["Phase2", "Mada"],
    "Phase3":["Phase2", "ParkingLot"]
}

# Implementing the algorithm

explored = {}             # Dictionary to keep track of the visited nodes
level = {}                # Dictionary to keep track of the distances from start node
parent = {}               # Dictionary to keep track of the parent of each node
bfs_traversal_output = [] # List to store the order of the bfs traversal
frontier = Queue()        # Initializing an empty queue

# Setting the default values
for node in adj_list.keys():
  explored[node] = False
  level[node] = -1
  parent[node] = None


s = "SportsComplex" # Defining the start node
explored[s] = True  # Marking the start node as explored
level[s] = 0        # Defining the level of the start node as zero
frontier.put(s)     # Adding the start node to the queue

while not frontier.empty():
  u = frontier.get()              # Popping the first element in the queue
  bfs_traversal_output.append(u)  # Adding the vertex u as a visited node
  
  # Exploring the adjacent vertices of u
  for v in adj_list[u]:
    if not explored[v]:
      explored[v] = True  # Marking the vertex as explored if it has not yet been visited
      parent[v] = u
      level[v] = level[u]+1
      frontier.put(v)     # Adding the vertex v to the queue

print (bfs_traversal_output)