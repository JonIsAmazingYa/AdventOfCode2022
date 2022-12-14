class CleanupSegment:

  def contains(self, other):
    if self.start_segment <= other.start_segment and self.end_segment >= other.end_segment:
      return True
    return False

  def overlaps_with(self, other):
    if self.start_segment <= other.start_segment and self.end_segment >= other.start_segment or \
      self.start_segment <= other.end_segment and self.end_segment >= other.end_segment:
      return True
    return False

  def __init__(self, input):
    self.start_segment, self.end_segment = input.split('-')
    self.start_segment = int(self.start_segment)
    self.end_segment = int(self.end_segment)
    if self.start_segment > self.end_segment:
      tmp = self.end_segment
      self.end_segment = self.start_segment
      self.start_segment = tmp

acc = 0

with open('input.txt') as fh:
  for line in fh.readlines():
    first, second = [CleanupSegment(input) for input in line.strip().split(',')]

    acc += first.overlaps_with(second) or second.overlaps_with(first)

print(acc)