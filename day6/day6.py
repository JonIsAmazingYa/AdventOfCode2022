length_of_marker = 14

with open('input.txt') as fh:
  for line in fh.readlines():
    for i in range(length_of_marker, len(line)):
      most_recent_four = line[i-length_of_marker:i]
      stored = set(most_recent_four)
      if len(stored) == length_of_marker:
        print(i)
        break