from graph import Graph, Nodes
from priorityQueue import pQueue


def heuristic(a, b):
  return abs(a.x - b.x) + abs(a.y - b.y)


def aStar(goal):
  while not frontier.empty():
    current = frontier.get()

    if current == goal:
      break

    for next in graph.neighbors(current):
      new_cost = costSoFar[current] + graph.cost(current, next)
      if next not in costSoFar or new_cost < costSoFar[next]:
        costSoFar[next] = new_cost
        priority = new_cost + heuristic(goal, next)
        frontier.put(next, priority)
        cameFrom[next] = current


graph = Graph()
frontier = pQueue()
start = None

file = input("Informe o nome do arquivo com o mapa: ")
file = file + '.txt' if not file.endswith('.txt') else file

with open(file) as grid:
  cont = 0
  for line in grid:
    if cont == 0:
      data = line.strip().split()
      graph.width, graph.height = int(data[0]), int(data[1])
      cont += 1
    elif cont == 1:
      start = line.strip().split()
      start = Nodes([int(x) for x in start])
      cont += 1
    else:
      temp = line.strip().split()
      x_cont = 0
      for value in temp:
        coord = [x_cont, cont - 2]
        node = Nodes(coord, int(value))
        graph.nodes.append(node)
        if node.x == start.x and node.y == start.y:
          start = graph.setStart(node)
        x_cont += 1
      cont += 1

cameFrom = {start: None}
frontier.put(start, 0)
costSoFar = {start: 0}

goalX = input("\nInforme o valor da coordenada x para onde se quer chegar: ")
goalY = input("Informe o valor da coordenada y para onde se quer chegar: ")

for i in graph.nodes:
  if i.x == int(goalX) and i.y == int(goalY):
    goal = i
    break

aStar(goal)
tcost, tlist = 0, []
for i in graph.nodes:
  if i in cameFrom:
    tlist.append(i)
    tcost += i.value
text = f"\n{tcost} -"
#não faz sentido tratar como lista (hash table não possui indíces), apenas para teste
for i in tlist:
  text += f' {i.x}.{i.y}'
print(text)
