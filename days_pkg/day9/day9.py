import traceback
from aocd import submit
from aocd import get_data
import sys
import re

# Get numbers from line
def get_nums(line):
  nums = line.split(' ')
  nums = [int(n) for n in nums]
  return nums

# Get difference numbers from a single set of numbers and last num from each
def get_diffs_and_last(nums):
  newNums = []
  for n_idx, n in enumerate(nums):
    if n_idx > 0:
      prevNum = nums[n_idx-1]
      newNums.append(n - prevNum)
  return (newNums, nums[-1])

# Get difference numbers from a single set of numbers and first num for each
def get_diffs_and_first(nums):
  newNums = []
  for n_idx, n in enumerate(nums):
    if n_idx > 0:
      prevNum = nums[n_idx-1]
      newNums.append(n - prevNum)
  return (newNums, nums[0])

# Part A
def part_a(dataList):
  ans_a = 0

  # Iterate over lines
  for line in dataList:
    #Setup
    currNums = get_nums(line)
    # print(f"currNums{currNums}")
    lastNums = []
    level = 0

    # Find the last nums and number of levels
    while not(not currNums or currNums.count(0) == len(currNums)):
      (currNums, lastNum) = get_diffs_and_last(currNums)
      # print(f"currNums{currNums}")
      lastNums.append(lastNum)
      level += 1

    # Iterate over the last nums to find the history value
    ans_a += sum(lastNums)
    # print(f"lastNums {lastNums}")
    # print(f"level {level}")
    # print(f"Incrementing ans_a by: {sum(lastNums)}")

  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0

  # Iterate over lines
  for line in dataList:
    #Setup
    currNums = get_nums(line)
    # print(f"currNums{currNums}")
    firstNums = []
    level = 0

    # Find the last nums and number of levels
    while not(not currNums or currNums.count(0) == len(currNums)):
      (currNums, firstNum) = get_diffs_and_first(currNums)
      # print(f"currNums{currNums}")
      firstNums.append(firstNum)
      level += 1

    # Iterate over the last nums to find the history value
    oldNum = 0
    newNum = 0
    for fn in reversed(firstNums):
      oldNum = newNum
      newNum = fn - oldNum
    ans_b += newNum
    # print(f"firstNums {firstNums}")
    # print(f"level {level}")
    # print(f"Incrementing ans_a by: {newNum}")

  return ans_b

# Main loop
if __name__ == "__main__":
  day = 9
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

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
  