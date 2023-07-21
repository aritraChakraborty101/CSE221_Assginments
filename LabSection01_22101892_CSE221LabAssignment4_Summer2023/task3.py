# inp = open("input3_1.txt", "r")
# out = open("output3_1.txt", "w")
#
# inp = open("input3_2.txt", "r")
# out = open("output3_2.txt", "w")
#
# inp = open("input3_3.txt", "r")
# out = open("output3_3.txt", "w")

inp = open("input3_4.txt", "r")
out = open("output3_4.txt", "w")

#############################################

# n = number of nodes and m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n+1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

print(graph)


##############################################

def dfs(graph_node, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    out.writelines(f"{start} ")
    print(start, end=" ")

    for neighbor in graph_node[start]:
        if neighbor not in visited:
            dfs(graph_node, neighbor, visited)


dfs(graph, 1)
