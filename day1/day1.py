
class Elf:

  def __init__(self):
    self.food_carried: int = []

  def add_food(self, cals: int) -> None:
    self.food_carried.append(cals)

  def get_calories(self) -> int:
    return sum(self.food_carried)

elves = []
current_elf = Elf()

with open('input.txt') as fh:
  for line in fh.readlines():
    if line != '\n':
      current_elf.add_food(int(line))
    else:
      elves.append(current_elf)
      current_elf = Elf()

total_count = 0

for i in range(3):
  next_elf = max(elves, key=lambda elf: elf.get_calories())
  elves.remove(next_elf)
  total_count += next_elf.get_calories()

print(total_count)