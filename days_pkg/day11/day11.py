import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
from collections import defaultdict

class Galaxy:

  # Constructor
  def __init__(self):

    # Default dictionary to store graph
    self.graph = defaultdict(list)

  # Function to add an edge to graph
  def addGalaxy(self, u, x, y):
    self.graph[u].extend([x,y])

  def getX(self, u):
    return self.graph[u][0]
  
  def getY(self, u):
    return self.graph[u][1]
  
  # Function to ic graph
  def print(self):
    ic(self.graph)
  
# Get shortest path between two nodes
def getShortestPath(x1, x2, y1, y2):
  return abs(x1 - x2) + abs(y1 - y2)

# Part A
def part_a(dataList):
  ans_a = 0

  # Find empty rows and columns
  emptyColList = [True for _ in range(len(dataList[0]))]
  emptyRowList = [True for _ in range(len(dataList))]
  for y, line in enumerate(dataList):
    for x, c in enumerate(line):
      if (c == '#'):
        emptyColList[x] = False
        emptyRowList[y] = False

  # Construct the galaxies
  g = Galaxy()
  galaxyNum = 1
  for y, line in enumerate(dataList):
    for x, c in enumerate(line):
      if (c == '#'):
        xEmpty = sum(emptyColList[:x])
        yEmpty = sum(emptyRowList[:y])
        g.addGalaxy(u=galaxyNum, x=x+xEmpty, y=y+yEmpty)
        galaxyNum += 1
  ic(galaxyNum)
  g.print()

  # Find the shortest path lengths between each galaxy
  for gn in range(galaxyNum):
    gn = gn + 1
    targetGalaxNum = galaxyNum - gn - 1
    for tgn_idx in range(targetGalaxNum):
      tgn = tgn_idx + gn + 1
      shortestPath = getShortestPath(g.getX(tgn), g.getX(gn), g.getY(tgn), g.getY(gn))
      ic((gn, tgn, shortestPath))
      ans_a += shortestPath
  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  
  # Find empty rows and columns
  emptyColList = [True for _ in range(len(dataList[0]))]
  emptyRowList = [True for _ in range(len(dataList))]
  for y, line in enumerate(dataList):
    for x, c in enumerate(line):
      if (c == '#'):
        emptyColList[x] = False
        emptyRowList[y] = False

  # Construct the galaxies
  g = Galaxy()
  galaxyNum = 1
  expansionFactor = 999999
  for y, line in enumerate(dataList):
    for x, c in enumerate(line):
      if (c == '#'):
        xEmpty = sum(emptyColList[:x]) * expansionFactor
        yEmpty = sum(emptyRowList[:y]) * expansionFactor
        g.addGalaxy(u=galaxyNum, x=x+xEmpty, y=y+yEmpty)
        galaxyNum += 1
  ic(galaxyNum)
  g.print()

  # Find the shortest path lengths between each galaxy
  for gn in range(galaxyNum):
    gn = gn + 1
    targetGalaxNum = galaxyNum - gn - 1
    for tgn_idx in range(targetGalaxNum):
      tgn = tgn_idx + gn + 1
      shortestPath = getShortestPath(g.getX(tgn), g.getX(gn), g.getY(tgn), g.getY(gn))
      ic((gn, tgn, shortestPath))
      ans_b += shortestPath
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 11
  ic.configureOutput(prefix='', includeContext=True)
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')
    
    ic.disable()
    # ans_a = part_a(dataList=dataList)
    # print(f"ans_a:{ans_a}")
    # if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
  