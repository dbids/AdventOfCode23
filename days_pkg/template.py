import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic

# Part A
def part_a(dataList):
  ans_a = 0
  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 8
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line.split('\n')[0] for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')
    
    ans_a = part_a(dataList=dataList)
    print(f"ans_a:{ans_a}")
    # if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    # ans_b = part_b(dataList=dataList)
    # print(f"ans_b:{ans_b}")
    # if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
  