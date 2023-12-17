import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
from enum import Enum
import numpy as np

class DirectionEnum(Enum):
  UP     = 0
  LEFT   = 1
  DOWN   = 2
  RIGHT  = 3

# Use recursion and dynamic programming to beam through matrix, creating visitedArray
def numBeamedTiles(dataArray, visitedArray, dirArray, x, y, dir):

  # Check for looping of the beams
  if(visitedArray[y,x] == True and dirArray[dir.value][y,x] == True):
    return visitedArray

  # Set the tracking arrays to true
  dirArray[dir.value][y,x] = True
  visitedArray[y,x] = True
  ic(x, y, dataArray[y,x], dir.name)

  # Move to next part of the matrix if not at its ends
  match dataArray[y,x]:
    case '.':
      match dir:
        case DirectionEnum.UP:
          if y != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y-1, DirectionEnum.UP)
        case DirectionEnum.LEFT:
          if x != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x-1, y, DirectionEnum.LEFT)
        case DirectionEnum.DOWN:
          if y != (dataArray.shape[0]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y+1, DirectionEnum.DOWN)
        case DirectionEnum.RIGHT:
          if x != (dataArray.shape[1]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x+1, y, DirectionEnum.RIGHT)
    case '\\':
      match dir:
        case DirectionEnum.UP:
          if x != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x-1, y, DirectionEnum.LEFT)
        case DirectionEnum.LEFT:
          if y != 0:
           return numBeamedTiles(dataArray, visitedArray, dirArray, x, y-1, DirectionEnum.UP)
        case DirectionEnum.DOWN:
          if x != (dataArray.shape[1]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x+1, y, DirectionEnum.RIGHT)
        case DirectionEnum.RIGHT:
          if y != (dataArray.shape[0]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y+1, DirectionEnum.DOWN)
    case '/':
      match dir:
        case DirectionEnum.UP:
          if x != (dataArray.shape[1]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x+1, y, DirectionEnum.RIGHT)
        case DirectionEnum.LEFT:
          if y != (dataArray.shape[0]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y+1, DirectionEnum.DOWN)
        case DirectionEnum.DOWN:
          if x != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x-1, y, DirectionEnum.LEFT)
        case DirectionEnum.RIGHT:
          if y != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y-1, DirectionEnum.UP)
    case '|':
      match dir:
        case DirectionEnum.UP:
          if y != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y-1, DirectionEnum.UP)
        case DirectionEnum.DOWN:
          if y != (dataArray.shape[0]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x, y+1, DirectionEnum.DOWN)
        ## BRANCH ON SPLITTER
        case DirectionEnum.LEFT | DirectionEnum.RIGHT:
          if y != 0:
            visitedArray = numBeamedTiles(dataArray, visitedArray, dirArray, x, y-1, DirectionEnum.UP)
          if y != (dataArray.shape[0]-1):
            visitedArray = np.logical_or(visitedArray, numBeamedTiles(dataArray, visitedArray, dirArray, x, y+1, DirectionEnum.DOWN))
    case '-':
      match dir:
        case DirectionEnum.LEFT:
          if x != 0:
            return numBeamedTiles(dataArray, visitedArray, dirArray, x-1, y, DirectionEnum.LEFT)
        case DirectionEnum.RIGHT:
          if x != (dataArray.shape[1]-1):
            return numBeamedTiles(dataArray, visitedArray, dirArray, x+1, y, DirectionEnum.RIGHT)
        ## BRANCH ON SPLITTER
        case DirectionEnum.UP | DirectionEnum.DOWN:
          if x != 0:
            visitedArray = numBeamedTiles(dataArray, visitedArray, dirArray, x-1, y, DirectionEnum.LEFT)
          if x != (dataArray.shape[1]-1):
            visitedArray = np.logical_or(visitedArray, numBeamedTiles(dataArray, visitedArray, dirArray, x+1, y, DirectionEnum.RIGHT))
  ic("ending path")
  return visitedArray

# Start the recursion and sum visitedarray
def startBeaming(dataArray, targetdir, x, y):
  # Create visted array and begin recurring
  visitedArray = np.full_like(dataArray, False, dtype=bool)
  dirArray = [np.full_like(dataArray, False, dtype=bool) for _ in range(4)]
  visitedArray = numBeamedTiles(dataArray=dataArray, visitedArray=visitedArray, dirArray=dirArray,
                                x=x, y=y, dir=targetdir)

  return np.count_nonzero(visitedArray)

# Part A
def part_a(dataList):
  sys.setrecursionlimit(100000)

  ic.disable()
  ic(dataList)

  # Convert pattern into numpy matrix of chars
  dataArray = np.array([list(line) for line in dataList], dtype=str)
  ic(dataArray)
  ic(dataArray.shape)

  # Create visted array and begin recurring
  visitedArray = np.full_like(dataArray, False, dtype=bool)
  dirArray = [np.full_like(dataArray, False, dtype=bool) for _ in range(4)]
  visitedArray = numBeamedTiles(dataArray=dataArray, visitedArray=visitedArray, dirArray=dirArray,
                                x=0, y=0, dir=DirectionEnum.RIGHT)
  ic(visitedArray)

  # Sum the number of True statements and return that value
  return np.count_nonzero(visitedArray)

# Part B
def part_b(dataList):
  sys.setrecursionlimit(100000)

  ic.disable()
  ic(dataList)

  # Convert pattern into numpy matrix of chars
  dataArray = np.array([list(line) for line in dataList], dtype=str)
  ic(dataArray)
  ic(dataArray.shape)

  ans_b = startBeaming(dataArray, DirectionEnum.RIGHT, 0, 0)
  for targetdir in DirectionEnum:
    match targetdir:
      case DirectionEnum.LEFT:
        for y in range(dataArray.shape[0]):
          ans_b = max(ans_b, startBeaming(dataArray, targetdir, dataArray.shape[1]-1, y))
      case DirectionEnum.RIGHT:
        for y in range(dataArray.shape[0]):
          ans_b = max(ans_b, startBeaming(dataArray, targetdir, 0, y))
      case DirectionEnum.UP:
        for x in range(dataArray.shape[1]):
          ans_b = max(ans_b, startBeaming(dataArray, targetdir, x, dataArray.shape[0]-1))  
      case DirectionEnum.DOWN:
        for x in range(dataArray.shape[1]):
          ans_b = max(ans_b, startBeaming(dataArray, targetdir, x, 0))

  # Return the max of the 
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 16
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')

    # ans_a = part_a(dataList=dataList)
    # print(f"ans_a:{ans_a}")
    # if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
