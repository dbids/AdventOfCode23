input_strs = []
with open('day2_sample1.txt') as f:
    for line in f.readlines():
      try:
        input_strs.append(line)
        print(line)

      except:
        print(exception)

print(input_strs)
