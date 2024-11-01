inp = open('input3_1.text', 'r')
out = open('output3_1.text', 'w')

# inp = open('input3_2.text', 'r')
# out = open('output3_2.text', 'w')

############################################
tuple_list = []
weight_list = []
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
    tuple_list.append((u, v))
    weight_list.append(w)
    adj_list[u][v] = w

start = 1
end = n

############################################


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_path(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

############################################


paths = find_path(adj_list, start, end)

result_arr = []
for path in paths:
    tmp_arr = []
    for j in range(len(path) - 1):
        first = path[j]
        second = path[j + 1]
        index = tuple_list.index((first, second))
        weight = weight_list[index]
        tmp_arr.append(weight)
    temp = max(tmp_arr)
    result_arr.append(temp)

result = min(result_arr)
out.write(str(result) + ' ')
print(result)

