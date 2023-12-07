import traceback
from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
import operator

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

# Main loop
if __name__ == "__main__":
  sum = 0
  with open('day7_input.txt') as f:
    try:
      hands = []
      for line in f.readlines():
        hands.append(getHand(line))
      
    #   print(f"hands:{hands}")
      hands.sort(key=operator.attrgetter('strength', 'hand'))
    #   print(f"hands:{hands}")

      print("asda\n")
      for h_idx, h in enumerate(hands):
        sum += (h.bid*(h_idx+1)) 
        print(f"(h, sum) \t {(h.orig_hand, sum)}")


    except Exception:
      traceback.print_exc()

  print(f"sum:{sum}")