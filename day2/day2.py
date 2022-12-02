score_map = {
  'X': 1,
  'Y': 2,
  'Z': 3,
}

beats_map = {
  'X': 'C',
  'Y': 'A',
  'Z': 'B',
  'A': 'Z',
  'B': 'X',
  'C': 'Y'
}

beats_map_inv = {v: k for k, v in beats_map.items()}

def get_winner(me, opponent) -> int:
  if beats_map[me] == opponent:
    return 6
  elif beats_map[opponent] == me:
    return 0
  return 3

def play(me, opponent) -> int:
  return score_map[me] + get_winner(me, opponent)

def get_play(opponent, outcome) -> int:
  if outcome == 'X':
    return play(beats_map[opponent], opponent)
  elif outcome == 'Y':
    wins_or_loses = (beats_map[opponent], beats_map_inv[opponent])
    for key in score_map.keys():
      if key not in wins_or_loses:
        return play(key, opponent)
  else:
    return play(beats_map_inv[opponent], opponent)

score = 0

with open('input.txt') as fh:
  line = fh.readline()
  while line:
    plays = line.strip().split(' ')
    # score += play(plays[1], plays[0])
    score += get_play(plays[0], plays[1])

    line = fh.readline()

print(score)