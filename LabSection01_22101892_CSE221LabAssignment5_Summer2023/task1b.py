# inp = open("input1b_1.text", "r")
# out = open("output1b_1.text", "w")

# inp = open("input1b_2.text", "r")
# out = open("output1b_2.text", "w")

inp = open("input1b_3.text", "r")
out = open("output1b_3.text", "w")

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

# In this solution, we use DFS to find the topological ordering of the graph
# We first create a visited array to keep track of the visited nodes
# We then create a stack to store the topological ordering of the graph
# We then call the dfs function on all the nodes of the graph
# In the dfs function, we first mark the current node as visited
# Then we recursively call the dfs function on all the adjacent nodes of the current node
# After all the adjacent nodes have been visited, we push the current node into the stack
# After all the nodes have been visited, we pop the elements from the stack and append them to the result_order
# We then reverse the result_order to get the topological ordering of the graph
# If the length of the result_order is not equal to the number of vertices
# then the graph has a cycle, and we return "IMPOSSIBLE"

# Time complexity: O(V + E)

###########################################################

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
    visited = [False] * (n + 1)
    stack = []
    result = []

    # here I have used nested functions to avoid passing the visited,
    # stack and result variables as parameters to the dfs function
    # the dfs function should also detect if the graph has a cycle
    # if the graph has a cycle, then we return "IMPOSSIBLE"

    def dfs(node):
        visited[node] = True
        for adjacent_node in graph[node]:
            if not visited[adjacent_node]:
                dfs(adjacent_node)
        stack.append(node)

    if has_cycle(graph):
        return "IMPOSSIBLE"

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)

    while stack:
        result.append(stack.pop())

    if len(result) != n:
        return "IMPOSSIBLE"
    else:
        return result


###########################################################


result_order = topological_sort(graph)

if result_order == "IMPOSSIBLE":
    out.write(result_order)
    out.write("\n")
else:
    for i in result_order:
        out.write(str(i) + " ")
    out.write("\n")
