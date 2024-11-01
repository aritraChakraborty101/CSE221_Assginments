inp = open("input2_1.text", "r")
out = open("output2_1.text", "w")

# inp = open("input2_2.text", "r")
# out = open("output2_2.text", "w")

# inp = open("input2_3.text", "r")
# out = open("output2_3.text", "w")

###########################################################

# create an adjacency list for unweighted graph

# Here n = number of vertices, m = number of edges
from heapq import *
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)

color = {}
element = []
for i in graph.keys():
    color[i] = "white"
def BFS(graph, vertex, color, element):
    color[vertex] = "gray"
    for neighbour in graph[vertex]:
        if color[neighbour] == "white":
            cycle_found = BFS(graph, neighbour, color, element)
            if cycle_found:
                return True
            elif color[neighbour] == "gray":
                return True
    element.append(vertex)
    color[vertex] = "black"
    return False

def has_cycle(graph):
    visited = set()
    path = set()

    def dfs(vertex):
        visited.add(vertex)
        path.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor in path:
                return True
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        path.remove(vertex)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True

    return False

def topological_sort(graph):
    queue = []
    indegree = [0]*(n+1)
    for node in graph.keys():
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    for node in graph.keys():
        if indegree[node] == 0:
            heappush(queue, node)

    result = []
    while queue:
        vertex = heappop(queue)
        result.append(vertex)
        for neighbour in graph[vertex]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                heappush(queue, neighbour)

    return result


flag = has_cycle(graph)
if flag:
    print("IMPOSSIBLE")
else:
     final = topological_sort(graph)


for i in range(1, len(final)):
    out.write(str(final[i]) + " ")

