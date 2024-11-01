inp = open('input1_1.text', 'r')
out = open('output1_1.text', 'w')

# inp = open('input1_2.text', 'r')
# out = open('output1_2.text', 'w')

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

source = inp.readline()
source = int(source)

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

dist = dijkstra(adj_list, source)

for vertex in dist:
    if dist[vertex] == float('inf'):
        out.write(str(-1) + ' ')
    else:
        out.write(str(dist[vertex]) + ' ')
