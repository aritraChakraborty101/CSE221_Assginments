
# inp = open("input3_1.text", "r")
# out = open("output3_1.text", "w")

# inp = open("input3_2.text", "r")
# out = open("output3_2.text", "w")

inp = open("input3_3.text", "r")
out = open("output3_3.text", "w")

###########################################################

# create an adjacency list for unweighted graph

# Here n = number of vertices, m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(1, n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)


###########################################################


def dfs(node, vertex, visited, topological_order):
    visited[vertex] = True
    for neighbor in node[vertex]:
        if not visited[neighbor]:
            dfs(node, neighbor, visited, topological_order)
    topological_order.append(vertex)
    return topological_order

###########################################################


def transpose(node):
    transposed_form = {}
    for vertex in node:
        transposed_form[vertex] = []
    for vertex in node:
        for neighbor in node[vertex]:
            transposed_form[neighbor].append(vertex)

    return transposed_form

###########################################################


def strongly_connected_component(graph, topological_order, transposed_node):
    visited = {vertex: False for vertex in graph}
    result = []

    while topological_order:
        vertex = topological_order.pop()
        if not visited[vertex]:
            component = []
            dfs(transposed_node, vertex, visited, component)
            result.append(component)

    for vertex in graph:
        if not visited[vertex]:
            component = []
            dfs(transposed_node, vertex, visited, component)
            result.append(component)

    return result

###########################################################
# Here we first call the dfs function on all the nodes of the graph
# and store the topological ordering of the graph in the order variable
# We then transpose the graph and store it in the transposed_graph variable
# We then call the strongly_connected_component function on the graph, order and transposed_graph
# and store the result in the strongly_connected_components variable

# Time complexity: O(V + E)


transposed_graph = transpose(graph)

stack = []
visited = {vertex: False for vertex in graph}
order = dfs(graph, 1, visited, stack)


strongly_connected_components = strongly_connected_component(graph, order, transposed_graph)

for i in range(len(strongly_connected_components)):
    for j in range(len(strongly_connected_components[i])):
        strongly_connected_components[i][j] = str(strongly_connected_components[i][j])
        out.write(strongly_connected_components[i][j] + " ")
    out.write("\n")
