import traceback
from aocd import submit
from aocd import get_data
import sys
from icecream import ic

# Implement H.A.S.H. == Holiday ASCII String Helper algorithm
def HASH(token):
  curr_val = 0
  for c in token:
    curr_val += ord(c)
    curr_val *= 17
    curr_val %= 256
  return curr_val

# Part A
def part_a(dataList):
  ans_a = 0

  ic.disable()
  ic(dataList)

  for token in dataList:
    ic(token)
    hash_val = HASH(token)
    ic(hash_val)
    ans_a += hash_val
  return ans_a

# Part B
def part_b(dataList):
  ans_b = 0
  return ans_b

# Main loop
if __name__ == "__main__":
  day = 15
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = f.readlines()[0].split(',')
    else:
      dataList = get_data(day=day, year=2023).split(',')

    ans_a = part_a(dataList=dataList)
    print(f"ans_a:{ans_a}")
    if (len(sys.argv) <= 1): submit(ans_a, part="a", day=day, year=2023)

    # ans_b = part_b(dataList=dataList)
    # print(f"ans_b:{ans_b}")
    # if (len(sys.argv) <= 1): submit(ans_b, part="b", day=day, year=2023)

  except Exception:
    traceback.print_exc()
