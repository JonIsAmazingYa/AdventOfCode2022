priorities = {v: k for k,v in enumerate(char for char in '0abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ')}

acc = 0
with open('sample.txt') as fh:
  for line in fh.readlines():
    result = [char for char in line[:int(len(line)/2)] if char in line[int(len(line)/2):]][0]

    print(result)

    print(priorities[result])

    acc += priorities[result]

print(acc)