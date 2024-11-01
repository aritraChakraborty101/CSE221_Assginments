inp = open('input2_1.text', 'r')
out = open('output2_1.text', 'w')

# inp = open('input2_2.text', 'r')
# out = open('output2_2.text', 'w')

# inp = open('input2_3.text', 'r')
# out = open('output2_3.text', 'w')

############################################

# Read input
first_line = inp.readline().split()
n = int(first_line[0])
m = int(first_line[1])

# Create adjacency list with dictionaries

adj_list = {}
for i in range(1, n + 1):
    adj_list[i] = {}

for line in range(m):
    line = inp.readline().split()
    u = int(line[0])
    v = int(line[1])
    w = int(line[2])
    adj_list[u][v] = w

last_line = inp.readline().split()
source1 = int(last_line[0])
source2 = int(last_line[1])


############################################

# Dijkstra's algorithm that return all the element of the shortest path tree
# if we cant find the path to the vertex, the distance is -1
# import heapq and store the vertices in a min heap

import heapq


def dijkstra(graph, source_element):
    distance = {}
    prev = {}
    for node in graph:
        distance[node] = float('inf')
        prev[node] = None
    distance[source_element] = 0
    pq = []
    heapq.heappush(pq, (distance[source_element], source_element))
    while pq:
        min_vertex = heapq.heappop(pq)[1]
        for neighbour in graph[min_vertex]:
            if distance[neighbour] > distance[min_vertex] + graph[min_vertex][neighbour]:
                distance[neighbour] = distance[min_vertex] + graph[min_vertex][neighbour]
                prev[neighbour] = min_vertex
                heapq.heappush(pq, (distance[neighbour], neighbour))
    return distance


############################################

alice_path = dijkstra(adj_list, source1)
bob_path = dijkstra(adj_list, source2)

############################################
flag = False
min_time = float('inf')
min_vertex = None

for vertex in alice_path:
    if vertex in bob_path:
        if max(alice_path[vertex],bob_path[vertex]) < min_time:
            min_time = max(alice_path[vertex], bob_path[vertex])
            min_vertex = vertex
            flag = True


if flag:
    out.write("Time " + str(min_time))
    out.write("\n")
    out.write("Node " + str(min_vertex))
else:
    out.write("Impossible")
