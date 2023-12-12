import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic

# Use dynamic programming / recursion to find the solution
# Basic idea:
#  iterate through groups choosing ? to represent # or . with the knowledge that
#  # : extends a group
#  . : can close a group or be skipped
#  recur back the number of solutions that work with the given sizes
def findNumSol(record, sizes, num_done_in_group=0):

  # When we reach the bottom of the tree return without calculating
  if not record:
    # Is this a solution? Did we handle and close all groups?
    return not sizes and not num_done_in_group

  # If not at bottom of tree, keep going
  numSol = 0
  # If next letter is a "?", we branch between "." and "#" in the tree
  branches = [".", "#"] if record[0] == "?" else record[0]
  for c in branches:
    ic(record, sizes, c)
    if c == "#":
      # Extend current group by going to the next character in the record
      ic("extending group", num_done_in_group)
      numSol += findNumSol(record[1:], sizes, num_done_in_group + 1)
    else:
      if num_done_in_group:
        # If we were in a group that can be closed, close it
        ic("closing group", num_done_in_group)
        if sizes and sizes[0] == num_done_in_group:
          ic("group matches size, close it")
          numSol += findNumSol(record[1:], sizes[1:])
      else:
        # If we are not in a group, move on to next symbol
        ic("not in group")
        numSol += findNumSol(record[1:], sizes)
  ic(numSol)
  return numSol

# Part A
def part_a(dataList):
  # Split out record and sizes
  lines = [(line.split(' ')[0]+ ".", # records with appended "." for easy end of line detection
            [int(size) for size in str(line.split(' ')[1]).split(',')])
            for line in dataList]
  ic(lines)

  ic.disable()

  return sum([findNumSol(record, sizes, 0) for record, sizes in lines])

# Part B
def part_b(dataList):
  # Split out record and sizes
  lines = [(line.split(' ')[0],
            [int(size) for size in str(line.split(' ')[1]).split(',')])
            for line in dataList]

  ic(lines)

  # Extend records with "?" in between
  # records with appended "." for easy end of line detection
  # Extend sizes as well with some peak coding
  lines = [((record + '?')*4 + record + ".",
            sizes * 5)
            for record, sizes in lines]

  ic(lines)

  ic.disable()

  return sum([findNumSol(record, sizes, 0) for record, sizes in lines])

# Main loop
if __name__ == "__main__":
  day = 12
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

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
