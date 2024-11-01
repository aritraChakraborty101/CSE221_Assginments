# inp = open("input1a_1.text", "r")
# out = open("output1a_1.text", "w")

# inp = open("input1a_2.text", "r")
# out = open("output1a_2.text", "w")

inp = open("input1a_3.text", "r")
out = open("output1a_3.text", "w")

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

# The main idea is to use Kahn's algorithm for topological sorting
# in this algorithm, we first calculate the in_degree of all vertices
# then we push all the vertices with in_degree = 0 into a queue
# then we pop the first element from the queue and append it to the result_order
# then we decrease the in_degree of all the vertices adjacent to the popped element
# if any of the in_degree becomes 0, we push that vertex into the queue
# we repeat this process until the queue is empty
# if the length of the result_order is not equal to the number of vertices
# then the graph has a cycle, and we return "IMPOSSIBLE"

# Time complexity: O(V + E)

###########################################################

def topological_sort(node):
    result_order = []
    queue = []
    in_degree = {}

    # initialize in_degree of all vertices to 0
    for vertex in range(1, n + 1):
        in_degree[vertex] = 0

    # calculate in_degree of all vertices
    for vertex in range(1, n + 1):
        for j in node[vertex]:
            in_degree[j] += 1

    for vertex in range(1, n + 1):
        if in_degree[vertex] == 0:
            queue.append(vertex)

    while queue:
        u = queue.pop(0)
        result_order.append(u)
        for vertex in node[u]:
            in_degree[vertex] -= 1
            if in_degree[vertex] == 0:
                queue.append(vertex)

    if len(result_order) != n:
        return "IMPOSSIBLE"
    return result_order


###########################################################


# calling the function and writing the output to file

result = topological_sort(graph)
if result == "IMPOSSIBLE":
    out.write(result)
else:
    for i in result:
        out.write(str(i) + " ")
