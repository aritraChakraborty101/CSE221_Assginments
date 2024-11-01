# inp = open('input4_1.txt', 'r')
# out = open('output4_1.txt', 'w')

# inp = open('input4_2.txt', 'r')
# out = open('output4_2.txt', 'w')

inp = open('input4_3.txt', 'r')
out = open('output4_3.txt', 'w')

# inp = open('input4_4.txt', 'r')
# out = open('output4_4.txt', 'w')

# inp = open('input4_5.txt', 'r')
# out = open('output4_5.txt', 'w')

###########################################################

# create an adjacency list for unweighted graph

# Here n = number of vertices, m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)


###########################################################

def has_cycle(graph):
    # Here I have used set because it is faster than list for checking if an element is present in it.
    visited = set()
    path = set()

    # Here I have used a nested function dfs() to perform the actual depth-first search.
    # Nested function is necessary because we need to keep track of the visited nodes and the path.
    # If we use a global variable, then the visited nodes and the path will be overwritten for each call of dfs().
    # If we use a local variable, then the visited nodes and the path will not be accessible from the main function.
    def dfs(vertex):
        visited.add(vertex)
        path.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor in path:
                return True  # Cycle found

            if neighbor not in visited:
                if dfs(neighbor):
                    return True  # Cycle found
        # If we have reached here, then there is no cycle in the path from vertex to any of its descendants.
        path.remove(vertex)
        return False

    # The dfs function is called for each vertex in the graph.
    # If any of the dfs function calls returns True, then there is a cycle in the graph.
    # If none of the dfs function calls returns True, then there is no cycle in the graph.
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True  # Cycle found

    return False  # No cycle found

# DFS
###########################################################


result = has_cycle(graph)

if result:
    out.writelines("YES")
else:
    out.writelines("NO")