class CleanupSegment:

  def contains(self, other):
    if self.start_segment <= other.start_segment and self.end_segment >= other.end_segment:
      return True
    return False

  def __init__(self, input):
    self.start_segment, self.end_segment = input.split('-')
    if self.start_segment > self.end_segment:
      tmp = self.end_segment
      self.end_segment = self.start_segment
      self.start_segment = tmp

acc = 0

with open('sample.txt') as fh:
  for line in fh.readlines():
    first, second = [CleanupSegment(input) for input in line.strip().split(',')]

    acc += first.contains(second) or second.contains(first)

print(acc)