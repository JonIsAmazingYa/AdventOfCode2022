with open('input.txt') as fh:
  state_mode = True
  line = fh.readline()
  number_of_columns = int(len(line) / 4)
  columns = [[] for _ in range(number_of_columns)]

  while line:

    if line == '\n':
      state_mode = False
      line = fh.readline()
      continue

    if state_mode:
      for i in range(number_of_columns):
        parsed = line[4*i+1]
        if parsed != ' ':
          columns[i].insert(0, parsed)

    if not state_mode:
      line = line.split(' ')

      idx_donor = int(line[3])-1
      idx_recipient = int(line[5])-1
      num_to_move = int(line[1])

      to_move = columns[idx_donor][-num_to_move:]
      columns[idx_donor] = columns[idx_donor][0:-num_to_move]

      columns[idx_recipient].extend(to_move)

    line = fh.readline()

print(columns)
print(''.join([column[-1] for column in columns]))