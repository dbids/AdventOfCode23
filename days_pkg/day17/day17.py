import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
import numpy as np

# Python program for the shortest path approach
import heapq

# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # In a weighted graph, store vertex and weight pair for every edge

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Function to ic graph
    def print(self):
      ic(self.adj)


    # Prints shortest paths from src to all other vertices
    def shortest_path(self, src):
        # Create a priority queue to store vertices that
        # are being preprocessed.
        pq = [(0, src)]  # The first element of the tuple is the distance, and the second is the vertex label

        # Create a list for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Looping until the priority queue becomes empty
        while pq:
            # The first element in the tuple is the minimum distance vertex
            # Extract it from the priority queue
            current_dist, u = heapq.heappop(pq)

            # Iterate over all adjacent vertices of a vertex
            for v, weight in self.adj[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    # Update the distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Print shortest distances
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

# def mod_dijkstra(dataArray, src):
#   # Create matrix of distances from src
#   dist = np.full_like(dataArray, sys.maxsize, dtype=int)
#   dist[0][0] = 0

#   # Create queue of notvisited nodes
#   Q = np.full_like(dataArray, 1, dtype=int)

#   # While Q is not empty
#   while np.count_nonzero(Q == 1):
#     for



# Part A
def part_a(dataList):
  ans_a = 0

  # ic.disable()
  # ic(dataList)

  # Get dataList as 2d numpy matrix
  dataArray = np.array([[int(char) for char in list(line)] for line in dataList], dtype=int)
  ic(dataArray)
  # ic(dataArray.shape)

  # Create graph
  g = Graph(np.size(dataArray))
  for x in range(len(dataList[0])):
    for y in range(len(dataList)):
      v = y*len(dataList[0]) + x
      u_left = y*len(dataList[0]) + (x-1)
      u_up = (y-1)*len(dataList[0]) + x
      ic(x,y,v,u_left,u_up)
      if (x > 0):
        g.add_edge(u=u_left, v=v, w=dataArray[x][y])
      if (y > 0):
        g.add_edge(u=u_up, v=v, w=dataArray[x][y])
  g.print()

  # Run djiestra's with modification for three of same direction in a row
  g.shortest_path(0)


  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 17
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')

    ans_a = part_a(dataList=dataList)
    print(f"ans_a:{ans_a}")
    # if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    # ans_b = part_b(dataList=dataList)
    # print(f"ans_b:{ans_b}")
    # if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
