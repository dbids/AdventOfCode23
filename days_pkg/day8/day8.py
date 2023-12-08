import traceback
from aocd import submit
from aocd import get_data
import sys
import re
from multiprocessing import Pool


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
    print(f'Start of movement pattern, movementPattern={movementPattern}, g={g}')
    for mp in movementPattern:
      # pre_g = g
      g = graphDict[g][1] if (mp == 'R') else graphDict[g][0]
      # print(f'Going {mp} from {pre_g} to {g}')
      numSteps += 1
      if 'Z' in g: break
  return numSteps

# Traverse a single step
def traverseStep(graphDict, g, movementPattern, mp):
  pre_g = g
  g = graphDict[g][1] if (mp == 'R') else graphDict[g][0]
  # print(f'Going {mp} from {pre_g} to {g}')
  if 'Z' in g:
    return (True,g)
  return (False,g)

# Part A
def part_a(dataList):
  # Get movement pattern
  movementPattern = dataList[0].split('\n')[0]

  # Setup graph
  graphDict = setupGraph(dataList)
  print(f"graphDict{graphDict}")

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
  print(f"graphDict{graphDict}")

  # Get key of start spaces
  startKeys = [k for k in graphDict.keys() if 'A' in k]
  print(f"startKeys{startKeys}")

  # # Move until you reach ZZZ
  # numSteps = 0
  # mp_idx=0
  # isZ = [True for i in range(len(startKeys))]
  # while True:
  #   mp = movementPattern[mp_idx]
  #   for g_idx, g in enumerate(startKeys):
  #     (isZ[g_idx],startKeys[g_idx]) = traverseStep(graphDict=graphDict, g=g,
  #                                                  movementPattern=movementPattern, mp=mp)
  #   mp_idx = 0 if(mp_idx + 1 == len(movementPattern)) else mp_idx+1
  #   numSteps += 1
  #   if all(isZ): 
  #     break

  # PARALLEL ALTERNATIVE:
  numSteps = 0
  mp_idx=0
  isZ = [True for i in range(len(startKeys))]
  while True:
    mp = movementPattern[mp_idx]
    with Pool() as pool:
      pool_inputs = [(graphDict, g, movementPattern, mp) for _, g in enumerate(startKeys)]
      for r_idx, result in enumerate(pool.starmap(traverseStep, pool_inputs)):
        isZ[r_idx] = result[0]
        startKeys[r_idx] = result[1]
    mp_idx = 0 if(mp_idx + 1 == len(movementPattern)) else mp_idx+1
    numSteps += 1
    if all(isZ): 
      break
  return numSteps

# Main loop
if __name__ == "__main__":
  day = 8
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample2.txt') as f:
        dataList = [line for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')
    
    # ans_a = part_a(dataList=dataList)
    # print(f"ans_a:{ans_a}")
    # submit(ans_a, part="a", day=day, year=2023)

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
  