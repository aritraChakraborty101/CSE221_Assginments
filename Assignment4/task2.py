# inp = open('input2_1.txt', 'r')
# out = open('output2_1.txt', 'w')

# inp = open('input2_2.txt', 'r')
# out = open('output2_2.txt', 'w')

# inp = open('input2_3.txt', 'r')
# out = open('output2_3.txt', 'w')

inp = open('input2_4.txt', 'r')
out = open('output2_4.txt', 'w')

######################################################

# create an adjacency list for unweighted graph


# Here n = number of vertices, m = number of edges
n, m = inp.readline().split()
n, m = int(n), int(m)

# creating an empty dictionary as an adjacency list
graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):
    node_1, node_2 = inp.readline().split()
    node_1, node_2 = int(node_1), int(node_2)
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


#######################################################


def bfs(graph, source):
    color = [0] * (n + 1)
    queue = []
    color[source] = 1  # source is colored as visited
    queue.append(source)  # append source to queue
    while queue:  # while queue is not empty
        node = queue.pop(0)
        out.writelines(str(node) + " ")

        for adjacent in graph[node]:  # for all adjacent nodes of node
            if color[adjacent] == 0:
                color[adjacent] = 1
                queue.append(adjacent)
    out.writelines("\n")


bfs(graph, 1)
