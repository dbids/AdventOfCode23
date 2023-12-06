import traceback
import re

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
  prod = 1
  with open('day6_input.txt') as f:
    try:
      time_line = f.readline()
      dist_line = f.readline()
      races = getRaces(time_line=time_line, dist_line=dist_line)
      print(f"races{races}")

      numWinnersList = [None] * len(races)
      for r_idx, r in enumerate(races):
        print(r)
        numWinnersList[r_idx] = getNumWinners(r[0], r[1])
      print(f"numWinnersList{numWinnersList}")

      for nw in numWinnersList:
        prod *= nw

    except Exception:
      traceback.print_exc()

  print(f"prod:{prod}")