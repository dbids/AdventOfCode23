import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic
import numpy as np

# Find reflection in dataArray and return value
def findReflection(dataArray):

  # Check vertical lines
  for vert_mid_idx in range(dataArray.shape[1]-1):
    left_idx = vert_mid_idx
    right_idx = vert_mid_idx + 1
    while np.array_equal(dataArray[:, left_idx],dataArray[:, right_idx]):
      left_idx  -= 1
      right_idx += 1
      if (left_idx == -1 or right_idx == dataArray.shape[1]):
        return (vert_mid_idx+1)

  # Check horizontal lines
  for horz_mid_idx in range(dataArray.shape[0]-1):
    top_idx = horz_mid_idx
    bottom_idx = horz_mid_idx + 1
    while np.array_equal(dataArray[top_idx],dataArray[bottom_idx]):
      top_idx  -= 1
      bottom_idx += 1
      if (top_idx == -1 or bottom_idx == dataArray.shape[0]):
        return 100*(horz_mid_idx+1)

  return 0




# Part A
def part_a(dataList):
  ans_a = 0
  ic.disable()

  ic(dataList)

  base_line_idx = 0
  top_line_idx = 1
  for line_idx, line in enumerate(dataList):

    # Check for empty line
    if (line == "" or line_idx == len(dataList)-1):
      top_line_idx = line_idx + (line_idx == len(dataList)-1)

      # Convert pattern into numpy matrix of chars
      dataArray = np.array([list(line) for line in dataList[base_line_idx:top_line_idx]], dtype=str)
      ic(dataArray)

      # Find reflection in dataArray and return value
      ans_a += findReflection(dataArray=dataArray)

      # Update base line idx
      base_line_idx = top_line_idx+1

  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 13
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
