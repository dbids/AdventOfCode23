import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
from dataclasses import dataclass
from enum import Enum
import numpy as np

class DirectionEnum(Enum):
  NORTH = 0
  WEST  = 1
  SOUTH = 2
  EAST  = 3

# Sort dem rocks
def organizeRocks(column):
  # Split column on '#'
  hashtag_sections = np.split(column, np.where(column == '#')[0])
  ic(hashtag_sections)
  
  # Sort, creating a second list with $ instead of O
  for hs_idx, hs in enumerate(hashtag_sections):
    hashtag_sections[hs_idx] = np.array(['$' if c == 'O' else c for c in hs])
    hashtag_sections[hs_idx].sort(axis=0)
    
  # Flatten and return
  column = np.concatenate(hashtag_sections)
  ic(column)
  
  return column

    

# Part A
def part_a(dataList):
  ans_a = 0
  ic.disable()
  
  ic(dataList)
  
  # Convert dataList into numpy matrix of chars and transpose it
  dataArray = np.array([list(line) for line in dataList], dtype=str)
  dataArray = dataArray.transpose()
  ic(dataArray)
  
  # Deal with tilt
  for column_idx, column in enumerate(dataArray):
    dataArray[column_idx] = organizeRocks(column)
  ic(dataArray)
  
  
  # Get the sum of the weights
  for column_idx, column in enumerate(dataArray):
    rock_weights = np.where(np.flipud(column) == '$')[0]
    ans_a += sum(rock_weights) + len(rock_weights)

  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  
  ic.disable()
  
  ic(dataList)
  
  # Convert dataList into numpy matrix of chars
  dataArray = np.array([list(line) for line in dataList], dtype=str)
  ic(dataArray)
  
  # Loop over cycles
  dataArrayList = []
  period = 0
  transient = 0
  for cycle in range(1000000000):
    ic("starting cycle: \t{}".format(cycle))
    for direction in DirectionEnum:
      ic(direction)
      # For North Flip compute on the columns
      if (direction == DirectionEnum.NORTH):
        for column_idx, column in enumerate(dataArray.transpose()):
          ic(column)
          dataArray[:, column_idx] = organizeRocks(column)
          
      # For West compute on the rows
      elif (direction == DirectionEnum.WEST):
        for row_idx, row in enumerate(dataArray):
          ic(row)
          dataArray[row_idx] = organizeRocks(row)

      # For South compute on the flipped columns
      elif (direction == DirectionEnum.SOUTH):
        for column_idx, column in enumerate(dataArray.transpose()):
          ic(column)
          dataArray[:, column_idx] = np.flipud(organizeRocks(np.flipud(column)))
          
      # For east compute on the flipped rows
      else:
        for row_idx, row in enumerate(dataArray):
          ic(row)
          dataArray[row_idx] = np.flipud(organizeRocks(np.flipud(row)))
          
    # Find when it enters a loop
    # ic.enable()
    if (cycle > 0):
      for dal_idx, dal in enumerate(dataArrayList):
        if np.array_equal(dal,dataArray):
          period = cycle - dal_idx
          transient = dal_idx
          ic(dal, dataArray, dal_idx)
          break
    if period != 0:
      ic(dataArrayList)
      ic(period, transient)
      break
    dataArrayList.append(np.copy(dataArray))
    # ic.disable()

  # Calculate the dataArray for the 1,000,000 iter
  dal_idx = ((1000000000 - 1 - transient) % period) + transient
  dataArray = dataArrayList[dal_idx]

  # Get the sum of the weights
  for column_idx, column in enumerate(dataArray.transpose()):
    rock_weights = np.where(np.flipud(column) == '$')[0]
    ans_b += sum(rock_weights) + len(rock_weights)

  return ans_b

# Main loop
if __name__ == "__main__":
  day = 14
  ic.configureOutput(prefix='', includeContext=True)
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
