import collections
from dataclasses import dataclass
from dataclasses import replace
import re

# Find index of symbols
def check_for_symbol(line):
  pos = []
  for cidx, char in enumerate(line):
    if (not(char.isdigit() or char == '.' or char == '\n' or char == '\r')):
      pos.append(cidx)
  return pos

# Find start idx, end idx, and value of numbers
@dataclass
class numData:
  start_pos : int
  end_pos : int
  value : int
  used : 0
def check_for_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(numData(m.start(), m.end(), int(m.group()), 0))
  return nums


# Main file loop
sum = 0
three_lines = collections.deque([], 3)
with open('day3_input.txt') as f:
    line_num = -1
    for line in f.readlines():
      # print("..........................................................................")
      try:
        # Store the three lines
        line_num += 1
        three_lines.append(line)
        # print(f"three_lines: {three_lines}")

        if (line_num >= 2):
          # Check the all three lines for numbers
          number_pos = [check_for_nums(three_lines[0]), check_for_nums(three_lines[1]),check_for_nums(three_lines[2])]
          # print(f"number_pos: {number_pos}")

          # Check the middle line for symbol
          symbol_pos = check_for_symbol(three_lines[1])
          # print(f"symbol_pos: {symbol_pos}")

          # Check if numbers are within range of symbols
          for np_idx, np in enumerate(number_pos):
            for npp in np:
              # print(f"npp: {npp}")
              for sp in symbol_pos:
                if ((sp >= npp.start_pos-1) and (sp <= npp.end_pos) and npp.used == 0):
                  npp = replace(npp, used=1)
                  sum += npp.value
                  # print(f"added {npp}")

                  # When number is matched, overwrite it with .'s
                  tll = list(three_lines[np_idx])
                  for tll_idx,_ in enumerate(tll):
                    tll[tll_idx] = '.' if (tll_idx >= npp.start_pos and tll_idx < npp.end_pos) else tll[tll_idx]
                  three_lines[np_idx] = ''.join(tll)

      except:
        print(exception)

print(f"sum: {sum}")

