# I misread the requirements of this section and ended up trying to find out
# how many sections overlap globally. Nonetheless, I think it was an interesting
# problem to try to tackle.

acc = 0

ranges = []

def consider_range(new_range) -> bool:
  i = 0

  for i in range(len(ranges)):
    if ranges[i][0] <= new_range[0] and ranges[i][1] >= new_range[1]:
      # range is already covered completely by this range
      return False

  # range is not covered in any existing range
  ranges.insert(i, new_range)
  return True

sources = []

with open('sample.txt') as fh:
  for line in fh.readlines():
    sources.extend([[int(x), int(y)] for x, y in [input.split('-') for input in line.strip().split(',')]])

# Sort according to size largest > smallest
sources.sort(key=lambda pair: pair[1]-pair[0], reverse=True)

for source in sources:
  if consider_range(source):
    acc += 1

print(acc)

print(ranges)
