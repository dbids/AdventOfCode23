import re

# Get numbers from line
def get_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(int(m.group()))
  return nums

# Add to dictionary
def add_to_dict(line, dict_in):
  # Get numbers from line as list
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(int(m.group()))

  # Check that there are only three numbers then
  # calculate dictionary values to add and add them
  if (len(nums) == 3):
    for i in range(nums[2]):
      dstNum = nums[0] + i
      srcNum = nums[1] + i
      dict_in[srcNum] = dstNum

  return dict_in

# Main loop
least       = 0
sectionNum  = 0
seeds       = []
currDict    = {}
with open('day5_input.txt') as f:
  try:
    for line in f.readlines():
      # Get seeds from first line
      if (sectionNum == 0):
          seeds = get_nums(line)
          sectionNum += 1
          print(f"seeds:{seeds}")

      if (sectionNum > 1):
        currDict = add_to_dict(line, currDict)

      # Detect section title, and calculate new info
      if(re.search("map", line)):
        if (sectionNum > 1):
          seeds = [currDict.get(s, s) for s in seeds]
          print("\n.......\n" + line[:-2])
          print(f"sectionNum:{sectionNum}")
          # print(f"currDict:{currDict}")
          print(f"seeds:{seeds}")
        sectionNum += 1
        currDict = {}

    for s_idx, s in enumerate(seeds):
      if s_idx == 0:
        least = s
      else:
        least = s if (s < least) else least
      print(f"least:{least}")

  except:
    print(Exception)

print(f"least:{least}")