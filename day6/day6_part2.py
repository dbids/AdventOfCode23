import traceback
import re

def mashNums(line):
  numStr = ''
  for l in line:
    if l.isdigit():
      numStr = numStr + l
  return(int(numStr))

def getRaces(time_line, dist_line):
  time = mashNums(time_line)
  dist = mashNums(dist_line)
  return (time, dist)

def getNumWinners(duration, recordDist):
  numWinners = 0
  for d in range(duration):
    dist = d * (duration - d)
    if (dist > recordDist):
      numWinners += 1
  return numWinners


if __name__ == "__main__":
  numWinners = 1
  with open('day6_input.txt') as f:
    try:
      time_line = f.readline()
      dist_line = f.readline()
      race = getRaces(time_line=time_line, dist_line=dist_line)
      print(f"race{race}")

      numWinners = getNumWinners(race[0], race[1])

    except Exception:
      traceback.print_exc()

  print(f"numWinners:{numWinners}")