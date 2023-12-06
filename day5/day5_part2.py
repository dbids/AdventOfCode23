import traceback
import re
from dataclasses import dataclass

# Define seeds datatype
@dataclass
class seedData:
  seed_base   : int
  seed_range  : int
  matched     : bool

def printSeeds(seeds):
  print("seeds:\n")
  for s in seeds:
    print(f"\t(seed_base={s.seed_base}, seed_bound={s.seed_base + s.seed_range}, seed_range={s.seed_range}, matched={s.matched}")

# Get numbers from line
def get_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(int(m.group()))
  return nums

# Get full list of seeds for part 2
def getSeedsFromNums(seeds):
  seeds_out = []
  if (len(seeds) % 2 == 1):
    Exception("Odd num of seeds")

  for s_idx, s in enumerate(seeds):
    if (s_idx % 2): # is odd
      seeds_out.append(seedData(seeds[s_idx-1], s, False))
  return seeds_out

# Checks if two ranges overlap
def range_overlapping(s, t):
  if s.start == s.stop or t.start == t.stop or s.stop == t.start or s.start == t.stop:
    return False
  return s.start <= t.stop and t.start <= s.stop

# Calculates the max and min of the matching and not matching ranges
def calc_overlap(s, t):
  unmatch2 = None
  # Case 1:
  # Seed    : -----------------
  # Target  :     -----------------
  # Match   :     -------------
  # Unmatch : ----
  if s.start < t.start and s.stop <= t.stop:
    match   = range(t.start, s.stop)
    unmatch = range(s.start, t.start)
  # Case 2:
  # Seed    :    --------------
  # Target  : ---------------------
  # Match   : -----------------
  # Unmatch :
  elif s.start >= t.start and s.stop <= t.stop:
    match   = range(s.start, s.stop)
    unmatch = None
  # Case 3:
  # Seed    :     --------------------  
  # Target  : ---------------------
  # Match   :     -----------------
  # Unmatch :                      ---
  elif s.start >= t.start and s.stop > t.stop:
    match   = range(s.start, t.stop)
    unmatch = range(t.stop, s.stop)
  # Case 4:
  # Seed    : ------------------------  
  # Target  :     -----------------
  # Match   :     -----------------
  # Unmatch : ----                 ---
  else: # s.start < t.start and s.stop > t.stop
    match = range(t.start, t.stop)
    unmatch = range(s.start, t.start)
    unmatch2 = range(t.stop, s.stop)
  return (match, unmatch, unmatch2)


# Update seeds depending on each line
def updateSeed(s, dstBase, srcBase, rangeLen):
  seedMax = s.seed_base + s.seed_range
  seedRangeObj = range(s.seed_base, seedMax)
  targRangeObj = range(srcBase, srcBase + rangeLen)
  listOfSeeds = []
  if (range_overlapping(seedRangeObj, targRangeObj)) :
    (match, unmatch, unmatch2) = calc_overlap(seedRangeObj, targRangeObj)
    # print("OVERLAP")
    # print(f"seedRangeObj{seedRangeObj}")
    # print(f"targRangeObj{targRangeObj}")
    # print(f"(match, unmatch, unmatch2){(match, unmatch, unmatch2)}")

    listOfSeeds = [seedData(seed_base=match.start + (dstBase - srcBase), 
                            seed_range = match.stop - match.start, 
                            matched=True)]
    if unmatch is not None: 
      listOfSeeds.append(seedData(seed_base=unmatch.start, 
                                  seed_range = (unmatch.stop - unmatch.start), 
                                  matched=False))
    if unmatch2 is not None: 
      listOfSeeds.append(seedData(seed_base=unmatch2.start, 
                                  seed_range = (unmatch2.stop - unmatch2.start), 
                                  matched=False))
    # print(f"listOfSeeds{listOfSeeds}")
  return listOfSeeds


# Main loop
if __name__ == "__main__":  # confirms that the code is under main function
  least       = 0
  sectionNum  = 0
  seeds       = []
  with open('day5_input.txt') as f:
    try:
      for line in f.readlines():
        # Get seeds from first line
        if (sectionNum == 0):
            seeds = get_nums(line)
            seeds = getSeedsFromNums(seeds=seeds)
            sectionNum += 1
            # printSeeds(seeds)

        # Update seeds for each map
        if (sectionNum > 1):
          nums = get_nums(line)
          if (len(nums) == 3):
            [dstBase, srcBase, rangeLen] = nums
            newSeeds = []
            for s_idx, s in enumerate(seeds):
              if (s.matched == False):
                listOfSeeds = updateSeed(s=s, dstBase=dstBase, srcBase=srcBase, rangeLen=rangeLen)
                if (len(listOfSeeds) > 0):
                  seeds[s_idx] = listOfSeeds[0]
                if (len(listOfSeeds) > 1):
                  newSeeds.append(listOfSeeds[1])
                if (len(listOfSeeds) > 2):
                  newSeeds.append(listOfSeeds[2])
            if (len(newSeeds) > 0): seeds.extend(newSeeds)
            # printSeeds(seeds)

        # Detect section title, and calculate new info
        if(re.search("map", line)):
          if (sectionNum > 1):
            print("\n.......\n" + line[:-2])
            print(f"sectionNum:{sectionNum}")
            seeds = [seedData(s.seed_base, s.seed_range, False) for s in seeds]
            printSeeds(seeds)
          sectionNum += 1

      # Find smallest loc
      # printSeeds(seeds)
      for s_idx, s in enumerate(seeds):
        if s_idx == 0:
          least = s.seed_base
        else:
          least = s.seed_base if (s.seed_base < least) else least
        print(f"least:{least}")

    except Exception:
      traceback.print_exc()

  print(f"final least:{least}")