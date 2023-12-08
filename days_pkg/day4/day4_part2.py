import re

# Get numbers from line
def get_nums(line):
  nums = []
  match_obj = re.finditer(r'[0-9]+', line)
  for m in match_obj:
    nums.append(int(m.group()))
  return nums

# Get num wins
def get_num_wins(your_nums, win_nums):
  num_wins = 0
  for yn in your_nums:
    for wn in win_nums:
      if (yn == wn):
        num_wins += 1
        break
  return num_wins

# Main Loop
sum = 0
card_copies_q = []
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


        # Calculate how many won
        num_wins = get_num_wins(your_nums, win_nums)
        print(f"num_wins{num_wins}")

        # Get number of instances of this card and update FIFO
        num_instances = card_copies_q.pop(0) if (len(card_copies_q) != 0) else 1
        print(f"num_instances{num_instances}")

        if (len(card_copies_q) != 0):
          print(f"card_copies_q before:{card_copies_q}")

        for nw in range(num_wins):
          if nw < len(card_copies_q):
            card_copies_q[nw] += num_instances
          else:
            card_copies_q.append(num_instances + 1)

        if (len(card_copies_q) != 0):
          print(f"card_copies_q after:{card_copies_q}")

        # Increment sum
        sum += num_instances
        print(f"sum:{sum}")
        print("\n")
      except:
        print(exception)

print(f"sum:{sum}")
