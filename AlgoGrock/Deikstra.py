# Алгоритм Дейкстры, в целом база

# Graph data

graph = {}
graph["start"]={}
graph["start"]["a"]= 6
graph["start"]["b"]= 2
# print(graph["start"].keys()
graph["a"]={}
graph["a"]["fin"]=1
graph["b"]={}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#---------------------------
# Cost Data
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
#-------------------------
# Parenst Data
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
#------------------------
#Список уже обработанных вершин!
processed = []
#------------------------

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
# Найти узел с наименьшей стоимостью среди необработанных
while node is not None:
# Если обработаны все узлы, цикл завершается
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
    # Перебрать всех соседей текущего узла.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
        # Если к соседу можно быстрее добраться через текущий узел
        # обновиться стоимость этого узла.
        # Этот узел становится новым родителем для соседа.
            costs[n] = new_cost
            parents[n] = node
    processed.append(node) # Узел помечается как обработанныйц
    node = find_lowest_cost_node(costs) # Найти следующий узел для обработки и повторить цикл.

print(graph)
print(costs)
print(parents)