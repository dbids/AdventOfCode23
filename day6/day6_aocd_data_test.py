import traceback
import re
from aocd import submit
from aocd import data
import sys


def getRaces(time_line, dist_line):
  races = []
  times = re.findall(r'[0-9]+', time_line)
  dists = re.findall(r'[0-9]+', dist_line)
  if (len(times) != len(dists)):
    Exception("times and dists not equal")
  for t_idx, t in enumerate(times):
    races.append((int(t), int(dists[t_idx])))
  return races

def getNumWinners(duration, recordDist):
  numWinners = 0
  for d in range(duration):
    dist = d * (duration - d)
    if (dist > recordDist):
      numWinners += 1
  return numWinners


if __name__ == "__main__":
  day = 6
  ans = 1
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line for line in f.readlines()]
    else:
      dataList = data.split('\n')
    print(dataList)


    time_line = dataList[0]
    dist_line = dataList[1]
    races = getRaces(time_line=time_line, dist_line=dist_line)
    print(f"races{races}")

    numWinnersList = [None] * len(races)
    for r_idx, r in enumerate(races):
      print(r)
      numWinnersList[r_idx] = getNumWinners(r[0], r[1])
    print(f"numWinnersList{numWinnersList}")

    for nw in numWinnersList:
      ans *= nw

  except Exception:
    traceback.print_exc()

  # Submit via advent-of-code-data
  print(f"ans:{ans}")
  # submit(ans, part="a", day=6, year=2023)