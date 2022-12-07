from day2_object_oriented import Rock, Paper, Scissors

class Play:

  source_keys = {
    'X': Rock,
    'A': Rock,
    'Y': Paper,
    'B': Paper,
    'Z': Scissors,
    'C': Scissors
  }

  @classmethod
  def create(cls, key):
    # Can we do something here to dynamically change the type at runtime?
    return Play.source_keys[key]()

  def wins(self, other):
    if isinstance(other, self.beats):
      return True
    return False