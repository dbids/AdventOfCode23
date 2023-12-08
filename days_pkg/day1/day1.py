# Get numbers from each line in list
input_strs = []
with open('day1_input.txt') as f:
    for line in f.readlines():
      try:
        # Find the start index for all occurances of a string based number
        # can share letter and there can be multiple occurances of the same number
        string_nums = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        string_num_idxs = []
        temp_line = line
        for (sn_idx, sn) in enumerate(string_nums):
          sn_occurrences=[]
          while(temp_line.find(sn)!=-1):
              # find and append
              found_idx = temp_line.find(sn)
              sn_occurrences.append(found_idx)
              # sneaky replace second letter of word to remove it from matching again
              temp_line_list = list(temp_line)
              temp_line_list[found_idx+1] = "*"
              temp_line = "".join(temp_line_list)

          for sno in sn_occurrences:
            string_num_idxs.append((sno,str(sn_idx+1)))

        # Get ints from each line, including string based numbers
        temp_str = ''
        for (char_idx, char) in enumerate(line):
          if char.isdigit():
            temp_str = temp_str + char
          else:
            for snii in string_num_idxs:
              if char_idx == snii[0]:
                temp_str = temp_str + str(snii[1])
        input_strs.append(temp_str)
      except:
        print(exception)

print(input_strs)

# Make the first and last num into two digit number and sum
sum = 0
for input_str in input_strs:
  sum += int(input_str[0] + input_str[-1])

print(sum)