import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
from dataclasses import dataclass
from enum import Enum
import numpy as np

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
  
  ic(dataList)
  
  # Convert dataList into numpy matrix of chars and transpose it
  dataArray = np.array([list(line) for line in dataList], dtype=str)
  dataArray = dataArray.transpose()
  ic(dataArray)
  
  # Deal with tilt
  ic.disable()
  for column_idx, column in enumerate(dataArray):
    dataArray[column_idx] = organizeRocks(column)
  ic.enable()
  ic(dataArray)
  
  
  # Get the sum of the weights
  for column_idx, column in enumerate(dataArray):
    rock_weights = np.where(np.flipud(column) == '$')[0]
    ans_a += sum(rock_weights) + len(rock_weights)

  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0

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

    ans_a = part_a(dataList=dataList)
    print(f"ans_a:{ans_a}")
    if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    # ans_b = part_b(dataList=dataList)
    # print(f"ans_b:{ans_b}")
    # if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
