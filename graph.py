class Graph:

  def __init__(self, width=None, height=None, start=None):
    self.nodes = []
    self.start = start if type(start) is Nodes else None
    self.width = width if type(width) is int else None
    self.height = height if type(height) is int else None

  def setStart(self, node):
    if type(node) is Nodes:
      for i in self.nodes:
        if i.x == node.x and i.y == node.y:
          node.value = 0
          self.start = node
          return self.start
    return False

  def neighbors(self, node):
    if isinstance(node, Nodes):
      neighbors = []
      x, y = node.x, node.y
      if x is not None and y is not None:
        for i in self.nodes:
          if (i.x == x and (i.y == y - 1 or i.y == y + 1)) or (
              (i.x == x - 1 or i.x == x + 1) and i.y == y):
            neighbors.append(i)
      return neighbors
    return False

  def cost(self, a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


class Nodes:

  def __init__(self, coords: list[int], exCost: int = 0):
    self.value = -1 if exCost == -1 else 1 + exCost
    self.y = coords[1]
    self.x = coords[0]
