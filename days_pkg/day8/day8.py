import traceback
from aocd import submit
from aocd import get_data
import sys
import re
from math import lcm


# setup graph as dict of lists
def setupGraph(dataList):
  graphDict = {}
  for l in dataList[2:]:
    # print(f"l: {l}")
    matchList = re.findall(r'[0-9A-Z]+', l)
    # print(f"matchList{matchList}")
    edges = []
    for m in matchList[1:]:
      edges.append(m)
    graphDict[matchList[0]] = edges
  return graphDict


# Traverse the graph from a single start point
def traverseToEnd(graphDict, g, movementPattern):
  numSteps = 0
  while 'Z' not in g:
    # print(f'Start of movement pattern, movementPattern={movementPattern}, g={g}')
    for mp in movementPattern:
      # pre_g = g
      g = graphDict[g][1] if (mp == 'R') else graphDict[g][0]
      # print(f'Going {mp} from {pre_g} to {g}')
      numSteps += 1
      if 'Z' in g: break
  return numSteps


# Traverse a single step
def traverseStep(graphDict, g, mp):
  # pre_g = g
  g = graphDict[g][1] if (mp == 'R') else graphDict[g][0]
  # print(f'Going {mp} from {pre_g} to {g}')
  if 'Z' in g:
    return (True,g)
  return (False,g)


# Traverse until you are at a loop
def traverseToLoop(graphDict, g, movementPattern):
  numSteps = 0
  mp_idx = 0
  Zpattern = []
  postZ_g = g
  postZ_mp = movementPattern[mp_idx]
  wasZ = False
  while True:
    # Traverse a step in the graph
    mp = movementPattern[mp_idx]
    (isZ,g) = traverseStep(graphDict=graphDict, g=g, mp=mp)
    mp_idx = 0 if(mp_idx + 1 == len(movementPattern)) else mp_idx+1
    numSteps += 1

    # Detect loop and break
    if (wasZ):
      if (g == postZ_g and mp == postZ_mp):
        if(Zpattern[-1] == Zpattern[-2]):
          Zpattern.pop()
        break
      postZ_g = g
      postZ_mp = mp
      wasZ = False

    # If at Z add to Z pattern
    if isZ:
      Zpattern.append(numSteps)
      numSteps = 0
      wasZ = True

  return (Zpattern)


# Part A
def part_a(dataList):
  # Get movement pattern
  movementPattern = dataList[0]

  # Setup graph
  graphDict = setupGraph(dataList)
  # print(f"graphDict{graphDict}")

  # Move until you reach ZZZ
  g = 'AAA'
  numSteps = traverseToEnd(graphDict=graphDict, g=g, movementPattern=movementPattern)
  return numSteps


# Part B
def part_b(dataList):
  # Get movement pattern
  movementPattern = dataList[0].split('\n')[0]

  # Setup graph
  graphDict = setupGraph(dataList)
  # print(f"graphDict{graphDict}")

  # Get key of start spaces
  startKeys = [k for k in graphDict.keys() if 'A' in k]
  # print(f"startKeys{startKeys}")

  # Move until you reach a loop
  Zpatterns = [True for i in range(len(startKeys))]
  for g_idx, g in enumerate(startKeys):
    Zpatterns[g_idx] = traverseToLoop(graphDict=graphDict, g=g,
                                        movementPattern=movementPattern)
  # print(Zpatterns)

  # If all the Z patterns have len(1) then find the LCM
  if all(1 == len(i) for i in Zpatterns):
    Zpatterns = tuple([z[0] for z in Zpatterns])
    return lcm(*Zpatterns)
  else:
    # Loop through Z patterns until you find a match
    Zpatterns_idx = [0 for i in range(len(startKeys))]
    Zsums = [0 for i in range(len(startKeys))]
    while True:
      
      # Find the smallest index and add the current Zsum (lowest idx default)
      minpos = Zsums.index(min(Zsums))

      # Update that position
      Zsums[minpos] += Zpatterns[minpos][Zpatterns_idx[minpos]]
      if (Zpatterns_idx[minpos] != len(Zpatterns[minpos])-1):
        Zpatterns_idx[minpos] += 1
      # print(f"Zsums: {Zsums}")
      
      # Check for all equal sums
      if (not Zsums or Zsums.count(Zsums[0]) == len(Zsums)):
        break
  return Zsums[0]


# Main loop
if __name__ == "__main__":
  day = 8
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample2.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')
    
    # ans_a = part_a(dataList=dataList)
    # print(f"ans_a:{ans_a}")
    # submit(ans_a, part="a", day=day, year=2023)

    ans_b = part_b(dataList=dataList)
    # print(f"ans_b:{ans_b}")
    submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
  