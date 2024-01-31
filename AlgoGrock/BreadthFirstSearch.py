# Алгоритм поиска в ширину в графе.
# Выполняется за O(V+E) - количество вершин + количество рёбер
from collections import deque

def BFS(graph,start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue+= graph[person]
                searched.append(person)
    print("False")
    return False

def person_is_seller(name):
    return name[-1]== "y"



#-------------------

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#-------------------

BFS(graph,"you")