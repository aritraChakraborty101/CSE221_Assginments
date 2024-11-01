# All test case file are included below

# inp = open("input5_1.txt", "r")
# out = open("output5_1.txt", "w")

# inp = open("input5_2.txt", "r")
# out = open("output5_2.txt", "w")

inp = open("input5_3.txt", "r")
out = open("output5_3.txt", "w")

# inp = open("input5_4.txt", "r")
# out = open("output5_4.txt", "w")

# inp = open("input5_5.txt", "r")
# out = open("output5_5.txt", "w")

#############################################

# Creating a graph with adjacency list

n, m, d = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


#############################################

def dfs(graph, start, end, visited, path, shortest_path):
    visited[start] = True
    path.append(start)

    if start == end:
        # If the shortest path is empty or the current path is shorter than the shortest path
        # Then update the shortest path
        if not shortest_path or len(path) < len(shortest_path):
            # This way I can copy the list without reference
            # Otherwise, it will be a reference to the original list
            shortest_path[:] = path[:]
    else:
        for neighbor in graph[start]:
            if not visited[neighbor]:
                dfs(graph, neighbor, end, visited, path, shortest_path)

    path.pop()
    visited[start] = False


def find_shortest_path(graph, start, end):
    visited = {}
    for node in graph:
        visited[node] = False

    shortest_path = []

    dfs(graph, start, end, visited, [], shortest_path)
    return shortest_path


#############################################

# In this way rather than finding the shortest path from 1 to d
# I am finding the shortest path from d to 1 and then reverse it
# The reason is a target node will always know its parent node,
# and eventually It will return to the source node

shortpath = find_shortest_path(graph, int(d), 1)

if len(shortpath) == 0:
    out.write("IMPOSSIBLE")
else:
    out.write(str(len(shortpath) - 1) + "\n")
    for i in range(len(shortpath) - 1, -1, -1):
        out.write(str(shortpath[i]) + " ")

print(shortpath)
