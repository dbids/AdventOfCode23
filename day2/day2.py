import re

def get_day_id(line):
  line = (re.search(r'Game\s[0-9]+', line)).group()
  line = (re.search(r'[0-9]+', line)).group()
  return int(line)

def get_num_tot_val(lines):
  tot = 0
  for l in lines:
    tot += int((re.search(r'[0-9]+', l)).group())
  return tot

def get_red_tot_val(line):
  lines = (re.findall(r'[0-9]+\sred', line))
  return get_num_tot_val(lines)

def get_blue_tot_val(line):
  lines = (re.findall(r'[0-9]+\sblue', line))
  return get_num_tot_val(lines)

def get_green_tot_val(line):
  lines = (re.findall(r'[0-9]+\sgreen', line))
  return get_num_tot_val(lines)

# Main file loop
sum_of_possible_days = 0
with open('day2_input.txt') as f:
    for line in f.readlines():
      try:
        print(line)
        id = get_day_id(line)
        print(f"id: {id}")

        # Split on semicolon for sets
        split_lines = line.split(';')

        # Iterate through split strings
        line_is_possible = True
        for sline in split_lines:
          red = get_red_tot_val(sline)
          print(f"red: {red}")
          blue = get_blue_tot_val(sline)
          print(f"blue: {blue}")
          green = get_green_tot_val(sline)
          print(f"green: {green}")
          if (red > 12 or blue > 14 or green > 13):
            line_is_possible = False

        if (line_is_possible):
          sum_of_possible_days += id
          print(f"incrementing sum_of_possible_days: {sum_of_possible_days}")

      except:
        print(exception)

print(f"sum_of_possible_days: {sum_of_possible_days}")
