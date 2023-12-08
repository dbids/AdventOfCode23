import traceback
from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
import operator
from aocd import submit
from aocd import get_data
import sys

# Define hands datatype
@dataclass
class handData:
  hand      : str
  bid       : int
  strength  : int
  orig_hand : str

# Calculate Strength
# 5 of a kind : 6
# 4 of a kind : 5
# full-house  : 4
# 3 of a kind : 3
# two pair    : 2
# one pair    : 1
# high card   : 0
def calcStrength(hand):
  # Get dict of occurances of each num
  occurDict = defaultdict(int)
  for c in hand:
    occurDict[c] += 1
  # print(occurDict)

  # Get values
  occurDict = Counter(occurDict.values())
  # print(occurDict)

  # Get strength
  if (occurDict.get(5, 0)):
    return 6
  elif (occurDict.get(4, 0)):
    return 5
  elif (occurDict.get(3, 0)):
    if (occurDict.get(2, 0)):
        return 4
    return 3
  return occurDict.get(2, 0)

# Calculate Strength
# 5 of a kind : 6
# 4 of a kind : 5
# full-house  : 4
# 3 of a kind : 3
# two pair    : 2
# one pair    : 1
# high card   : 0
def calcStrength_partb(hand):
  # Get dict of occurances of each num
  occurDict = defaultdict(int)
  for c in hand:
    occurDict[c] += 1
  # print(occurDict)

  # Get values
  numJokers = occurDict.pop('1', 0)
  occurDict = Counter(occurDict.values())
  # print(occurDict)

  # Get strength
  if (occurDict.get(5, 0)):
    return 6
  elif (occurDict.get(4, 0)):
    return 5 + numJokers
  elif (occurDict.get(3, 0)):
    if (occurDict.get(2, 0)):
        return 4
    elif numJokers:
      return 4 + numJokers 
    return 3
  elif occurDict.get(2, 0) == 2:
    if numJokers == 1:
      return 4
    return 2
  elif occurDict.get(2, 0) == 1:
    if numJokers == 3:
      return 6
    elif numJokers == 2:
      return 5
    elif numJokers == 1:
      return 3
    return 1
  else:
    if numJokers == 5:
      return 6
    elif numJokers == 4:
      return 6
    elif numJokers == 3:
      return 5
    elif numJokers == 2:
      return 3
    elif numJokers == 1:
      return 1
    return 0

# Transform hand string to sort properly
def transformHand(line):
  outline = ''
  for l in line:
    if (l == 'A'):
      outline = outline + 'Z'
    elif (l == 'K'):
      outline = outline + 'Y'
    elif (l == 'Q'):
      outline = outline + 'X'
    elif (l == 'J'):
      outline = outline + 'W'
    elif (l == 'T'):
      outline = outline + 'V'
    else:
      outline = outline + l
  return outline

# Transform hand string to sort properly
def transformHand_partb(line):
  outline = ''
  for l in line:
    if (l == 'A'):
      outline = outline + 'Z'
    elif (l == 'K'):
      outline = outline + 'Y'
    elif (l == 'Q'):
      outline = outline + 'X'
    elif (l == 'J'):
      outline = outline + '1'
    elif (l == 'T'):
      outline = outline + 'V'
    else:
      outline = outline + l
  return outline

# Get hand object
def getHand(line):
  hand = line[0:5]
  thand = transformHand(line[0:5])
  bid = int(line[6:10])
  strength = calcStrength(thand)
  return handData(thand, bid, strength, hand)

# Get hand object
def getHand__partb(line):
  hand = line[0:5]
  thand = transformHand_partb(line[0:5])
  bid = int(line[6:10])
  strength = calcStrength_partb(thand)
  return handData(thand, bid, strength, hand)

# Part A
def part_a(dataList):
  sum = 0
  hands = []
  for line in dataList:
    hands.append(getHand(line))
  
#   print(f"hands:{hands}")
  hands.sort(key=operator.attrgetter('strength', 'hand'))
#   print(f"hands:{hands}")

  for h_idx, h in enumerate(hands):
    sum += (h.bid*(h_idx+1)) 
    # print(f"(h, sum) \t {(h.orig_hand, sum)}")
  return sum

# Part B
def part_b(dataList):
  sum = 0
  hands = []
  for line in dataList:
    hands.append(getHand__partb(line))

  #   print(f"hands:{hands}")
  hands.sort(key=operator.attrgetter('strength', 'hand'))
  #   print(f"hands:{hands}")

  for h_idx, h in enumerate(hands):
    sum += (h.bid*(h_idx+1)) 
    # print(f"(h, sum) \t {(h.orig_hand, sum)}")
  return sum


# Main loop
if __name__ == "__main__":
  day = 7
  try:
    # Get either puzzle input from server or sample from txt as list of strings
    if (len(sys.argv) > 1):
      with open('day' + str(day) + '_sample.txt') as f:
        dataList = [line for line in f.readlines()]
    else:
      dataList = get_data(day=day, year=2023).split('\n')
    
    ans_a = part_a(dataList=dataList)
    print(f"ans_a:{ans_a}")
    submit(ans_a, part="a", day=day, year=2023)

    ans_b = part_b(dataList=dataList)
    print(f"ans_b:{ans_b}")
    submit(ans_b, part="b", day=day, year=2023)


  except Exception:
    traceback.print_exc()