import re

# Get numbers from line
def get_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(int(m.group()))
  return nums

def get_num_wins(your_nums, win_nums):
  num_wins = 0
  for yn in your_nums:
    for wn in win_nums:
      if (yn == wn):
        num_wins += 1
        print(f"num_wins{num_wins}")
        break
  return num_wins

# Main Loop
sum = 0
with open('day4_input.txt') as f:
    for line in f.readlines():
      try:
        # Get numbers
        print(f"{line[:-2]}")
        [_, line] = line.split(':')
        [your_line, win_line] = line.split('|')
        your_nums = get_nums(your_line)
        win_nums = get_nums(win_line)
        print(f"your_nums{your_nums}")
        print(f"win_nums{win_nums}")

        # Increment sum based on how many won
        num_wins = get_num_wins(your_nums, win_nums)
        sum += pow(2, num_wins-1) if (num_wins > 0) else 0
        print("\n")
      except:
        print(exception)

print(f"sum:{sum}")
