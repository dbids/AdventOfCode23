sum = 0
with open('day4_sample.txt') as f:
    for line in f.readlines():
      try:
        print(line)

      except:
        print(exception)

print(f"sum:{sum}")