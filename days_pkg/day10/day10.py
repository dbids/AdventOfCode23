import traceback
from aocd import submit
from aocd import get_data
import sys
from collections import defaultdict, deque
from icecream import ic

# This class represents a directed graph using
# adjacency list representation
class Graph:

  # Constructor
  def __init__(self, Vertices):
    # No. of vertices
    self.V = Vertices  # No. of vertices

    # Default dictionary to store graph
    self.graph = defaultdict(list)


  # Function to add an edge to graph
  def addEdge(self, u, v):
    self.graph[u].append(v)


  # Function to ic graph
  def print(self):
    ic(self.graph)

  # Function to find smallest cycle with BFS from source
  def bfs(self, src):

   # Initialize the distance array and set the distance of the source vertex to 0
    dist = [-1] * len(self.graph)
    dist[src] = 0

    # Initialize the BFS queue and add the source vertex
    q = deque([src])

    # Perform BFS
    while q:
        v = q.popleft()
        for neighbor in self.graph[v]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[v] + 1
                q.append(neighbor)
                print(q)
            elif dist[neighbor] >= dist[v]:
                # A cycle is found, return its length
                return dist[v] + dist[neighbor] + 1
    return float('inf')

  # Calculate length of cycle from source
  def girth(self, source):
    min_cycle = float('inf')
    min_cycle = min(min_cycle, self.bfs(source))
    return min_cycle


# Label nodes of graph
def labelNodes(dataList):
  graphLabels = []
  currLabel = 0
  for line in dataList:
    lineLabels = []
    for c in line:
      if (c != '.'):
        lineLabels.append(currLabel)
        currLabel += 1
      else:
        lineLabels.append('.')
    graphLabels.append(lineLabels)
  return (graphLabels, currLabel)

# Add edge in direction
def addNorth(g, graphLabels, l_idx, c_idx):
  if (l_idx != 0 and graphLabels[l_idx-1][c_idx] != '.'):
    ic(f"addNorth{graphLabels[l_idx][c_idx], graphLabels[l_idx-1][c_idx]}")
    g.addEdge(graphLabels[l_idx][c_idx], graphLabels[l_idx-1][c_idx])
  return
def addSouth(g, graphLabels, l_idx, c_idx, length):
  if (l_idx != length-1 and graphLabels[l_idx+1][c_idx] != '.'):
    ic(f"addSouth{graphLabels[l_idx][c_idx], graphLabels[l_idx+1][c_idx]}")
    g.addEdge(graphLabels[l_idx][c_idx], graphLabels[l_idx+1][c_idx])
  return
def addWest(g, graphLabels, l_idx, c_idx):
  if (c_idx != 0 and graphLabels[l_idx][c_idx-1] != '.'):
    ic(f"addWest{graphLabels[l_idx][c_idx], graphLabels[l_idx][c_idx-1]}")
    g.addEdge(graphLabels[l_idx][c_idx], graphLabels[l_idx][c_idx-1])
  return
def addEast(g, graphLabels, l_idx, c_idx, length):
  if (c_idx != length-1 and graphLabels[l_idx][c_idx+1] != '.'):
    ic(f"addEast{graphLabels[l_idx][c_idx], graphLabels[l_idx][c_idx+1]}")
    g.addEdge(graphLabels[l_idx][c_idx], graphLabels[l_idx][c_idx+1])
  return

# Add nodes to graph from data
def createGraph(dataList, graphLabels, numVerticies):
  g = Graph(numVerticies)
  sIndex = 0
  for l_idx, line in enumerate(dataList):
     for c_idx, c in enumerate(line):
        if (c != '.'):
          match(c):
            case '|':
              addNorth(g, graphLabels, l_idx, c_idx)
              addSouth(g, graphLabels, l_idx, c_idx, len(dataList))
            case '-':
              addWest(g, graphLabels, l_idx, c_idx)
              addEast(g, graphLabels, l_idx, c_idx, len(line))
            case 'L':
              addNorth(g, graphLabels, l_idx, c_idx)
              addEast(g, graphLabels, l_idx, c_idx, len(line))
            case 'J':
              addNorth(g, graphLabels, l_idx, c_idx)
              addWest(g, graphLabels, l_idx, c_idx)
            case '7':
              addSouth(g, graphLabels, l_idx, c_idx, len(dataList))
              addWest(g, graphLabels, l_idx, c_idx)
            case 'F':
              addSouth(g, graphLabels, l_idx, c_idx, len(dataList))
              addEast(g, graphLabels, l_idx, c_idx, len(line))
            case 'S':
              if (dataList[l_idx-1][c_idx] == '|' or
                  dataList[l_idx-1][c_idx] == '7' or
                  dataList[l_idx-1][c_idx] == 'F'):
                addNorth(g, graphLabels, l_idx, c_idx)
              if (dataList[l_idx+1][c_idx] == '|' or
                  dataList[l_idx+1][c_idx] == 'L' or
                  dataList[l_idx+1][c_idx] == 'J'):
                addSouth(g, graphLabels, l_idx, c_idx, len(dataList))
              if (dataList[l_idx][c_idx-1] == '-' or
                  dataList[l_idx][c_idx-1] == 'L' or
                  dataList[l_idx][c_idx-1] == 'F'):
                addWest(g, graphLabels, l_idx, c_idx)
              if (dataList[l_idx][c_idx+1] == '-' or
                  dataList[l_idx][c_idx+1] == 'J' or
                  dataList[l_idx][c_idx+1] == '7'):
                addEast(g, graphLabels, l_idx, c_idx, len(line))
              sIndex = graphLabels[l_idx][c_idx]
  return (g, sIndex)

# Part A
def part_a(dataList):
  ic.disable()
  ic(dataList)

  # Label nodes
  (graphLabels, numVerticies) = labelNodes(dataList)
  ic(graphLabels)

  # Create graph
  (g, sIndex) = createGraph(dataList=dataList, graphLabels=graphLabels, numVerticies=numVerticies)
  g.print()
  ic(sIndex)

  # Find max distance along graph
  ic.enable()
  sys.setrecursionlimit(100000)
  girth = g.girth(sIndex)
  ic(girth)
  if (girth != float('inf')):
    return int((girth)/2)

  return 0

# Part B
def part_b(dataList):
  ans_b = 0
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 10
  ic.configureOutput(prefix='', includeContext=True)
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample2.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')

    ans_a = part_a(dataList=dataList)
    ic(f"ans_a:{ans_a}")
    submit(ans_a, part="a", day=day, year=2023)

    # ans_b = part_b(dataList=dataList)
    # ic(f"ans_b:{ans_b}")
    # submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.ic_exc()
