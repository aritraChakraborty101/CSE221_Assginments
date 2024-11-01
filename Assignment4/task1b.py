inp = open("input1b_1.txt", "r")
out = open("output1b_1.txt", "w")

# inp = open("input1b_2.txt", "r")
# out = open("output1b_2.txt", "w")

# inp = open("input1b_3.txt", "r")
# out = open("output1b_3.txt", "w")

n, m = inp.readline().split()
n, m = int(n), int(m)

graph = {}
for i in range(n + 1):
    graph[i] = []
for i in range(m):

    # using unpacking method to assign values to the variables
    node_1, node_2, weight = inp.readline().split()
    node_1, node_2, weight = int(node_1), int(node_2), int(weight)
    graph[node_1].append((node_2, weight))

for i in range(n + 1):
    out.writelines(f"{i}: ")
    for j in graph[i]:
        out.writelines(f"{j} ")
    out.writelines("\n")
