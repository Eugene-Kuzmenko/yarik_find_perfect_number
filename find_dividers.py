import sys

def find_dividers(number):
  yield 1
  max_divider = number
  
  possible_divider = 2

  iterations = 1

  while possible_divider < max_divider:
    other_divider, remainder = divmod(number, possible_divider)
    max_divider = other_divider

    if not remainder:
      yield possible_divider
      
      if possible_divider != other_divider:
        yield other_divider

    possible_divider += 1
    iterations += 1

if __name__ == "__main__":
  dividers = list(find_dividers(int(sys.argv[1])))
  dividers.sort()
  print(f"dividers are {", ".join(str(divider) for divider in dividers)}")
