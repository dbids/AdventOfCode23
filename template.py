import traceback

if __name__ == "__main__":
  sum = 0
  with open('day4_sample.txt') as f:
    try:
      for line in f.readlines():
        print(line[:-2])

    except Exception:
      traceback.print_exc()

  print(f"sum:{sum}")