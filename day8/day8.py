import traceback
from aocd import submit
from aocd import data
import sys

if __name__ == "__main__":
  day = 8
  ans = 0
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line for line in f.readlines()]
    else:
      dataList = data.split('\n')
    print(dataList)

  except Exception:
    traceback.print_exc()

  # Submit via advent-of-code-data
  print(f"ans:{ans}")
  # submit(ans, part="a", day=day, year=2023)