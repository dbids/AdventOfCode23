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

# Follow dictionaries from seed to location
def follow_dicts(s, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc):
  s = seed2soil.get(s, s)
  s = soil2fert.get(s, s)
  s = fert2water.get(s, s)
  s = water2light.get(s, s)
  s = light2temp.get(s, s)
  s = temp2humid.get(s, s)
  s = humid2loc.get(s, s)
  return s


# Main loop
least       = 0
sectionNum  = 0
seeds       = []
seed2soil   = {}
soil2fert   = {}
fert2water  = {}
water2light = {}
light2temp  = {}
temp2humid  = {}
humid2loc   = {}
# dictList = [{}, {}, {}, {}, {}, {}, {}]
with open('day5_input.txt') as f:
  try:
    for line in f.readlines():
      print(line[:-2])

      # Get seeds from first line
      match sectionNum:
        # seeds
        case 0:
          seeds = get_nums(line)
          sectionNum += 1
          print(f"seeds:{seeds}")

        # seed-to-soil-map
        case 1:
          seed2soil = add_to_dict(line, seed2soil)
          # print(f"seed2soil:{seed2soil}")

        # soil-to-fertilizer map:
        case 2:
          soil2fert = add_to_dict(line, soil2fert)
          # print(f"soil2fert:{soil2fert}")

        # fertilizer-to-water map:
        case 3:
          fert2water = add_to_dict(line, fert2water)
          # print(f"fert2water:{fert2water}")

        # water-to-light map:
        case 4:
          water2light = add_to_dict(line, water2light)
          # print(f"water2light:{water2light}")

        # light-to-temperature map:
        case 5:
          light2temp = add_to_dict(line, light2temp)
          # print(f"light2temp:{light2temp}")

        # temperature-to-humidity map:
        case 6:
          temp2humid = add_to_dict(line, temp2humid)
          # print(f"temp2humid:{temp2humid}")

        # humidity-to-location map:
        case 7:
          humid2loc = add_to_dict(line, humid2loc)
          # print(f"humid2loc:{humid2loc}")

      # Advance sectionNum if section title is detected
      sectionNum += 1 if(re.search("map", line)) else 0
      print(f"sectionNum:{sectionNum}")

    # Then map each seed to a location
    for s_idx, s in enumerate(seeds):
      loc = follow_dicts(s, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc)
      if s_idx == 0:
        least = loc
      else:
        least = loc if (loc < least) else least
      print(f"least:{least}")

  except:
    print(exception)

print(f"least:{least}")