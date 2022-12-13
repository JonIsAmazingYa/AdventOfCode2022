class File:
  def __init__(self, name, size: int):
    self.name = name
    self.size: int = size

  def __str__(self):
    return f'{self.name} (file, size={self.size})'

class Directory:
  def __init__(self, name: str, parent=None):
    self.name = name
    self.children: list[Directory] = []
    self.files: list[File] = []
    self.parent = parent

  def add_child(self, new_name):
    new_node = Directory(new_name, self)
    self.children.append(new_node)
    return new_node

  def __str__(self):
    return f'{self.name} (dir)'


root_node = Directory('/')
current_node = root_node

with open('input.txt') as fh:
  for line in fh.readlines():
    line = line.strip().split(' ')
    if line[0] == '$':
      if line[1] == 'cd':
        if line[2] == '/':
          current_node = root_node
          continue
        if line[2] == '..':
          current_node = current_node.parent
          continue
        else:
          try:
            existing_node = next(node for node in current_node.children if node.name == line[2])
          except StopIteration:
            existing_node = None
          if existing_node:
            current_node = existing_node
          else:
            current_node = current_node.add_child(line[2])

      # in the simple case all printed output that is not a command
      # is output -- we could add a state if there was more complex output
      if line[1] == 'ls':
        continue
    
    # line is not a command
    else:
      if line[0] == 'dir':
        current_node.add_child(line[1])
      else:
        current_node.files.append(File(line[1], int(line[0])))

def dfs(node: Directory, action):
  action(node)
  for file in node.files:
    action(file)
  for child in node.children:
    dfs(child, action)

directory_sizes = {}

def solve_recur(node: Directory, path=''):
  directory_sizes[path] = 0
  for file in node.files:
    directory_sizes[path] += file.size
  for child in node.children:
    solve_recur(child, path=path+'/'+child.name)
    directory_sizes[path] += directory_sizes[path+'/'+child.name]

solve_recur(root_node)

# acc = 0
# for directory, size in directory_sizes.items():
#   if size <= 100000:
#     print(directory, size)
#     acc += size
# print(acc)

space_to_free = 30000000 + directory_sizes[''] - 70000000
print(space_to_free)

sorted_sizes = sorted(directory_sizes.values())

for size in sorted_sizes:
  if size >= space_to_free:
    print(size)
    break
