import traceback
import re
from dataclasses import dataclass

# Define seeds datatype
@dataclass
class seedData:
  seed   : int
  mapped : bool

# Get numbers from line
def get_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(seedData(int(m.group()), False))
  return nums


# Main loop
least       = 0
sectionNum  = 0
seeds       = []
with open('day5_input.txt') as f:
  try:
    for line in f.readlines():
      # Get seeds from first line
      if (sectionNum == 0):
          seeds = get_nums(line)
          sectionNum += 1
          print(f"seeds:{seeds}")

      if (sectionNum > 1):
        nums = get_nums(line)
        if (len(nums) == 3):
          [dstBase, srcBase, rangeLen] = [i.seed for i in nums]
          for s in seeds:
            for r in range(rangeLen):
              if ((s.mapped == False) and ((srcBase + r) == s.seed)):
                s.seed   = dstBase + r
                s.mapped = True
          print(f"seeds:{seeds}")

      # Detect section title, and calculate new info
      if(re.search("map", line)):
        if (sectionNum > 1):
          print("\n.......\n" + line[:-2])
          print(f"sectionNum:{sectionNum}")
          print(f"seeds:{seeds}")
          seeds = [seedData(s.seed, False) for s in seeds]
        sectionNum += 1

    print(f"seeds:{seeds}")
    for s_idx, s in enumerate(seeds):
      if s_idx == 0:
        least = s.seed
      else:
        least = s.seed if (s.seed < least) else least
      print(f"least:{least}")

  except Exception:
    traceback.print_exc()

print(f"final least:{least}")