sum = 0
with open('day4_sample.txt') as f:
    for line in f.readlines():
      try:
        print(line[:-2])

      except:
        print(Exception)

print(f"sum:{sum}")