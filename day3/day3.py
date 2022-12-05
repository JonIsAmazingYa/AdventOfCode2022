priorities = {v: k for k,v in enumerate(char for char in '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

acc = 0
with open('input.txt') as fh:
  line = fh.readline()

  while line:
    line1 = line
    line2 = fh.readline()
    line3 = fh.readline()

    result = [char for char in line1 if char in line2 and char in line3][0]

    acc += priorities[result]

    line = fh.readline()

print(acc)