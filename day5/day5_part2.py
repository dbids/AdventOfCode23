import traceback
import re
from dataclasses import dataclass

# Define seeds datatype
@dataclass
class seedData:
  seed_base   : int
  seed_range  : int
  mapped : bool

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


# Update seeds depending on each line
def updateSeed(s, dstBase, srcBase, rangeLen):
  for r in range(s.seed_range):
    if ((s.mapped == False) and ((srcBase + rangeLen) > s.seed) and ((srcBase) <= s.seed)):
      s.seed   = dstBase + (s.seed - srcBase)
      s.mapped = True
    return s


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
            # print(f"seeds:{seeds}")

        # Update seeds for each map
        if (sectionNum > 1):
          nums = get_nums(line)
          if (len(nums) == 3):
            [dstBase, srcBase, rangeLen] = nums
            for s in seeds:
              s = updateSeed(s=s, dstBase=dstBase, srcBase=srcBase, rangeLen=rangeLen)
            # print(f"seeds:{seeds}")

        # Detect section title, and calculate new info
        if(re.search("map", line)):
          if (sectionNum > 1):
            print("\n.......\n" + line[:-2])
            print(f"sectionNum:{sectionNum}")
            # print(f"seeds:{seeds}")
            seeds = [seedData(s.seed, False) for s in seeds]
          sectionNum += 1

      # Find smallest loc
      # print(f"seeds:{seeds}")
      for s_idx, s in enumerate(seeds):
        if s_idx == 0:
          least = s.seed
        else:
          least = s.seed if (s.seed < least) else least
        print(f"least:{least}")

    except Exception:
      traceback.print_exc()

  print(f"final least:{least}")