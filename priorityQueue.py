class pQueue:

  def __init__(self):
    self.list = []
    self.size = 0

  def empty(self):
    return bool(not self.list)

  def get(self):
    if not self.empty():
      first = self.list[0]
      self.list.pop(0)
      self.size -= 1
      return first.obj
    return False

  def put(self, obj, priValue):
    node = pqNode(obj, priValue)
    if self.empty():
      self.list.append(node)
    else:
      for i, x in enumerate(self.list):
        if node.priority < x.priority:
          self.list.insert(i, node)
          break
      else:
        self.list.append(node)
    self.size += 1
    return node


class pqNode:

  def __init__(self, obj, value):
    self.obj = obj
    self.priority = value
